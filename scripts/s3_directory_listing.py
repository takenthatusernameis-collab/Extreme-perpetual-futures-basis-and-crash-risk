import re, urllib.request, hashlib, json, sys
from datetime import datetime, timezone

BASE = "https://data.binance.vision"

def fetch(url):
    with urllib.request.urlopen(url) as r:
        return r.read()

def list_files(prefix):
    url = f"{BASE}/?prefix={prefix}"
    data = fetch(url)
    text = data.decode("utf-8", "replace")
    # extract hrefs pointing to zip files
    links = re.findall(r'href="([^"]+)"', text)
    zips = [l for l in links if l.endswith(".zip")]
    # normalize to filenames
    names = [l.split("/")[-1] for l in zips]
    return sorted(set(names)), hashlib.sha256(data).hexdigest(), datetime.now(timezone.utc).isoformat()

if __name__ == "__main__":
    prefix = sys.argv[1] if len(sys.argv) > 1 else "data/futures/um/daily/indexPriceKlines/ETHUSDT/1d/"
    names, h, ts = list_files(prefix)
    out = {"prefix": prefix, "n_files": len(names), "files": names, "sha256": h, "retrieved_at_utc": ts}
    print(json.dumps(out, indent=2)[:4000])
