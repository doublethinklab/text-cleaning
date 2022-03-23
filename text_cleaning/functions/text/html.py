import re

from text_cleaning import regexps
from text_cleaning.functions.base import ReplaceInText


class RemoveHtml(ReplaceInText):

    def __init__(self):
        super().__init__(replacement=' ')

    def clean(self, text: str, **kwargs) -> str:
        # NOTE: replace with a space to avoid joining strings
        #  but is still semantically a "remove" function
        text = re.sub(regexps.html, self.replacement, text)
        return text
