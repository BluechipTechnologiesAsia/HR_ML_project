from extract_keypoints import cleanup_sentence, cleanup_bulletpoints,\
        calculate_score_clubs, advanced_search_clubs
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


class TestAdvancedSearch(unittest.TestCase):
    """
    """
    def test_keywords(self):
        """check if any keyword is present in the
        given string
        """
        pass

    def test_scoring_clubs(self):
        """check if the scoring mechanism is evaluated
        properly
        """
        test_string_1 = """I went to AIESEC"""
        test_string_2 = """I went to Rotract"""
        test_string_3 = """I go to school"""
        test_string_4 = """LEO is my home"""
        test_string_5 = """I was president of LEO club and IEASL"""

        # getting the scores using the function
        score_1 = calculate_score_clubs(test_string_1)
        score_2 = calculate_score_clubs(test_string_2)
        score_3 = calculate_score_clubs(test_string_3)
        score_4 = calculate_score_clubs(test_string_4)
        score_5 = calculate_score_clubs(test_string_5)

        # if name is AIESEC score is 1.5
        self.assertEqual(score_1, 1.5)
        # if name is Rotract score is 1.5
        self.assertEqual(score_2, 1.5)
        self.assertEqual(score_3, 0)
        self.assertEqual(score_4, 1.0)
        self.assertEqual(score_5, 1.5)


if __name__ == "__main__":
    unittest.main()
