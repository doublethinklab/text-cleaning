from abc import ABC
from typing import Callable, List, Union

from text_cleaning.functions.base import CleanText, CleanTokens


def debug_message(text_or_tokens: Union[str, List[str]],
                  function: Callable) -> None:
    print('-' * 8)
    print(type(function))
    print(text_or_tokens)


class TextCleaningPipeline(ABC):

    def __init__(self, functions: List[CleanText], debug: bool = False):
        self.functions = functions
        self.debug = debug

    def __call__(self, text: str, **kwargs) -> str:
        for fn in self.functions:
            text = fn(text, **kwargs)
            if self.debug:
                debug_message(text, fn)
        return text


class TokensCleaningPipeline(ABC):

    def __init__(self, functions: List[CleanTokens], debug: bool = False):
        self.functions = functions
        self.debug = debug

    def __call__(self, tokens: List[str], **kwargs) -> List[str]:
        for fn in self.functions:
            tokens = fn(tokens, **kwargs)
            if self.debug:
                debug_message(tokens, fn)
        return tokens
