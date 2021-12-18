from text_cleaning.functions.base import CleanText


class LowerCase(CleanText):

    def clean(self, text: str, **kwargs) -> str:
        return text.lower()
