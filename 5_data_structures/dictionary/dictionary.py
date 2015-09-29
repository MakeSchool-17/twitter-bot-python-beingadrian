import sys
sys.path.append('../')

import converter

words_list = converter.convert_to_words_list("../robinson_crusoe_text.txt")


def histogram(words_list):
    histogram = {}
    for word in words_list:
        try:
            histogram[word] += 1
        except:
            histogram[word] = 0
    return histogram


def frequency(word, histogram):
    try:
        return histogram[word]
    except:
        print("Word does not exist")


if __name__ == "__main__":
    histogram = histogram(words_list)
    # print(histogram)
    to_frequency = frequency("to", histogram)
    print(to_frequency)
