import urllib.request
from collections import defaultdict


book_file = urllib.request.urlopen("https://www.gutenberg.org/files/521/521-0.txt").read().decode("utf-8")


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


if __name__ == "__main__":
    hist = histogram(book_file)
    total_word_count = unique_words(hist)
    frequency("gave", hist)
    gave_word_frequency = frequency("to", hist)
    print(gave_word_frequency)
