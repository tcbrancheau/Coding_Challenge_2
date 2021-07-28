from io import StringIO

class LongWordFinder:
    """
    This class is able to read in words from a file and determine the largest
    word(s).
    """
    def __init__(self):
        self.long_word_list = []

    def read_file(self, input_file_name):
        """
        This method reads in a file, finding the largest words in the file and
        storing them in an array.

        :param input_file_name: file of words to read
        :type input_file_name: str
        :return: list of words that are the longest (if there is only one, it
            will be a list with one element)
        :rtype: list of str
        """
        self.long_word_list = []

        # For testing purposes, this uses StringIO as the input
        # instead of a file
        if type(input_file_name) is StringIO:
            input_file = input_file_name
        elif type(input_file_name) is str:
            input_file = open(input_file_name, 'r')
        else:
            print("Incorrect type of parameter passed into read_file.")

        for line in input_file:
            # create list of words from each line of file
            line_words = line.split()

            # loop through words in word list and compare with current long
            # word list
            for current_word in line_words:
                if len(self.long_word_list) == 0:
                    # word list has nothing in it, so add word
                    self.long_word_list.append(current_word)
                elif current_word not in self.long_word_list:
                    # long word list is not empty and word is not in it, so
                    # test to see if it is the new longest word or if it ties
                    # with the existing long words
                    for long_word in self.long_word_list:
                        if len(current_word) > len(long_word):
                            self.long_word_list.clear()
                            self.long_word_list.append(current_word)
                        elif len(current_word) == len(long_word):
                            self.long_word_list.append(current_word)
                            break  # to avoid infinite loop

    def print_long_words(self):
        """
        Method to print the longest word(s) found in the data file.
        """
        if len(self.long_word_list) > 1:
            print("The longest words detected are:\n")
        elif len(self.long_word_list) == 1:
            print("The longest word detected is:\n")
        else:
            print("No data.")
        for long_word in self.long_word_list:
            print(long_word)






