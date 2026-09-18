import json, sys
from dataclasses import asdict
from src.hybrid_search import RankedDocument, fuse
for line in sys.stdin:
    if line.strip():
        payload=json.loads(line)
        rankings={source:[RankedDocument(**doc) for doc in docs] for source,docs in payload["rankings"].items()}
        print(json.dumps({"results":[asdict(item) for item in fuse(rankings, payload.get("k",60))]}))
