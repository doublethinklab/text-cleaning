from typing import List

from data_structures.nlp import Token
from textacy.preprocessing import replace

from text_cleaning import replacements as repl
from text_cleaning.functions.base import ReplaceInTokens


class ReplaceUrls(ReplaceInTokens):

    def __init__(self, replacement: str = repl.URL):
        super().__init__(replacement=replacement)

    def clean(self, tokens: List[Token], **kwargs) -> List[Token]:
        for token in tokens:
            token.text = replace.urls(token.text, repl=self.replacement)
        return tokens


class RemoveUrls(ReplaceUrls):

    def __init__(self):
        super().__init__(replacement='')
