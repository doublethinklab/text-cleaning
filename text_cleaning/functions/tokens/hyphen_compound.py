from typing import List

from data_structures.nlp import Token

from text_cleaning.functions.base import ReplaceInTokens


class ReplaceHyphenCompoundWithSpace(ReplaceInTokens):

    def __init__(self):
        super().__init__(replacement=' ')
        self.regex = r'[\w\d]+(?P<target>-)[\w\d]+'

    def clean(self,
              tokens: List[Token],
              copy_meta_attrs_on_split: bool = False,
              **kwargs) -> List[Token]:
        tokens = [self.clean_token(x) for x in tokens]
        tokens = self.split_on_space(tokens)
        return tokens

    def clean_token(self, token: Token) -> Token:
        token.text = self.replace_all(self.regex, token.text, self.replacement)
        return token
