from text_cleaning import regexps, replacements
from text_cleaning.functions.base import ReplaceInText


class ReplaceUrls(ReplaceInText):

    def __init__(
            self,
            replacement: str = replacements.URL,
            logger = None,
            debug: bool = False
    ):
        super().__init__(
            replacement=replacement,
            logger=logger,
            debug=debug)

    def clean(self, text: str, **kwargs) -> str:
        text = self.replace_all(
            regex=regexps.url,
            text=text,
            replacement=self.replacement)
        return text


class RemoveUrls(ReplaceUrls):

    def __init__(self, logger = None, debug: bool = False):
        super().__init__(replacement='', logger=logger, debug=debug)
