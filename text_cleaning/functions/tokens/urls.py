from typing import List

from textacy.preprocessing import replace

from text_cleaning.functions.base import ReplaceInTokens


class ReplaceUrls(ReplaceInTokens):

    def clean(self, tokens: List[str], **kwargs) -> List[str]:
        return [replace.urls(x, repl=self.replacement) for x in tokens]


class RemoveUrls(ReplaceUrls):

    def __init__(self):
        super().__init__(replacement='')
