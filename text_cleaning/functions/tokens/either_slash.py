from typing import List

from text_cleaning import regexps
from text_cleaning.functions.base import ReplaceInTokens


class ReplaceEitherSlashWithSpace(ReplaceInTokens):

    def __init__(self):
        super().__init__(replacement=' ')
        self.regex = regexps.either_slash

    def clean(self, tokens: List[str], **kwargs) -> List[str]:
        tokens = [self.replace_all(self.regex, x, ' ') for x in tokens]
        tokens = self.split_on_space(tokens)
        return tokens
