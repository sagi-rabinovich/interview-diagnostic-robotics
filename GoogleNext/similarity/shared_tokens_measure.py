from GoogleNext.similarity.similarity_measure import SimilarityMeasure


class SharedTokensMeasure(SimilarityMeasure):
    def score(self, document_tokens, query_tokens):
        return distinct_intersection_size(query_tokens, document_tokens)


# just to prove that I care about duplicate code :)
def distinct_intersection_size(listA, listB):
    distinct_a = set(listA)
    return sum([1 for a in distinct_a if a in listB])
