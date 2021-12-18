import re

from text_cleaning import chars, regexps
from text_cleaning.functions.base import ReplaceInText


class ReplacePunctuation(ReplaceInText):

    def clean(self, text: str, **kwargs) -> str:
        regex = regexps.punctuation
        return re.sub(regex, '', text)


class RemovePunctuation(ReplacePunctuation):

    def __init__(self):
        super().__init__(replacement='')
