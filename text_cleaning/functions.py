"""Specific cleaning functions."""
import re
from typing import List, Union

from opencc import OpenCC
from textacy.preprocessing import normalize, replace

from text_cleaning import chars


class CleaningFunction:
    """Base cleaning function.

    Implements two functions, one for text, one for a token. The reason is that
    the cleaning strategy will differ depending on whether the cleaning function
    is applied before or after tokenization.

    There are generally two types of cleaning function:
    - replace noisy text with some token
    - remove noisy text
    Removal can be seen as a sub-type of replacing, where the replacement is the
    empty string.

    For semantic clarity, the implementing classes are called `ReplaceX` or
    `RemoveX`. But for implementation, the constructor here has a `replace_with`
    argument. In order to avoid repeated code, this allows for defining a
    `ReplaceX` function, and then sub-classing that as a `RemoveX(Replace(X)`
    where the constructor defines `replace_with=''`.
    """

    def __init__(self, replacement: str):
        self.replacement = replacement

    def __call__(self, data: Union[str, List[str]], **kwargs):
        if isinstance(data, str):
            return self.clean_text(data, **kwargs)
        elif isinstance(data, list):
            tokens = self.clean_tokens(data, **kwargs)
            return self.remove_empty(tokens)
        else:
            raise ValueError(f'Unexpected data type: {type(data)}')

    def clean_text(self, text: str, **kwargs) -> str:
        raise NotImplementedError

    def clean_tokens(self, tokens: List[str], **kwargs) -> List[str]:
        # default implementation is to apply `clean_text` to all
        return [self.clean_text(x, **kwargs) for x in tokens]

    @staticmethod
    def remove_empty(tokens: List[str]) -> List[str]:
        return [x for x in tokens if x is not None and x != '']

    @staticmethod
    def replace_all(regex: str, text: str, replacement: str) -> str:
        assert '(?P<target>' in regex
        for match in re.finditer(regex, text):
            if 'target' in match.groupdict():
                target = match.groupdict()['target']
                text = text.replace(target, replacement)
        return text.strip()


class ReplaceUrls(CleaningFunction):
    # NOTE: will only work on already tokenized or English - i.e. needs spaces

    def clean_text(self, text: str, **kwargs) -> str:
        raise NotImplementedError('Only works on tokens for now.')

    def clean_tokens(self, tokens: List[str], **kwargs) -> List[str]:
        return [replace.urls(x, repl=self.replacement) for x in tokens]


class RemoveUrls(ReplaceUrls):

    def __init__(self):
        super().__init__(replacement='')


class ReplacePunctuation(CleaningFunction):

    def clean_text(self, text: str, **kwargs) -> str:
        regex = r'[%s]' % chars.punctuation
        return re.sub(regex, '', text)


class RemovePunctuation(ReplacePunctuation):

    def __init__(self):
        super().__init__(replacement='')


class ReplaceDigits(CleaningFunction):
    # NOTE: handles １２３ chars as well as 123
    # TODO: this doesn't permit of a digit threshold

    def clean_text(self, text: str, **kwargs) -> str:
        return replace.numbers(text, self.replacement)


class ReplaceOrdinals(CleaningFunction):

    def clean_text(self, text: str, **kwargs) -> str:
        pass


class RemoveOrdinals(ReplaceOrdinals):

    def __init__(self):
        super().__init__(replacement='')


class ReplaceDateMonthYearDigits(CleaningFunction):

    pass


class RemoveDateMonthYearDigits(ReplaceDateMonthYearDigits):

    def __init__(self):
        super().__init__(replacement='')


class ReplaceTokensWithTooManyNumbers(CleaningFunction):

    def __init__(self, replacement: str, threshold: float = 0.5):
        super().__init__(replacement)
        self.threshold = threshold

    def clean_text(self, text: str, **kwargs) -> str:
        raise NotImplementedError('Only implemented for tokens.')

    def clean_tokens(self, tokens: List[str], **kwargs) -> List[str]:
        return [self.replacement if self.too_many_digits(x) else x
                for x in tokens]

    @staticmethod
    def too_many_digits(token: str) -> bool:
        n_digits = sum(1 for c in token if c in chars.digits)
        return n_digits > 0.5 * len(token)


class RemoveTokensWithTooManyNumbers(ReplaceTokensWithTooManyNumbers):

    def __init__(self):
        super().__init__(replacement='')


# TODO: with all these different ways of handling numbers, should I just collect
#  them all into a single ReplaceNumbers function, with boolean options?


