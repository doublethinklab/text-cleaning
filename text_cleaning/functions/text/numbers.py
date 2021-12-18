import re

from text_cleaning import replacements
from text_cleaning.functions.base import ReplaceInText


class ReplaceNumbers(ReplaceInText):

    def __init__(self,
                 replacement: str = replacements.NUM,
                 digit_threshold: int = 2,
                 split_replacement: bool = False,
                 only_numbers: bool = True):
        super().__init__(replacement=replacement)
        self.digit_threshold = digit_threshold
        self.split_replacement = split_replacement
        self.only_numbers = only_numbers

    def clean(self, text: str, **kwargs) -> str:
        # digit threshold: numbers with less than this number of digits are kept
        regex = r'%s[\d０１２３４５６７８９]{%s,}(st|rd|th)?%s' \
                % ('^' if self.only_numbers else '',
                   self.digit_threshold,
                   '$' if self.only_numbers else '')
        text = re.sub(regex, self.replacement, text)
        return text


class RemoveNumbers(ReplaceNumbers):

    def __init__(self,
                 digit_threshold: int = 2,
                 split_replacement: bool = False,
                 only_numbers: bool = True):
        super().__init__(replacement='')
        self.digit_threshold = digit_threshold
        self.split_replacement = split_replacement
        self.only_numbers = only_numbers


# class ReplaceNumbers2(Clean):
#
#     def clean(self, text_or_token: str, *args, **kwargs) -> str:
#         return replace.numbers(text_or_token, NUM)
