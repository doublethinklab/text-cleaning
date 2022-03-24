import re
from typing import List

from data_structures.nlp import Token

from text_cleaning import regexps
from text_cleaning.functions.base import ReplaceInTokens


class RemovePunctuation(ReplaceInTokens):

    def __init__(self, keep_hashtags: bool = False):
        super().__init__(replacement='')
        self.keep_hashtags = keep_hashtags
        self.regex = regexps.r_punctuation
        if self.keep_hashtags:
            self.regex = self.regex.replace('\#', '')
            self.regex = self.regex.replace('#', '')
        self.regex = re.compile(self.regex)

    def clean(self,
              tokens: List[Token],
              copy_meta_attrs_on_split: bool = False,
              **kwargs) -> List[Token]:
        for token in tokens:
            token.text = re.sub(self.regex, self.replacement, token.text)
        return tokens
