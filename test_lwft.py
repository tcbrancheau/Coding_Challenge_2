from contextlib import redirect_stdout
from long_word_finder import LongWordFinder
import io
import unittest


class LWFTest(unittest.TestCase):

    def setUp(self) -> None:
        self.lwf = LongWordFinder()

    # Positive Tests
    def test_read_file_one_long_word(self):
        """
        This test method ensures LongWordFinder.read_file can read data from a
        file and find one long word when there is only one longest word.
        """
        test_input = io.StringIO()
        test_input.write('First\n')
        test_input.write('Second\n')
        test_input.write('Third\n')
        test_input.seek(0)  # reset stream position back to beginning

        self.lwf.read_file(test_input)

        self.assertEqual(
            len(self.lwf.long_word_list), 1, "Found too many long words."
        )

        self.assertEqual(
            self.lwf.long_word_list[0],
            "Second",
            "Did not find correct long word"
        )

    def test_read_file_three_long_words(self):
        """
        This test method ensures LongWordFinder.read_file can read data from a
        file and find the three long words in the input.
        """
        test_input = io.StringIO()
        test_input.write('First\n')
        test_input.write('Second\n')
        test_input.write('Third\n')
        test_input.write('grape\n')
        test_input.write('kiwi\n')
        test_input.write('orange\n')
        test_input.write('ruleRs\n')
        test_input.write('paper\n')
        test_input.write('pens\n')

        test_input.seek(0)  # reset stream position back to beginning

        self.lwf.read_file(test_input)

        self.assertEqual(
            len(self.lwf.long_word_list),
            3,
            "Did not find correct number of long words."
        )

        self.assertIn("Second", self.lwf.long_word_list, "Did not find correct long word 'Second'.")
        self.assertIn("orange", self.lwf.long_word_list, "Did not find correct long word 'Second'.")
        self.assertIn("ruleRs", self.lwf.long_word_list, "Did not find correct long word 'Second'.")


    def test_print_long_words_one_long_word(self):
        """
        This test method ensures LongWordFinder.read_file can read data from a
        file, find one long word when there is only one longest word, and print
        that word to stdout. This test also makes sure the other words from the
        input do not appear in the output.
        """
        test_input = io.StringIO()
        test_input.write('Fourth\n')
        test_input.write('Fifth\n')
        test_input.write('Sixth\n')
        test_input.seek(0)
        self.lwf.read_file(test_input)

        output_stream = io.StringIO()
        with output_stream as f:
            with redirect_stdout(f):
                self.lwf.print_long_words()

            output_stream.seek(0)
            stream_contents = output_stream.read()

            # test for expected word
            self.assertIn(
                "Fourth",
                stream_contents,
                "Did not find correct word in output. Looking for 'Fourth'"
            )

            # test for not expected words
            self.assertNotIn(
                "Fifth",
                stream_contents,
                "Found incorrect word in output ('Fifth')."
            )
            self.assertNotIn(
                "Sixth",
                stream_contents,
                "Found incorrect word in output ('Sixth')."
            )

    def test_print_long_words_three_long_words(self):
        """
        This test method ensures LongWordFinder.read_file can read data from a
        file, find the three long words it contains, and print those words to
        stdout. This test also makes sure the other words from the input do not
        appear in the output.
        """
        test_input = io.StringIO()
        test_input.write('Fourth\n')
        test_input.write('Fifth\n')
        test_input.write('Sixth\n')
        test_input.write('Ohio\n')
        test_input.write('Hawaii\n')
        test_input.write('Texas\n')
        test_input.write('Honda\n')
        test_input.write('Fiat\n')
        test_input.write('Toyota\n')
        test_input.seek(0)
        self.lwf.read_file(test_input)

        output_stream = io.StringIO()
        with output_stream as f:
            with redirect_stdout(f):
                self.lwf.print_long_words()

            output_stream.seek(0)
            stream_contents = output_stream.read()

            # test for expected words
            expected_words = ["Fourth", "Hawaii", "Toyota"]
            for exp_word in expected_words:
                self.assertIn(
                    exp_word,
                    stream_contents,
                    "Did not find correct word in output."
                    "Looking for '{0}'".format(exp_word)
                )

            # test for unexpected words
            unexpected_words = ['Fifth', 'Sixth', 'Ohio', 'Texas', 'Honda', 'Fiat']
            for unexp_word in unexpected_words:
                self.assertNotIn(
                    unexp_word,
                    stream_contents,
                    "Found incorrect word in output ('{0}').".format(unexp_word)
                )

    # Negative Tests
    def test_read_file_print_long_words_no_words(self):
        """
        This test method ensures LongWordFinder.read_file is working.
        """
        test_input = io.StringIO()
        test_input.write('\n')
        test_input.write('\n')
        test_input.write('\n')
        test_input.seek(0)  # reset stream position back to beginning

        # test read_file
        self.lwf.read_file(test_input)

        self.assertEqual(
            len(self.lwf.long_word_list),
            0,
            "Found too many long words. Input only had whitespace."
        )

        # test print_long_words
        output_stream = io.StringIO()
        with output_stream as f:
            with redirect_stdout(f):
                self.lwf.print_long_words()

            output_stream.seek(0)
            stream_contents = output_stream.read()

            self.assertIn(
                "No data.",
                stream_contents,
                "Did not receive expected message of 'No data.'."
            )

    def test_read_file_print_long_words_no_data(self):
        """
        This test method ensures LongWordFinder.read_file is working.
        """
        test_input = io.StringIO()

        self.lwf.read_file(test_input)

        self.assertEqual(
            len(self.lwf.long_word_list),
            0,
            "Found too many long words. Input only had whitespace."
        )

        # test print_long_words
        output_stream = io.StringIO()
        with output_stream as f:
            with redirect_stdout(f):
                self.lwf.print_long_words()

            output_stream.seek(0)
            stream_contents = output_stream.read()

            self.assertIn(
                "No data.",
                stream_contents,
                "Did not receive expected message of 'No data.'."
            )

