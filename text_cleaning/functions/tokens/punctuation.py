import re
from typing import List

from data_structures.nlp import Token

from text_cleaning import regexps
from text_cleaning.functions.base import ReplaceInTokens


class RemovePunctuation(ReplaceInTokens):

    def __init__(
            self,
            exclude_hashtags: bool = False,
            exclude_mentions: bool = False
    ):
        super().__init__(replacement='')
        self.exclude_hashtags = exclude_hashtags
        self.exclude_mentions = exclude_mentions

    def clean(self,
              tokens: List[Token],
              copy_meta_attrs_on_split: bool = False,
              **kwargs) -> List[Token]:
        for token in tokens:
            if self.exclude_mentions:
                if token.is_mention \
                        or regexps.matches_target(token.text, regexps.mention):
                    continue
            if self.exclude_hashtags:
                if token.is_hashtag \
                        or regexps.matches_target(token.text, regexps.hashtag):
                    continue
            token.text = re.sub(
                regexps.punctuation, self.replacement, token.text)
        return tokens
