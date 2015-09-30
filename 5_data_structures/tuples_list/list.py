import sys
sys.path.append('../')

import converter
import timer

words_list = converter.convert_to_words_list("../robinson_crusoe_text.txt")


def find(item, histogram):
    for index, pair in enumerate(histogram):
        if pair[0] == item:
            return index
    return None


# Algorithm complexity: O(n^2)
def histogram(words):
    hist = []
    for word in words:
        index = find(word, hist)
        if index is None:
            hist.append((word, 1))
        else:
            count = hist[index][1]
            new_pair = (word, count + 1)
            hist[index] = new_pair
    return hist


def frequency(word, histogram):
    index = find(word, histogram)
    word = histogram[index][0]
    return word


if __name__ == "__main__":
    hist = histogram(words_list)
    # timer.time_function("frequency('the', hist)")  # 0.000 secs
    timer.time_function("histogram(words_list)")  # 9.175 secs
