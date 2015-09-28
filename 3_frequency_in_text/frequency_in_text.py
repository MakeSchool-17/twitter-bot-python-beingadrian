import re
from collections import defaultdict

book_path = "robinson_crusoe_text.txt"
book_file = open(book_path).read()


def histogram(source_text):
    hist = defaultdict(int)
    words = source_text.split()
    # defaultdict to the rescue
    for word in words:
        hist[word] += 1
    return hist


def unique_words(histogram):
    total_count = sum(histogram.values())
    return total_count


def frequency(word, histogram):
    return histogram[word]


def write_to_file(histogram):
    # write_to_file
    text_file = open("histogram.txt", 'w+')
    # text_file.write(str(histogram))
    for key in histogram:
        word = key.lower()
        processed = re.sub(r'[\W]+', "", word)
        text_file.write("{} {} \n".format(processed, histogram[key]))


if __name__ == "__main__":
    hist = histogram(book_file)
    # total_word_count = unique_words(hist)
    # frequency("gave", hist)
    # gave_word_frequency = frequency("to", hist)
    # print(gave_word_frequency)
    write_to_file(hist)
