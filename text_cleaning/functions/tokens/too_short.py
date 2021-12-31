from typing import List

from text_cleaning.functions.base import CleanTokens


class RemoveTooShortTokens(CleanTokens):
    # cleans up some garbage
    # only for english and spanish

    def __init__(self,
                 min_length: int = 2,
                 exceptions: List[str] = ['i', 'a', 'y']):
        super().__init__()
        self.min_length = min_length
        self.exceptions = exceptions

    def clean(self, tokens: List[str], **kwargs) -> List[str]:
        tokens = [x for x in tokens
                  if len(x) >= self.min_length
                  or x in self.exceptions]
        return tokens
