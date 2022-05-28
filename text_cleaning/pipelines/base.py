from abc import ABC
from typing import Callable, Dict, List, Optional, Type, Union

from data_structures.nlp import Token

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

    def includes(self, function_type: Type) -> bool:
        return function_type in [type(x) for x in self.functions]

    def pass_down_logger_and_debug_flag(self):
        for fn in self.functions:
            fn.logger = self.logger
            fn.debug = self.debug

    def remove(self, function_type: Type) -> None:
        fn = next((x for x in self.functions
                   if isinstance(x, function_type)),
                  None)
        if fn:
            self.functions.remove(fn)


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

    def __call__(
            self,
            text: str,
            standardization_rules: Optional[Dict[str, List[str]]] = None,
            **kwargs
    ) -> str:
        for fn in self.functions:
            text = fn(
                text,
                standardization_rules=standardization_rules,
                **kwargs)
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

    def __call__(self,
                 tokens: List[Union[Token, str]],
                 return_strings: bool = True,
                 **kwargs) \
            -> List[Union[Token, str]]:
        # if no input, just return
        if not tokens or len(tokens) == 0:
            return tokens

        # if a list of strings is input, automatically map to Tokens to pass
        # to the cleaning functions
        if isinstance(tokens[0], str):
            tokens = [Token(text=x) for x in tokens]

        # clean
        for fn in self.functions:
            tokens = fn(tokens, return_strings=return_strings, **kwargs)
            if self.debug:
                self.debug_message(tokens, fn)

        return tokens
