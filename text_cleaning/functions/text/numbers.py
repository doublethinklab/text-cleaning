import re

from text_cleaning import replacements
from text_cleaning.functions.base import ReplaceInText


class ReplaceNumbers(ReplaceInText):

    def __init__(self,
                 replacement: str = replacements.NUMBER,
                 min_num_digits: int = 3,
                 only_numbers: bool = False):
        super().__init__(replacement=replacement)
        self.min_num_digits = min_num_digits
        self.only_numbers = only_numbers

    def clean(self, text: str, **kwargs) -> str:
        # digit threshold: numbers with less than this number of digits are kept
        regex = r'%s[\d０１２３４５６７８９]{%s,}(st|rd|th)?%s' \
                % ('^' if self.only_numbers else '',
                   self.min_num_digits,
                   '$' if self.only_numbers else '')
        text = re.sub(regex, self.replacement, text)
        return text


class RemoveNumbers(ReplaceNumbers):

    def __init__(self,
                 min_num_digits: int = 2,
                 only_numbers: bool = True):
        super().__init__(
            replacement='',
            min_num_digits=min_num_digits,
            only_numbers=only_numbers)


# class ReplaceNumbers2(Clean):
#
#     def clean(self, text_or_token: str, *args, **kwargs) -> str:
#         return replace.numbers(text_or_token, NUM)
