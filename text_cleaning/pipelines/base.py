from abc import ABC
from typing import List

from text_cleaning.functions.base import CleanText, CleanTokens


class TextCleaningPipeline(ABC):

    def __init__(self, functions: List[CleanText]):
        self.functions = functions

    def __call__(self, text: str, **kwargs) -> str:
        for fn in self.functions:
            text = fn(text, **kwargs)
        return text


class TokensCleaningPipeline(ABC):

    def __init__(self, functions: List[CleanTokens]):
        self.functions = functions

    def __call__(self, tokens: List[str], **kwargs) -> List[str]:
        for fn in self.functions:
            tokens = fn(tokens, **kwargs)
        return tokens
