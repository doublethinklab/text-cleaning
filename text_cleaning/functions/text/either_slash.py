from text_cleaning import regexps
from text_cleaning.functions.base import ReplaceInText


class ReplaceEitherSlashWithSpace(ReplaceInText):

    def __init__(self):
        super().__init__(replacement=' ')
        self.regex = regexps.either_slash

    def clean(self, text: str, *args, **kwargs) -> str:
        return self.replace_all(self.regex, ' ', text)
