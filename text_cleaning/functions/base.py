from abc import ABC, abstractmethod
import re
from typing import Dict, List


class Clean(ABC):

    @staticmethod
    def replace_all(regex: str, text: str, replacement: str) -> str:
        assert '(?P<target>' in regex
        for match in re.finditer(regex, text):
            if 'target' in match.groupdict():
                target = match.groupdict()['target']
                text = text.replace(target, replacement)
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

    def __init__(self, replacement: str):
        self.replacement = replacement


class ReplaceInTokens(CleanTokens, ABC):

    def __init__(self, replacement: str):
        self.replacement = replacement
