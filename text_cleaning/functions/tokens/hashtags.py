from typing import List

from data_structures.nlp import Token

from text_cleaning import regexps
from text_cleaning.functions.base import ReplaceInTokens


class NormalizeHashtags(ReplaceInTokens):

    def __init__(self, logger = None, debug: bool = False):
        super().__init__(replacement='', logger=logger, debug=debug)

    def clean(self,
              tokens: List[Token],
              copy_meta_attrs_on_split: bool = False,
              **kwargs) -> List[Token]:
        tokens_out = []
        for token in tokens:
            if regexps.matches_target(token.text, regexps.hashtag):
                if token.text[-1] == '#':
                    token.text = token.text[0:-1]
            tokens_out.append(token)
        return tokens_out
