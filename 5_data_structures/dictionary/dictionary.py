import sys
sys.path.append('../')

import converter
import timer

words_list = converter.convert_to_words_list("../robinson_crusoe_text.txt")


# algorithm complexity: 1 (some constant)
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
    # histogram = histogram(words_list)
    # timer.time_function("frequency('the', histogram)")  # 0.000 secs
    timer.time_function("histogram(words_list)")  # 0.027 secs
