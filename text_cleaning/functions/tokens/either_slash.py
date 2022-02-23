from typing import List

from data_structures.nlp import Token

from text_cleaning import regexps
from text_cleaning.functions.base import ReplaceInTokens


class ReplaceEitherSlashWithSpace(ReplaceInTokens):

    def __init__(self):
        super().__init__(replacement=' ')
        self.regex = regexps.either_slash

    def clean(self,
              tokens: List[Token],
              copy_meta_attrs_on_split: bool = False,
              **kwargs) -> List[Token]:
        for token in tokens:
            token.text = self.replace_all(self.regex, token.text, ' ')
            token.text = token.text.replace('  ', ' ')
        tokens = self.split_on_space(tokens)
        return tokens
