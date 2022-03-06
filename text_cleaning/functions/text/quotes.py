from quote_extraction.direct_quotes import replace
from text_cleaning import replacements
from text_cleaning.functions.base import ReplaceInText


class ReplaceQuotes(ReplaceInText):

    def __init__(
            self,
            replacement: str = replacements.QUOTE,
            logger=None,
            debug: bool = False
    ):
        super().__init__(
            replacement=replacement,
            logger=logger,
            debug=debug)

    def clean(self, text: str, **kwargs) -> str:
        text = replace(text, replacement=self.replacement)
        return text
