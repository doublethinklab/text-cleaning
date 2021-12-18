from text_cleaning import chars
from text_cleaning.functions.base import ReplaceInTokens


class RemoveHashtags(ReplaceInTokens):

    def __init__(self):
        super().__init__(replacement='')
        self.regex = r'([\s%s]|^)(?P<target>#[\w]+)([\s%s]|$)' \
                     % (chars.punctuation, chars.punctuation)

    def clean(self, text: str, **kwargs) -> str:
        return self.replace_all(self.regex, '', text)
