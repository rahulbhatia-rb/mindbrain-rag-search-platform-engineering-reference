# RAG Search Platform Reference

A compact, tested hybrid-retrieval core tailored to MindBrain's Search & Platform Engineer contract. It illustrates transparent lexical/vector fusion, deterministic ranking, and retrieval metadata that an API or RAG service can expose for debugging.

## What it demonstrates

- reciprocal-rank fusion (RRF) across lexical and vector retrieval results
- stable tie-breaking for reproducible search behaviour
- explicit retrieval diagnostics rather than opaque ranking output
- dependency-free Python tests, ready to place behind FastAPI or a worker

## Run

```bash
python3 -m unittest discover -s tests -v
python3 -m src.app < examples/rankings.jsonl
```

The example produces explainable reciprocal-rank-fusion results, including the
retrieval sources behind each document—useful evidence for a RAG platform.

## Integration shape

An OpenSearch adapter can translate BM25 and kNN result lists into `RankedDocument` values, call `fuse()`, and return the fused results with source ranks. In production I would add tenant filters, index-version identifiers, query tracing, relevance evaluation datasets, latency SLOs, and Prometheus metrics.

## Scope and candour

This is a role-specific engineering reference, not a claim that I have operated MindBrain's clinical-search data or that it is clinical decision-support software. It is informed by my AWS GenAI/RAG deployment work and focuses on a safe, inspectable retrieval primitive.

## Contact

[LinkedIn](https://www.linkedin.com/in/rahul-h-bhatia/) · [Portfolio](https://rahulhbhatia.vercel.app) · [Credly](https://www.credly.com/users/rahul-h-bhatia/badges)
