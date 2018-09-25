from GoogleNext.similarity.shared_tokens_measure import distinct_intersection_size
from GoogleNext.similarity.similarity_measure import SimilarityMeasure


class DiceCoefficientMeasure(SimilarityMeasure):

    def score(self, document_tokens, query_tokens):
        intersection_size = distinct_intersection_size(query_tokens, document_tokens)
        return 2 * intersection_size / (len(query_tokens) + len(document_tokens))
