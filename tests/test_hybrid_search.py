import sys
import unittest

sys.path.append("src")
from hybrid_search import RankedDocument, fuse


class HybridSearchTests(unittest.TestCase):
    def test_document_in_both_sources_wins(self):
        results = fuse({"bm25": [RankedDocument("a", 1), RankedDocument("b", 2)], "vector": [RankedDocument("b", 1)]})
        self.assertEqual(results[0].document_id, "b")
        self.assertEqual(results[0].sources, ("bm25", "vector"))

    def test_equal_scores_are_stable(self):
        results = fuse({"bm25": [RankedDocument("z", 1), RankedDocument("a", 1)]})
        self.assertEqual([r.document_id for r in results], ["a", "z"])

    def test_invalid_rank_is_rejected(self):
        with self.assertRaises(ValueError):
            fuse({"vector": [RankedDocument("a", 0)]})


if __name__ == "__main__":
    unittest.main()
