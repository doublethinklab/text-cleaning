from text_cleaning.functions.base import ReplaceInText


class ReplaceEitherSlashWithSpace(ReplaceInText):

    def __init__(self):
        super().__init__(replacement=' ')
        self.regex = r'(\s|^)[\w]+(?P<target>/)[\w]+([\s.,]|$)'

    def clean(self, text: str, *args, **kwargs) -> str:
        return self.replace_all(self.regex, ' ', text)
