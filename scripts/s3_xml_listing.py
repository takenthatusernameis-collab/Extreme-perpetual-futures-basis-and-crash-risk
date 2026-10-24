import urllib.request, hashlib, json, sys, re
from datetime import datetime, timezone, timedelta
from xml.etree import ElementTree as ET

BUCKET = "https://s3-ap-northeast-1.amazonaws.com/data.binance.vision"

def fetch(url):
    with urllib.request.urlopen(url) as r:
        return r.read()

def list_keys(prefix, max_keys=1000):
    keys = []
    marker = ""
    while True:
        url = f"{BUCKET}?prefix={prefix}&max-keys={max_keys}"
        if marker:
            url += f"&marker={marker}"
        data = fetch(url)
        h = hashlib.sha256(data).hexdigest()
        root = ET.fromstring(data)
        ns = "{http://s3.amazonaws.com/doc/2006-03-01/}"
        for c in root.findall(f"{ns}Contents"):
            key = c.find(f"{ns}Key").text
            keys.append(key)
        truncated = root.find(f"{ns}IsTruncated")
        if truncated is not None and truncated.text == "true":
            marker = root.find(f"{ns}NextMarker")
            if marker is None or marker.text is None:
                # derive from last key
                marker = keys[-1] if keys else None
            else:
                marker = marker.text
            if not marker:
                break
        else:
            break
    return keys, h

def extract_dates(keys):
    dates = set()
    for k in keys:
        m = re.search(r"-(\d{4}-\d{2}-\d{2})\.zip$", k)
        if m:
            dates.add(m.group(1))
    return sorted(dates)

def enumerate_missing(dates, start, end):
    d = datetime.strptime(start, "%Y-%m-%d").date()
    endd = datetime.strptime(end, "%Y-%m-%d").date()
    all_dates = []
    cur = d
    while cur <= endd:
        all_dates.append(cur.isoformat())
        cur += timedelta(days=1)
    present = set(dates)
    missing = [x for x in all_dates if x not in present]
    return all_dates, missing

if __name__ == "__main__":
    prefix = sys.argv[1] if len(sys.argv) > 1 else "data/futures/um/daily/indexPriceKlines/ETHUSDT/1d/"
    keys, h = list_keys(prefix)
    dates = extract_dates(keys)
    if dates:
        all_dates, missing = enumerate_missing(dates, dates[0], dates[-1])
    else:
        all_dates, missing = [], []
    out = {
        "prefix": prefix,
        "n_keys": len(keys),
        "n_zip_dates": len(dates),
        "earliest": dates[0] if dates else None,
        "latest": dates[-1] if dates else None,
        "missing_count": len(missing),
        "missing_sample": missing[:50],
        "sha256_last_page": h,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    print(json.dumps(out, indent=2))
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w") as f:
            json.dump({"prefix": prefix, "dates": dates, "missing": missing, "n_keys": len(keys)}, f, indent=2)
