from opencc import OpenCC

from text_cleaning.functions.base import CleanText


class TraditionalToSimplified(CleanText):

    def __init__(self):
        super().__init__()
        self.t2s = OpenCC('t2s')

    def clean(self, text: str, **kwargs) -> str:
        return self.t2s.convert(text)