class NormalizeWhitespace(CleaningFunction):
    """Implements normalization as in textacy:

    Replace all contiguous zero-width spaces with an empty string,
    line-breaking spaces with a single newline, and non-breaking spaces with a
    single space, then strip any leading/trailing whitespace."""

    def clean_text(self, text: str, **kwargs) -> str:
        return normalize.whitespace(text)


class ReplaceGarbage(CleaningFunction):
    """We rule in valid characters to avoid enumerating all garbage.

    This is the set of English, Chinese, and Japanese characters, including
    their punctuation marks, and digits.
    """

    def __init__(self,
                 replace_with: str = JUNK,
                 languages: List[str] = SUPPORTED_LANGUAGES):
        self.replace_with = replace_with
        self.languages = languages
        self.regex = self.build_regex(languages)

    def build_regex(self, languages: List[str]):
        regex = '[^'
        if 'en_US' in languages:
            regex += en_chars
        if 'zh_CN' in languages or 'zh_TW' in languages:
            regex += zh_chars
        if 'ja_JP' in languages:
            regex += ja_chars
        if 'es_ES' in languages:
            regex += es_chars
            regex += en_chars
        regex += punctuation
        regex += all_digits
        regex += '\s+]'
        return regex

    def clean_text(self, text: str, **kwargs) -> str:
        return re.sub(self.regex, self.replace_with, text)


class RemoveGarbage(ReplaceGarbage):

    def __init__(self, languages: List[str] = SUPPORTED_LANGUAGES):
        super().__init__(replace_with='', languages=languages)


class TraditionalToSimplified(CleaningFunction):

    def __init__(self):
        super().__init__()
        self.t2s = OpenCC('t2s')

    def clean(self, text: str, **kwargs) -> str:
        return self.t2s.convert(text)


class SingleNewlineToSpace(CleaningFunction):

    def __init__(self):
        super().__init__(replacement=' ')
        self.regex = r'[^\n]+(?P<target>\n)[^\n]'

    def clean_text(self, text: str, **kwargs) -> str:
        return self.replace_all(self.regex, text, self.replacement)









class ReplaceNumbers(CleaningFunction):

    def __init__(self,
                 digit_threshold: int = 2,
                 split_replacement: bool = True,
                 only_numbers: bool = True,
                 replacement: str = chars.NUM):
        """Create a new ReplaceNumbers.
# TODO: I think this needs to simplify and split into other functions...
        Args:
            digit_threshold: Int. Numbers with less than this number of digits
                are unaffected.
            split_replacement: Bool. If True, when handling tokens, if the
                token ends up as, e.g. `NUM月`, then this will split the results
                into two tokens, `NUM` and `月`. Default is True.
            only_numbers: Bool. If True, will only replace tokens that are
               independent numbers. I.e. `12月` or `1st` would not be replaced.
               If False, then could potentially replace, e.g., `COVID19` (if
               `digit_threshold` <= 2). Default is True.
            replacement: Str. The string to replace numbers with. Defaults to
               `text_cleaning.chars.NUM`.
        """
        super().__init__(replacement)
        self.digit_threshold = digit_threshold
        self.split_replacement = split_replacement
        self.only_numbers = only_numbers

    def clean_text(self, text: str, **kwargs) -> str:
        regex = r'%s[%s]{%s,}%s' \
                % ('^' if self.only_numbers else '',
                   chars.digits,
                   self.digit_threshold,
                   '$' if self.only_numbers else '')
        text = re.sub(regex, self.replacement, text)
        return text

    def clean_tokens(self, tokens: List[str], **kwargs) -> List[str]:
        # trick here is to make sure NUM is separated from things like 年 and 日
        tokens_out = []
        for t in tokens:
            t = self.clean_text(t)
            if self.split_replacement \
                    and self.replacement in t \
                    and len(t) > len(self.replacement):
                # case where NUM is at the start
                if t[0:len(NUM)] == NUM:
                    tokens_out.append(NUM)
                    tokens_out.append(t.replace(NUM, ''))
                # case where NUM is in the middle
                elif t[-len(NUM):] != NUM:
                    tokens_out.append(t[0:t.index(NUM)])
                    tokens_out.append(NUM)
                    tokens_out.append(t[t.index(NUM) + len(NUM):])
                # case where NUM is at the end
                else:
                    tokens_out.append(t.replace(NUM, ''))
                    tokens_out.append(NUM)
            else:
                if t != '':
                    tokens_out.append(t)
        return tokens_out


class RemoveNumbers(ReplaceNumbers):

    def __init__(self):
        super().__init__(replacement='')









