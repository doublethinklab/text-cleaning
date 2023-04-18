from text_cleaning import languages as lang, replacements as repl
from text_cleaning.functions import text as text_fx
from text_cleaning.functions import tokens as tokens_fx
from text_cleaning.pipelines.base import \
    TextCleaningPipeline, TokensCleaningPipeline


class CleanChineseWeiboText(TextCleaningPipeline):

    def __init__(
            self,
            logger=None,
            debug: bool = False
    ):
        super().__init__(
            functions=[
                text_fx.RemoveHtml(),
                text_fx.NormalizeWhitespace(),
                text_fx.ReplaceUrls(),
                text_fx.RemoveGarbage(languages=[lang.zh]),
                text_fx.StandardizeText(),
                text_fx.LowerCase(),
            ],
            logger=logger,
            debug=debug)


class CleanChineseWeiboTokens(TokensCleaningPipeline):

    def __init__(
            self,
            numbers_replacement: str = repl.NUMBER,
            numbers_replacement_digit_threshold: int = 2,
            numbers_split_replacement: bool = False,
            split_only_numbers: bool = True,
            too_many_numbers_ratio_threshold: float = 0.5,
            too_many_numbers_length_threshold: int = 3,
            logger=None,
            debug: bool = False
    ):
        super().__init__(
            functions=[
                tokens_fx.RemovePunctuation(
                    exclude_hashtags=True,
                    exclude_mentions=True),
                tokens_fx.ReplaceNumbers(
                    replacement=numbers_replacement,
                    digit_threshold=numbers_replacement_digit_threshold,
                    split_replacement=numbers_split_replacement,
                    only_numbers=split_only_numbers),
                tokens_fx.ReplaceTooManyNumbers(
                    replacement=numbers_replacement,
                    ratio_threshold=too_many_numbers_ratio_threshold,
                    length_threshold=too_many_numbers_length_threshold),
                tokens_fx.NormalizeHashtags(),
            ],
            logger=logger,
            debug=debug)
