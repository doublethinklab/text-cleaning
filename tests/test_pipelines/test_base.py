import unittest

from text_cleaning.functions.text import StandardizeText
from text_cleaning.pipelines.twitter import TwitterEnglishTextCleaningPipeline


class TestPipelineBase(unittest.TestCase):

    def test_get_function(self):
        # use an implementation
        pipeline = TwitterEnglishTextCleaningPipeline(debug=False)

        # get a function and set debug
        fn = pipeline.get_function(StandardizeText)
        fn.debug = True

        # get it again and check debug was set
        fn = pipeline.get_function(StandardizeText)
        self.assertTrue(fn.debug)
