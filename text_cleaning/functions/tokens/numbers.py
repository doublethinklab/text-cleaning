from copy import copy
from typing import List

from data_structures.nlp import Token

from text_cleaning import chars, replacements
from text_cleaning.functions.base import ReplaceInTokens
from text_cleaning.functions.text import numbers as clean_text_numbers


class ReplaceTooManyNumbers(ReplaceInTokens):

    def __init__(self,
                 replacement: str = replacements.NUMBER,
                 ratio_threshold: float = 0.5,
                 length_threshold: int = 3):
        super().__init__(replacement=replacement)
        self.ratio_threshold = ratio_threshold
        self.length_threshold = length_threshold

    # TODO: when I come back - no, not in the constructor, in __call__... thanks

    def clean(self,
              tokens: List[Token],
              copy_meta_attrs_on_split: bool = False,
              **kwargs) -> List[Token]:
        return [self.clean_token(x) for x in tokens]

    def clean_token(self, token: Token) -> Token:
        if len(token) < self.length_threshold:
            return token
        n_digits = sum(1 for c in token.text if c in chars.digits)
        if n_digits / len(token) > self.ratio_threshold:
            token.text = self.replacement
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
                 replacement: str = replacements.NUMBER,
                 digit_threshold: int = 2,
                 split_replacement: bool = False,
                 only_numbers: bool = True):
        super().__init__(replacement=replacement)
        self.digit_threshold = digit_threshold
        self.split_replacement = split_replacement
        self.only_numbers = only_numbers
        self.clean_text = clean_text_numbers.ReplaceNumbers(
            replacement=replacement,
            min_num_digits=digit_threshold,
            only_numbers=only_numbers)

    def clean(self,
              tokens: List[Token],
              copy_meta_attrs_on_split: bool = False,
              **kwargs) -> List[Token]:
        # trick here is to make sure NUM is separated from things like 年 and 日
        repl = self.replacement
        tokens_out = []
        for token in tokens:
            token.text = self.clean_text(token.text)
            if self.split_replacement and repl in token.text \
                    and len(token.text) > len(repl):
                # case where NUM is at the start
                if token.text[0:len(repl)] == repl:
                    tok_repl = self.new_token_from_split(
                        token, repl, copy_meta_attrs_on_split)
                    token.text = token.text.replace(repl, '')
                    tokens_out.append(tok_repl)
                    tokens_out.append(token)
                # case where NUM is in the middle
                elif token.text[-len(repl):] != repl:
                    repl_ix = token.text.index(repl)
                    start_tok = self.new_token_from_split(
                        token, token.text[0:repl_ix], copy_meta_attrs_on_split)
                    repl_tok = self.new_token_from_split(token, repl)
                    end_tok = self.new_token_from_split(
                        token, token.text[repl_ix + len(repl):],
                        copy_meta_attrs_on_split)
                    tokens_out.append(start_tok)
                    tokens_out.append(repl_tok)
                    tokens_out.append(end_tok)
                # case where NUM is at the end
                else:
                    tok_repl = self.new_token_from_split(
                        token, repl, copy_meta_attrs_on_split)
                    token.text = token.text.replace(repl, '')
                    tokens_out.append(token)
                    tokens_out.append(tok_repl)
            else:
                if token.text != '':
                    tokens_out.append(token)
        return tokens_out

    @staticmethod
    def new_token_from_split(token: Token,
                             new_text: str,
                             copy_meta_attrs_on_split: bool = False) -> Token:
        if copy_meta_attrs_on_split:
            new_token = copy(token)
            new_token.text = new_text
        else:
            new_token = Token(text=new_text)
        return new_token
