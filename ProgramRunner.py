import sys
from word_finder_reverser import WordFinderReverser

if __name__ == "__main__":
    if len(sys.argv) == 1:
        data_file_name = "data01.txt"
    else:
        data_file_name = sys.argv[1]

    print("Running WordFinderReverser with {0}\n".format(data_file_name))
    wfr = WordFinderReverser()

    wfr.read_file(data_file_name)

    # wfr.print_long_words()
    wfr.print_words_reverses()
