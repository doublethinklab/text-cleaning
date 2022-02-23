from quote_extraction.direct_quotes import replace
from text_cleaning.functions.base import ReplaceInText


class ReplaceQuotes(ReplaceInText):

    def clean(self, text: str, **kwargs) -> str:
        text = replace(text, replacement=self.replacement)
        return text
