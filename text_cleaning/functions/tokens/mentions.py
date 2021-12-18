from typing import List

from text_cleaning import chars, replacements
from text_cleaning.functions.base import ReplaceInTokens


class ReplaceMentions(ReplaceInTokens):

    def __init__(self, replacement: str = replacements.MENTION):
        super().__init__(replacement=replacement)
        self.regex = r'[\s%s](?P<target>@[\w]+)([\s%s]|$)' \
                     % (chars.punctuation, chars.punctuation)

    def clean(self, tokens: List[str], **kwargs) -> List[str]:
        tokens = [self.clean_token(x) for x in tokens]
        return tokens

    def clean_token(self, token: str) -> str:
        return self.replace_all(self.regex, self.replacement, token)
