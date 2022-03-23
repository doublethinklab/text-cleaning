import unittest

from text_cleaning.functions.text import LowerCase, StandardizeText
from text_cleaning.pipelines.twitter.en import \
    CleanEnglishTwitterText


class TestPipelineBase(unittest.TestCase):

    def test_get_function(self):
        # use an implementation
        pipeline = CleanEnglishTwitterText(debug=False)

        # get a function and set debug
        fn = pipeline.get_function(StandardizeText)
        fn.debug = True

        # get it again and check debug was set
        fn = pipeline.get_function(StandardizeText)
        self.assertTrue(fn.debug)

    def test_remove_function(self):
        # use an implementation
        pipeline = CleanEnglishTwitterText(debug=False)

        # remove one we know is in there
        pipeline.remove(LowerCase)

        # confirm it's no longer in the functions list
        self.assertNotIn(LowerCase, [type(x) for x in pipeline.functions])

    def test_includes(self):
        # use an implementation
        pipeline = CleanEnglishTwitterText(debug=False)

        # one we know is in there should be detected
        self.assertTrue(pipeline.includes(LowerCase))

        # but after removal, should be false
        pipeline.remove(LowerCase)
        self.assertFalse(pipeline.includes(LowerCase))
