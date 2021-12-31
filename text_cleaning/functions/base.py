from abc import ABC, abstractmethod
import re
from typing import List


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
            if 'target' in match.groupdict():
                target = match.groupdict()['target']
                text = text.replace(target, replacement)
            matches = self.look_for_matches(regex, text)
        return text.strip()


class CleanText(Clean):

    def __call__(self, text: str, **kwargs) -> str:
        return self.clean(text, **kwargs)

    @abstractmethod
    def clean(self, text: str, **kwargs) -> str:
        raise NotImplementedError


class CleanTokens(Clean):

    def __call__(self, tokens: List[str], **kwargs) -> List[str]:
        tokens = self.clean(tokens, **kwargs)
        tokens = self.drop_null(tokens)
        return tokens

    @abstractmethod
    def clean(self, tokens: List[str], **kwargs) -> List[str]:
        raise NotImplementedError

    @staticmethod
    def drop_null(tokens: List[str]) -> List[str]:
        return [x for x in tokens
                if x != '' and x is not None]

    @staticmethod
    def split_on_space(tokens: List[str]) -> List[str]:
        tokens_out = []
        for x in tokens:
            if ' ' in x:
                tokens_out += x.split(' ')
            else:
                tokens_out.append(x)
        return tokens_out


class ReplaceInText(CleanText, ABC):

    def __init__(self, replacement: str, logger=None, debug: bool = False):
        super().__init__(logger, debug)
        self.replacement = replacement


class ReplaceInTokens(CleanTokens, ABC):

    def __init__(self, replacement: str, logger=None, debug: bool = False):
        super().__init__(logger, debug)
        self.replacement = replacement
