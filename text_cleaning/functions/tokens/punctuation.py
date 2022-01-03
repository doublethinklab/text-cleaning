import re
from typing import List

from data_structures.nlp import Token

from text_cleaning import regexps
from text_cleaning.functions.base import ReplaceInTokens


class RemovePunctuation(ReplaceInTokens):

    def __init__(self):
        super().__init__(replacement='')
        self.regex = regexps.punctuation

    def clean(self,
              tokens: List[Token],
              copy_meta_attrs_on_split: bool = False,
              **kwargs) -> List[Token]:
        for token in tokens:
            token.text = re.sub(self.regex, self.replacement, token.text)
        return tokens
