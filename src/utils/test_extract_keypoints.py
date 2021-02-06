from extract_keypoints import cleanup_sentence, cleanup_bulletpoints
import unittest


class TestCleanUp(unittest.TestCase):
    """
    Test cases for clean up functions in
    the extract_keypoints script
    """
    def test_stopwords(self):
        """check if the stop words are configured
        properly
        """
        test_string_1 = """why through down it"""
        test_string_2 = """herself the which me"""
        test_string_3 = """hello world"""

        filter_sentence_1 = cleanup_sentence(test_string_1)
        filter_sentence_2 = cleanup_sentence(test_string_2)
        filter_sentence_3 = cleanup_sentence(test_string_3)

        self.assertEqual(filter_sentence_1, "")
        self.assertEqual(filter_sentence_2, "")
        self.assertEqual(filter_sentence_3, "hello world")

    def test_bulletpoints(self):
        """check if any non alphanumeric characters are removed
        """
        test_string_1 = """hey! how are you doing"""
        test_string_2 = """!?@#$!$%^&%#$#$%$$%$^%&*!"""
        test_string_3 = """$$$$@@#!@$%$@^$#&*()())___"""

        filter_sentence_1 = cleanup_bulletpoints(test_string_1)
        filter_sentence_2 = cleanup_bulletpoints(test_string_2)
        filter_sentence_3 = cleanup_bulletpoints(test_string_3)

        self.assertNotEqual(filter_sentence_1, " ")
        self.assertEqual(filter_sentence_1, "hey how are you doing")
        self.assertEqual(filter_sentence_2, " ")
        self.assertEqual(filter_sentence_3, " ")


class TestNormalSearch(unittest.TestCase):
    """
    """
    def test_keywords(self):
        """check if any keyword is present in the
        given string
        """
        test_string_1 = """I went to AISEc"""

    def test_scoring(self):
        """check if the scoring mechanism is evaluated
        properly
        """


class TestAdvancedSearch(unittest.TestCase):
    """
    """
    def test_keywords(self):
        """check if any keyword is present in the
        given string
        """
        test_string_1 = """I went to AISEc"""

    def test_scoring(self):
        """check if the scoring mechanism is evaluated
        properly
        """


if __name__ == "__main__":
    unittest.main()
