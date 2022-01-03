from abc import ABC, abstractmethod
import re
from typing import List, Union

from data_structures.nlp import Token


class Clean(ABC):

    def __init__(self, logger=None, debug: bool = False):
        self.logger = logger
        self.debug = debug

    def look_for_matches(self, regex: str, text: str):
        if self.debug:
            self.logger.debug(f'Looking for regex "{regex}" in text "{text}"')
        matches = list(re.finditer(regex, text))
        if self.debug:
            self.logger.debug(f'Found {len(matches)} matches.')
        return matches

    def replace_all(self, regex: str, text: str, replacement: str) -> str:
        assert '(?P<target>' in regex
        matches = self.look_for_matches(regex, text)
        while len(matches) > 0:
            match = matches[0]
            if self.debug:
                self.logger.debug(f'Looking at first match: {match}')
            if 'target' in match.groupdict():
                target = match.groupdict()['target']
                if self.debug:
                    self.logger.debug('`target` is: %r' % target)
                text = text.replace(target, replacement)
                if self.debug:
                    self.logger.debug('Text after replacement: %r' % text)
            else:
                if self.debug:
                    self.logger.debug('`target` not in match groupdict keys: '
                                      '%s.'
                                      % ', '.join(match.groupdict().keys()))
            matches = self.look_for_matches(regex, text)
        return text.strip()


class CleanText(Clean):

    def __call__(self, text: str, **kwargs) -> str:
        return self.clean(text, **kwargs)

    @abstractmethod
    def clean(self, text: str, **kwargs) -> str:
        raise NotImplementedError


class CleanTokens(Clean):

    def __init__(self,
                 logger=None,
                 debug: bool = False):
        super().__init__(logger, debug)

    def __call__(self,
                 tokens: List[Union[Token, str]],
                 return_strings: bool = True,
                 copy_meta_attrs_on_split: bool = False,
                 **kwargs) \
            -> List[Union[Token, str]]:
        # if no input, just return the input
        if not tokens or len(tokens) == 0:
            return tokens

        # if the input is strings, automatically map to tokens for the
        # implementation of the cleaning functions
        if isinstance(tokens[0], str):
            tokens = [Token(text=x) for x in tokens]

        # clean
        tokens = self.clean(
            tokens=tokens,
            copy_meta_attrs_on_split=copy_meta_attrs_on_split,
            **kwargs)

        # drop any nulled tokens
        tokens = self.drop_null(tokens)

        # map to strings if consumers requests
        if return_strings:
            tokens = [x.text for x in tokens]

        return tokens

    @abstractmethod
    def clean(self,
              tokens: List[Token],
              copy_meta_attrs_on_split: bool = False,
              **kwargs) -> List[Token]:
        raise NotImplementedError

    @staticmethod
    def drop_null(tokens: List[Token]) -> List[Token]:
        return [x for x in tokens
                if x.text != '' and x.text is not None]

    @staticmethod
    def split_on_space(tokens: List[Token],
                       copy_meta_attrs_on_split: bool = False) -> List[Token]:
        tokens_out = []
        for x in tokens:
            if ' ' in x.text:
                tokens_out += x.split(
                    split_on=' ',
                    copy_meta_attrs=copy_meta_attrs_on_split)
            else:
                tokens_out.append(x)
        return tokens_out


class ReplaceInText(CleanText, ABC):

    def __init__(self, replacement: str, logger=None, debug: bool = False):
        super().__init__(logger, debug)
        self.replacement = replacement


class ReplaceInTokens(CleanTokens, ABC):

    def __init__(self,
                 replacement: str,
                 logger=None,
                 debug: bool = False):
        super().__init__(
            logger=logger,
            debug=debug)
        self.replacement = replacement
