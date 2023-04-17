from typing import Tuple

from text_cleaning import errors, genres, languages
from text_cleaning.pipelines.facebook \
    import zh as facebook_zh
from text_cleaning.pipelines.generic \
    import zh as generic_zh
from text_cleaning.pipelines.news_media \
    import zh as news_media_zh
from text_cleaning.pipelines.twitter \
    import en as twitter_en, zh as twitter_zh
from text_cleaning.pipelines.weibo \
    import zh as weibo_zh


def get_pipelines(
        language: str,
        genre: str
) -> Tuple[TextCleaningPipeline, TokensCleaningPipeline]:
    if language not in languages.supported_languages:
        raise errors.UnsupportedLanguage(language)
    if genre not in genres.supported_genres:
        raise errors.UnsupportedGenre(genre)

    if language == languages.zh:
        if genre == genres.facebook:
            clean_text = facebook_zh.CleanChineseFacebookText()
            clean_tokens = facebook_zh.CleanChineseFacebookTokens()
        elif genre == genres.generic:
            clean_text = generic_zh.CleanGenericChineseText()
            clean_tokens = generic_zh.CleanGenericChineseTokens()
        elif genre == genres.news_media:
            clean_text = news_media_zh.CleanChineseNewsMediaText()
            clean_tokens = news_media_zh.CleanChineseNewsMediaTokens()
        elif genre == genres.twitter:
            clean_text = twitter_zh.CleanChineseTwitterText()
            clean_tokens = twitter_zh.CleanChineseTwitterTokens()
        elif genre == genres.weibo:
            clean_text = weibo_zh.CleanChineseWeiboText()
            clean_tokens = weibo_zh.CleanChineseWeiboTokens()
        else:
            raise ValueError(genre)
    elif language == languages.en:
        if genre == genres.facebook:
            raise NotImplementedError
        elif genre == genres.generic:
            raise NotImplementedError
        elif genre == genres.news_media:
            raise NotImplementedError
        elif genre == genres.twitter:
            clean_text = twitter_en.CleanEnglishTwitterText()
            clean_tokens = twitter_en.CleanEnglishTwitterTokens()
        elif genre == genres.weibo:
            raise ValueError('No such thing as English Weibo.')
        else:
            raise ValueError(genre)
    else:
        raise ValueError(language)

    return clean_text, clean_tokens
