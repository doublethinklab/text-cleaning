from text_cleaning import chars
from text_cleaning.functions.base import ReplaceInText


class RemoveTrailingApostropheS(ReplaceInText):

    def __init__(self):
        super().__init__(replacement='')
        self.regex = r"[\w]+(?P<target>['’]s)([\s%s]|$)" % chars.punctuation

    def clean(self, text: str, **kwargs) -> str:
        return self.replace_all(self.regex, '', text)
