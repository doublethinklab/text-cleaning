from typing import Tuple

from text_cleaning import errors, genres, languages
from text_cleaning.pipelines.facebook \
    import en as facebook_en, zh as facebook_zh
from text_cleaning.pipelines.generic \
    import en as generic_en, zh as generic_zh
from text_cleaning.pipelines.news_media \
    import en as news_media_en, zh as news_media_zh
from text_cleaning.pipelines.twitter \
    import en as twitter_en, zh as twitter_zh
from text_cleaning.pipelines.weibo \
    import zh as weibo_zh
from text_cleaning.pipelines.youtube \
    import en as youtube_en, zh as youtube_zh


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
        elif genre == genres.youtube:
            clean_text = youtube_zh.CleanChineseYouTubeText()
            clean_tokens = youtube_zh.CleanChineseYouTubeTokens()
        else:
            raise ValueError(genre)
    elif language == languages.en:
        if genre == genres.facebook:
            clean_text = facebook_en.CleanEnglishFacebookText()
            clean_tokens = facebook_en.CleanEnglishFacebookTokens()
        elif genre == genres.generic:
            clean_text = generic_en.CleanGenericEnglishText()
            clean_tokens = generic_en.CleanGenericEnglishTokens()
        elif genre == genres.news_media:
            clean_text = news_media_en.CleanEnglishNewsMediaText()
            clean_tokens = news_media_en.CleanEnglishNewsMediaTokens()
        elif genre == genres.twitter:
            clean_text = twitter_en.CleanEnglishTwitterText()
            clean_tokens = twitter_en.CleanEnglishTwitterTokens()
        elif genre == genres.weibo:
            raise ValueError('No such thing as English Weibo.')
        elif genre == genres.youtube:
            clean_text = youtube_en.CleanEnglishYouTubeText()
            clean_tokens = youtube_en.CleanEnglishYouTubeTokens()
        else:
            raise ValueError(genre)
    else:
        raise ValueError(language)

    return clean_text, clean_tokens
