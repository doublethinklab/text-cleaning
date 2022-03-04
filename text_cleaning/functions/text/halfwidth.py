from text_cleaning.functions.base import CleanText
import unicodedata

class NormalizeTextWidth(CleanText):

    def clean(self, text:str, **kwargs) -> str:
        # https://stackoverflow.com/questions/2422177/python-how-can-i-replace-full-width-characters-with-half-width-characters
        return unicodedata.normalize('NFKC', text)