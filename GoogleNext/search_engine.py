import threading
from typing import List, Tuple

from GoogleNext.similarity.shared_tokens_measure import SharedTokensMeasure
from GoogleNext.similarity.similarity_measure import SimilarityMeasure
from GoogleNext.tokenizer.delimiter_tokenizer import DelimiterTokenizer
from GoogleNext.tokenizer.tokenizer import Tokenizer


class SearchEngine:
    def __init__(self, similarity_measure: SimilarityMeasure = None, tokenizer: Tokenizer = None) -> None:
        super().__init__()
        self.__similarityMeasure = similarity_measure or SharedTokensMeasure()
        self.__tokenizer = tokenizer or DelimiterTokenizer()
        self.__documents: List[str] = []
        self.__indexLock = threading.Lock()

    def index(self, documents: List[str]) -> None:
        if documents is None:
            raise TypeError("documents cannot be None")

        documents_to_index = []
        for document in documents:
            tokens = self.__tokenizer.tokenize(document)
            documents_to_index.append(_IndexedDocument(document, tokens))
        with self.__indexLock:
            self.__documents.extend(documents_to_index)

    def search(self, query: str) -> List[Tuple[str, float]]:
        if query is None:
            raise TypeError("query cannot be None")

        query_tokens = self.__tokenizer.tokenize(query)
        search_results = []

        with self.__indexLock:
            documents = self.__documents.copy()

        for document in documents:
            score = self.__similarityMeasure.score(document.tokens, query_tokens)
            if score > 0:
                search_results.append((document.source, score))

        search_results.sort(key=lambda r: r[1], reverse=True)
        return search_results


class _IndexedDocument:
    def __init__(self, document: str, tokens: List[str]) -> None:
        super().__init__()
        self.source = document
        self.tokens = tokens
