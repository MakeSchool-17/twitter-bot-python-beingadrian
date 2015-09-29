import sys
sys.path.append('../')

import converter

words_list = converter.convert_to_words_list("../robinson_crusoe_text.txt")


# def histogram2(list_of_words):
#     tuple_list = []
#     for word in list_of_words:
#         tuple_list.append((word, 0))
#     for word in tuple_list:
#         for item in tuple_list:
#             if item[0] == word:
#                 new_count = item[1] + 1
#                 tuple_list.append((word, new_count))
#                 tuple_list.pop(item.index())
#     print(tuple_list)
#

def find(item, histogram):
    for index, pair in enumerate(histogram):
        if pair[0] == item:
            return index
    return None


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


if __name__ == "__main__":
    print(histogram(words_list))
