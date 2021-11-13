from typing import Callable, Optional

from text_cleaning.functions import *


class CleaningPipeline:

    def __init__(self, functions: List[CleaningFunction]):
        self.functions = functions


class TextCleaningPipeline(CleaningPipeline):

    def __call__(self, text: str, **kwargs) -> str:
        for fn in self.functions:
            text = fn.clean_text(text, **kwargs)
        return text


class TokensCleaningPipeline(CleaningPipeline):

    def __call__(self, tokens: List[str], **kwargs):
        cleaned_tokens = []
        for token in tokens:
            for fn in self.functions:
                token = fn.clean_token(token)
                if token != '':
                    cleaned_tokens.append(token)
        return cleaned_tokens








class StandardTextCleaningPipeline(CleaningPipeline):

    def __init__(self, languages: List[str]):
        functions = [
            NormalizeWhitespace(),
            RemoveGarbage(languages=languages),
        ]
        super().__init__(functions)


class StandardTokensCleaningPipeline(CleaningPipeline):

    def __init__(self):
        functions = [
            ReplaceUrls(),
            RemovePunctuation(),
            ReplaceNumbers(),
        ]
        super().__init__(functions)


class StandardZhTokensCleaningPipeline(CleaningPipeline):

    def __init__(self):
        functions = [
            ReplaceUrls(),
            RemovePunctuation(),
            ReplaceNumbers(),
            TraditionalToSimplified(),
        ]
        super().__init__(functions)


class StandardEntityCleaningPipeline(CleaningPipeline):

    def __init__(self, normalize: Optional[Callable] = None):
        functions = [
            RemovePunctuation(),
        ]
        if normalize is not None:
            functions.append(normalize)
        super().__init__(functions)


class StandardZhEntityCleaningPipeline(CleaningPipeline):

    def __init__(self, normalize: Optional[Callable] = None):
        functions = [
            RemovePunctuation(),
            TraditionalToSimplified(),
        ]
        if normalize is not None:
            functions.append(normalize)
        super().__init__(functions)


class TweetTextCleaningPipeline(CleaningPipeline):

    def __init__(self, languages: List[str] = SUPPORTED_LANGUAGES):
        functions = [
            NormalizeWhitespace(),
            RemoveGarbage(languages=languages),
        ]
        super().__init__(functions)


class TweetTokensCleaningPipeline(CleaningPipeline):

    def __init__(self):
        functions = [
            RemoveUrls(),
            RemovePunctuation(),
            ReplaceNumbers(),
        ]
        super().__init__(functions)


class EnglishTweetTextCleaningPipeline(TweetTextCleaningPipeline):

    def __init__(self):
        super().__init__(languages=['en_US'])


class ChineseTweetTextCleaningPipeline(CleaningPipeline):

    def __init__(self):
        functions = [
            NormalizeWhitespace(),
            RemoveGarbage(languages=['zh_CN']),
            TraditionalToSimplified(),
        ]
        super().__init__(functions)


class JapaneseTweetTextCleaningPipeline(TweetTextCleaningPipeline):

    def __init__(self):
        super().__init__(languages=['ja_JP'])
