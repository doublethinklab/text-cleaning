import re

from text_cleaning import regexps, replacements
from text_cleaning.functions.base import ReplaceInText


class ReplaceMentions(ReplaceInText):

    def __init__(self, replacement: str = replacements.MENTION):
        super().__init__(replacement=replacement)
        self.regex = regexps.mention

    def clean(self, text: str, **kwargs) -> str:
        return self.replace_all(
            regex=self.regex,
            text=text,
            replacement=self.replacement)
