from text_cleaning import regexps
from text_cleaning.functions.base import ReplaceInText


class RemoveHashtags(ReplaceInText):

    def __init__(self):
        super().__init__(replacement='')

    def clean(self, text: str, **kwargs) -> str:
        return self.replace_all(
            regex=regexps.hashtag,
            text=text,
            replacement=self.replacement)
