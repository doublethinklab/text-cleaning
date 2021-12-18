import re

from text_cleaning import regexps, replacements as repl
from text_cleaning.functions.base import ReplaceInText


class ReplacePunctuation(ReplaceInText):

    def __init__(self, replacement: str = repl.PUNCTUATION):
        super().__init__(replacement=replacement)

    def clean(self, text: str, **kwargs) -> str:
        regex = regexps.punctuation
        return re.sub(regex, self.replacement, text)


class RemovePunctuation(ReplacePunctuation):

    def __init__(self):
        super().__init__(replacement='')
