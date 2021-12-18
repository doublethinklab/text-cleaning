from typing import List

from text_cleaning.functions.base import ReplaceInTokens


class ReplaceHyphenCompoundWithSpace(ReplaceInTokens):

    def __init__(self):
        super().__init__(replacement=' ')
        self.regex = r'[\w\d]+(?P<target>-)[\w\d]+'

    def clean(self, tokens: List[str], **kwargs) -> List[str]:
        tokens = [self.clean_token(x) for x in tokens]
        tokens = self.split_on_space(tokens)
        return tokens

    def clean_token(self, token: str) -> str:
        return self.replace_all(self.regex, self.replacement, token)
