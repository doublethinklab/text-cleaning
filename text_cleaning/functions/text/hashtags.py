import re

from text_cleaning import chars
from text_cleaning.functions.base import ReplaceInText


class RemoveHashtags(ReplaceInText):

    def __init__(self):
        super().__init__(replacement='')
        self.regex = r'([\s%s]|^)(?P<target>#[\w\d]+)([\s%s]|$)' \
                     % (re.escape(chars.punctuation),
                        re.escape(chars.punctuation))

    def clean(self, text: str, **kwargs) -> str:
        return self.replace_all(
            regex=self.regex,
            text=text,
            replacement=self.replacement)
