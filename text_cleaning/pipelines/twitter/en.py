from typing import List

from text_cleaning import languages as lang, replacements as repl
from text_cleaning.functions import text as text_fx
from text_cleaning.functions import tokens as tokens_fx
from text_cleaning.pipelines.base import \
    TextCleaningPipeline, TokensCleaningPipeline


class CleanEnglishTwitterText(TextCleaningPipeline):

    def __init__(
            self,
            mentions_replacement: str = repl.MENTION,
            logger=None,
            debug: bool = False
    ):
        super().__init__(
            functions=[
                text_fx.NormalizeWhitespace(),
                text_fx.SingleNewlineToPeriod(language=lang.en),
                text_fx.RemoveTrailingApostropheS(),
                text_fx.RemoveGarbage(languages=[lang.en]),
                text_fx.ReplaceMentions(replacement=mentions_replacement),
                text_fx.StandardizeText(),
                text_fx.LowerCase(),
            ],
            logger=logger,
            debug=debug)


class CleanEnglishTwitterTokens(TokensCleaningPipeline):

    def __init__(
            self,
            min_token_length: int = 2,
            numbers_replacement: str = repl.NUMBER,
            numbers_replacement_digit_threshold: int = 2,
            numbers_split_replacement: bool = False,
            split_only_numbers: bool = True,
            too_many_numbers_ratio_threshold: float = 0.5,
            too_many_numbers_length_threshold: int = 3,
            short_token_exceptions: List[str] = ['i', 'a'],
            logger=None,
            debug: bool = False):
        super().__init__(
            functions=[
                tokens_fx.RemoveUrls(),
                tokens_fx.ReplaceEitherSlashWithSpace(),
                tokens_fx.ReplaceHyphenCompoundWithSpace(),
                tokens_fx.RemovePunctuation(),
                tokens_fx.ReplaceNumbers(
                    replacement=numbers_replacement,
                    digit_threshold=numbers_replacement_digit_threshold,
                    split_replacement=numbers_split_replacement,
                    only_numbers=split_only_numbers),
                tokens_fx.ReplaceTooManyNumbers(
                    replacement=numbers_replacement,
                    ratio_threshold=too_many_numbers_ratio_threshold,
                    length_threshold=too_many_numbers_length_threshold),
                tokens_fx.RemoveTooShortTokens(
                    min_length=min_token_length,
                    exceptions=short_token_exceptions),
            ],
            logger=logger,
            debug=debug)
