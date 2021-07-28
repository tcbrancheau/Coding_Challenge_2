from long_word_finder import LongWordFinder


class WordFinderReverser(LongWordFinder):
    """
    Subclass of LongWordFinder that adds the ability to reverse
    words from the long_word_list and print out both the original
    word and its reverse.
    """

    def print_words_reverses(self):
        """
        Method to print longest word(s) and their(its) reverse.
        """
        if len(self.long_word_list) > 1:
            print("The longest words detected (and their reverses) are:\n")
        elif len(self.long_word_list) == 1:
            print("The longest word detected (and its reverse) is:\n")
        else:
            print("No data.")

        for long_word in self.long_word_list:
            reverse_word = self.reverse_word(long_word)

            print("{0} ... {1}".format(long_word, reverse_word))

    def reverse_word(self, original_word):
        """
        Takes in a string and reverses the order of the characters in it.
        :param original_word: string to be reversed
        :type original_word: str
        :return: reversed version of original string
        :rtype: str
        """
        if type(original_word) is not str:
            print(
                "Cannot reverse {0} as it is not a string.".format(original_word),
                "It is a {0}.".format(type(original_word))
            )
            return
        word_reversed = ""
        cur_index = len(original_word) - 1
        while cur_index >= 0:
            word_reversed += original_word[cur_index]
            cur_index -= 1
        return word_reversed
