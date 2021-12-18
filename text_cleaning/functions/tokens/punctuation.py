import re
from typing import List

from text_cleaning import regexps
from text_cleaning.functions.base import ReplaceInTokens


class RemovePunctuation(ReplaceInTokens):

    def __init__(self):
        super().__init__(replacement='')
        self.regex = regexps.punctuation

    def clean(self, tokens: List[str], **kwargs) -> List[str]:
        tokens = [re.sub(self.regex, self.replacement, x) for x in tokens]
        return tokens
