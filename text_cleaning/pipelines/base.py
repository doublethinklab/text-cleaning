from abc import ABC
from typing import Callable, List, Union

from text_cleaning.functions.base import Clean, CleanText, CleanTokens


class CleaningPipeline(ABC):

    def __init__(self,
                 logger=None,
                 debug: bool = False):
        self.logger = logger
        self.debug = debug
        self.functions = []

    def debug_message(self,
                      text_or_tokens: Union[str, List[str]],
                      function: Callable) -> None:
        self.logger.debug('-' * 8)
        self.logger.debug(type(function))
        self.logger.debug(text_or_tokens)

    def get_function(self, function_type: type) -> Union[Clean, None]:
        return next(
            (x for x in self.functions if isinstance(x, function_type)),
            None)

    def pass_down_logger_and_debug_flag(self):
        for fn in self.functions:
            fn.logger = self.logger
            fn.debug = self.debug


class TextCleaningPipeline(CleaningPipeline):

    def __init__(self,
                 functions: List[CleanText],
                 logger=None,
                 debug: bool = False):
        super().__init__(
            logger=logger,
            debug=debug)
        self.functions = functions
        self.pass_down_logger_and_debug_flag()

    def __call__(self, text: str, **kwargs) -> str:
        for fn in self.functions:
            text = fn(text, **kwargs)
            if self.debug:
                self.debug_message(text, fn)
        return text


class TokensCleaningPipeline(CleaningPipeline):

    def __init__(self,
                 functions: List[CleanTokens],
                 logger=None,
                 debug: bool = False):
        super().__init__(
            logger=logger,
            debug=debug)
        self.functions = functions
        self.pass_down_logger_and_debug_flag()

    def __call__(self, tokens: List[str], **kwargs) -> List[str]:
        for fn in self.functions:
            tokens = fn(tokens, **kwargs)
            if self.debug:
                self.debug_message(tokens, fn)
        return tokens
