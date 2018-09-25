from typing import List

from GoogleNext.tokenizer.tokenizer import Tokenizer


class DelimiterTokenizer(Tokenizer):
    def __init__(self, delimiter: str = ' ') -> None:
        super().__init__()

        if not delimiter:
            raise ValueError("delimiter should be a non-empty string")

        self.__delimiter = delimiter

    def tokenize(self, document) -> List[str]:
        return [t for t in document.split(self.__delimiter) if t != ""]
