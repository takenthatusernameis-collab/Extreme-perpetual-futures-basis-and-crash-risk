import csv, hashlib, io, json, urllib.request, zipfile
from datetime import datetime, timezone

BASE = "https://data.binance.vision/data"
SYMBOL = "BTCUSDT"
DAY = "2024-01-01"

def fetch(url):
    with urllib.request.urlopen(url) as r:
        return r.read()

def kline_zip(path):
    url = f"{BASE}/{path}/{SYMBOL}/1d/{SYMBOL}-1d-{DAY}.zip"
    data = fetch(url)
    z = zipfile.ZipFile(io.BytesIO(data))
    name = z.namelist()[0]
    txt = z.read(name).decode()
    rows = list(csv.reader(io.StringIO(txt)))
    # open_time_ms, open, high, low, close, volume, close_time_ms, ...
    data_rows = [r for r in rows if r and r[0].isdigit()]
    closes = [float(r[4]) for r in data_rows]
    open_ms = int(data_rows[0][0])
    close_ms = int(data_rows[0][6])
    dt = datetime.fromtimestamp(open_ms/1000, tz=timezone.utc).date().isoformat()
    return {"date": dt, "n_bars": len(rows), "close_median": sorted(closes)[len(closes)//2] if closes else None,
            "open_time_ms": open_ms, "close_time_ms": close_ms, "raw_sha256": hashlib.sha256(data).hexdigest()}

spot = kline_zip("spot/daily/klines")
um = kline_zip("futures/um/daily/klines")
mark = kline_zip("futures/um/daily/markPriceKlines")
index = kline_zip("futures/um/daily/indexPriceKlines")

# funding monthly
ym = DAY[:7]
furl = f"{BASE}/futures/um/monthly/fundingRate/{SYMBOL}/{SYMBOL}-fundingRate-{ym}.zip"
fdata = fetch(furl)
fz = zipfile.ZipFile(io.BytesIO(fdata))
ftxt = fz.read(fz.namelist()[0]).decode()
frows = list(csv.reader(io.StringIO(ftxt)))
# header? check
header = frows[0]
# find calc_time column
ci = header.index("calc_time") if "calc_time" in header else 0
fi = header.index("last_funding_rate") if "last_funding_rate" in header else None
day_funding = []
for r in frows[1:]:
    if not r: continue
    ts = int(r[ci])
    d = datetime.fromtimestamp(ts/1000, tz=timezone.utc).date().isoformat()
    if d == DAY:
        day_funding.append(float(r[fi]))
funding_median = sorted(day_funding)[len(day_funding)//2] if day_funding else None

basis = None
if mark["close_median"] is not None and index["close_median"] is not None:
    basis = 100*(mark["close_median"]/index["close_median"] - 1)

out = {
  "symbol": SYMBOL,
  "date": DAY,
  "spot": spot,
  "um_kline": um,
  "mark": mark,
  "index": index,
  "funding_rates_on_day": day_funding,
  "funding_median": funding_median,
  "basis_pct": basis,
  "funding_raw_sha256": hashlib.sha256(fdata).hexdigest(),
  "funding_header": header,
}
with open("research_state/ingestion_prototype_sample.json","w") as f:
    json.dump(out, f, indent=2)
print(json.dumps(out, indent=2))
print("header:", header)
