from dataclasses import dataclass
from collections import defaultdict


@dataclass(frozen=True)
class RankedDocument:
    document_id: str
    rank: int


@dataclass(frozen=True)
class FusedResult:
    document_id: str
    score: float
    sources: tuple[str, ...]


def fuse(rankings: dict[str, list[RankedDocument]], k: int = 60) -> list[FusedResult]:
    """Fuse ranked lists using reciprocal-rank fusion with explainable sources."""
    scores: dict[str, float] = defaultdict(float)
    sources: dict[str, list[str]] = defaultdict(list)
    for source, documents in rankings.items():
        for document in documents:
            if document.rank < 1:
                raise ValueError("rank must start at 1")
            scores[document.document_id] += 1 / (k + document.rank)
            sources[document.document_id].append(source)
    return sorted(
        (FusedResult(doc_id, score, tuple(sources[doc_id])) for doc_id, score in scores.items()),
        key=lambda item: (-item.score, item.document_id),
    )
