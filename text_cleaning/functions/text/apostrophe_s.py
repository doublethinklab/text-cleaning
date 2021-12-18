from text_cleaning import chars
from text_cleaning.functions.base import ReplaceInText


class RemoveTrailingApostropheS(ReplaceInText):

    def __init__(self):
        super().__init__(replacement='')
        self.regex = r"[\w]+" \
                     r"(?P<target>['’]s)" \
                     r"([\s%s]|$)" % chars.word_end_punct

    def clean(self, text: str, **kwargs) -> str:
        text = self.replace_all(
            regex=self.regex,
            text=text,
            replacement=self.replacement)
        return text
