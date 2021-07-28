from contextlib import redirect_stdout
from word_finder_reverser import WordFinderReverser
import io
import unittest


class WFRTest(unittest.TestCase):

    def setUp(self) -> None:
        """

        :return:
        """
        self.wfr = WordFinderReverser()

    # Positive tests
    def test_reverse_word_short_word(self):
        """
        Tests that WordFinderReverser.reverse_word can handle short (3 letters)
        words.
        """
        rw = self.wfr.reverse_word("cab")
        self.assertEqual(
            rw,
            "bac",
            "Word 'cab' was not reversed correctly.  Received {0}".format(rw)
        )

    def test_reverse_word_medium_word(self):
        """
        Tests that WordFinderReverser.reverse_word can handle medium
        (7 letters) words.
        """
        rw = self.wfr.reverse_word("Georgia")
        self.assertEqual(
            rw,
            "aigroeG",
            "Word 'Georgia' was not reversed correctly.  Received {0}".format(rw)
        )

    def test_reverse_word_long_word(self):
        """
        Tests that WordFinderReverser.reverse_word can handle long (15 letters)
        words.
        """

        rw = self.wfr.reverse_word("prognostication")
        self.assertEqual(
            rw,
            "noitacitsongorp",
            "Word 'prognostication' was not reversed correctly.  Received {0}".format(rw)
        )

    def test_print_words_reverses_one_long_word(self):
        """

        :return:
        """
        test_input = io.StringIO()
        test_input.write('Fourth\n')
        test_input.write('Fifth\n')
        test_input.write('Sixth\n')
        test_input.seek(0)
        self.wfr.read_file(test_input)

        output_stream = io.StringIO()
        with output_stream as f:
            with redirect_stdout(f):
                self.wfr.print_words_reverses()
            output_stream.seek(0)
            stream_contents = output_stream.read()
            self.assertIn(
                "Fourth",
                stream_contents,
                "Did not find correct word in output. Looking for 'Fourth'"
            )
            self.assertIn(
                "htruoF",
                stream_contents,
                "Did not find correct reversed word in output. Looking for 'htruoF'"
            )

    def test_print_words_reverses_three_long_words(self):
        """

        :return:
        """
        test_input = io.StringIO()
        test_input.write('Fourth\n')
        test_input.write('Fifth\n')
        test_input.write('Sixth\n')
        test_input.write('Ohio\n')
        test_input.write('Hawaii\n')
        test_input.write('Texas\n')
        test_input.write('Honda\n')
        test_input.write('Chevy\n')
        test_input.write('Toyota\n')
        test_input.seek(0)
        self.wfr.read_file(test_input)

        output_stream = io.StringIO()
        with output_stream as f:
            with redirect_stdout(f):
                self.wfr.print_words_reverses()
            output_stream.seek(0)
            stream_contents = output_stream.read()
            self.assertIn(
                "Fourth",
                stream_contents,
                "Did not find correct word in output. Looking for 'Fourth'"
            )
            self.assertIn(
                "htruoF",
                stream_contents,
                "Did not find correct reversed word in output. Looking for 'htruoF'"
            )
            self.assertIn(
                "Hawaii",
                stream_contents,
                "Did not find correct word in output. Looking for 'Hawaii'"
            )
            self.assertIn(
                "iiawaH",
                stream_contents,
                "Did not find correct reversed word in output. Looking for 'iiawaH'"
            )
            self.assertIn(
                "Toyota",
                stream_contents,
                "Did not find correct word in output. Looking for 'Toyota'"
            )
            self.assertIn(
                "atoyoT",
                stream_contents,
                "Did not find correct reversed word in output. Looking for 'atoyoT'"
            )

    # Negative tests
    def test_reverse_word_int_input(self):
        """
        Tests data type checking of reverse_word() to ensure it does not accept
        int as input
        """
        expected_response = "Cannot reverse 12 as it is not a string. It is a <class 'int'>.\n"

        output_stream = io.StringIO()
        with output_stream as f:
            with redirect_stdout(f):
                rw = self.wfr.reverse_word(12)

            output_stream.seek(0)
            stream_contents = output_stream.read()

            self.assertEqual(
                expected_response,
                stream_contents,
                "Did not get correct error message."
                "\nExpected: {0}\nReceived: {1}".format(
                    expected_response, stream_contents
                )
            )

            self.assertIsNone(
                rw, "Output of reverse_word() with int input should be None"
            )

    def test_read_file_print_words_reverses_no_words(self):
        """
        This test method ensures LongWordFinder.read_file is working.
        """
        test_input = io.StringIO()
        test_input.write('\n')
        test_input.write('\n')
        test_input.write('\n')
        test_input.seek(0)  # reset stream position back to beginning

        # test read_file
        self.wfr.read_file(test_input)

        self.assertEqual(
            len(self.wfr.long_word_list),
            0,
            "Found too many long words. Input only had whitespace."
        )

        # test print_long_words
        output_stream = io.StringIO()
        with output_stream as f:
            with redirect_stdout(f):
                self.wfr.print_words_reverses()

            output_stream.seek(0)
            stream_contents = output_stream.read()

            self.assertIn(
                "No data.",
                stream_contents,
                "Did not receive expected message of 'No data.'."
            )

    def test_read_file_print_words_reverses_no_data(self):
        """
        This test method ensures LongWordFinder.read_file is working.
        """
        test_input = io.StringIO()

        self.wfr.read_file(test_input)

        self.assertEqual(
            len(self.wfr.long_word_list),
            0,
            "Found too many long words. Input only had whitespace."
        )

        # test print_long_words
        output_stream = io.StringIO()
        with output_stream as f:
            with redirect_stdout(f):
                self.wfr.print_words_reverses()

            output_stream.seek(0)
            stream_contents = output_stream.read()

            self.assertIn(
                "No data.",
                stream_contents,
                "Did not receive expected message of 'No data.'."
            )
