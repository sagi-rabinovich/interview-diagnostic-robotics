from typing import List

from GoogleNext.tokenizer.tokenizer import Tokenizer


class PathTokenizer(Tokenizer):

    def __init__(self, path_separator: str = "/") -> None:
        super().__init__()

        if not path_separator:
            raise ValueError("path_separator should be a non-empty string")

        self.__path_separator = path_separator

    def tokenize(self, document) -> List[str]:
        parts = document.split(self.__path_separator)
        current_path = ""
        tokens = []
        for part in parts:
            current_path += part
            tokens.append(current_path)
            current_path += self.__path_separator
        return tokens
