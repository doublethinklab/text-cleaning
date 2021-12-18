from typing import List

from text_cleaning import chars, replacements
from text_cleaning.functions.base import ReplaceInTokens
from text_cleaning.functions.text import numbers as clean_text_numbers


class ReplaceTooManyNumbers(ReplaceInTokens):

    def __init__(self,
                 replacement: str = replacements.NUM,
                 ratio_threshold: float = 0.5,
                 length_threshold: int = 3):
        super().__init__(replacement=replacement)
        self.ratio_threshold = ratio_threshold
        self.length_threshold = length_threshold

    def clean(self, tokens: List[str], **kwargs) -> List[str]:
        return [self.clean_token(x) for x in tokens]

    def clean_token(self, token: str) -> str:
        if len(token) < self.length_threshold:
            return token
        n_digits = sum(1 for c in token if c in chars.digits)
        if n_digits / len(token) > self.ratio_threshold:
            return self.replacement
        return token


class RemoveTooManyNumbers(ReplaceTooManyNumbers):

    def __init__(self,
                 ratio_threshold: float = 0.5,
                 length_threshold: int = 3):
        super().__init__(
            replacement='',
            ratio_threshold=ratio_threshold,
            length_threshold=length_threshold)


class ReplaceNumbers(ReplaceInTokens):

    def __init__(self,
                 replacement: str = replacements.NUM,
                 digit_threshold: int = 2,
                 split_replacement: bool = False,
                 only_numbers: bool = True):
        super().__init__(replacement=replacement)
        self.digit_threshold = digit_threshold
        self.split_replacement = split_replacement
        self.only_numbers = only_numbers
        self.clean_text = clean_text_numbers.ReplaceNumbers(
            replacement=replacement,
            digit_threshold=digit_threshold,
            split_replacement=split_replacement,
            only_numbers=only_numbers)

    def clean(self, tokens: List[str], **kwargs) -> List[str]:
        # trick here is to make sure NUM is separated from things like 年 and 日
        repl = self.replacement
        tokens_out = []
        for t in tokens:
            t = self.clean_text(t)
            if self.split_replacement and repl in t and len(t) > len(repl):
                # case where NUM is at the start
                if t[0:len(repl)] == repl:
                    tokens_out.append(repl)
                    tokens_out.append(t.replace(repl, ''))
                # case where NUM is in the middle
                elif t[-len(repl):] != repl:
                    tokens_out.append(t[0:t.index(repl)])
                    tokens_out.append(repl)
                    tokens_out.append(t[t.index(repl) + len(repl):])
                # case where NUM is at the end
                else:
                    tokens_out.append(t.replace(repl, ''))
                    tokens_out.append(repl)
            else:
                if t != '':
                    tokens_out.append(t)
        return tokens_out
