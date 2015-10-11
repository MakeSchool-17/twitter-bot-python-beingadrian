import sys
from hash_table import HashTable
from binary_heap_max import Binary_Heap_Max


def tokenize(text_file_dir):
    text_file = open(text_file_dir, 'r')
    text = text_file.read()
    text_file.close()
    tokenized_array = text.split(" ")
    return tokenized_array


def count_tokens(tokenized_array):
    histogram = HashTable()
    for word in tokenized_array:
        searched_word_data = histogram.search(word)
        if searched_word_data is not None:
            histogram.set_value(word, searched_word_data[1] + 1)
        else:
            histogram.set_value(word, 1)
    return histogram


def count_tokens_second(tokenized_array):
    histogram = HashTable()


def convert_to_heap(histogram):
    heap = Binary_Heap_Max()
    items_list = []
    for item in histogram.items():
        items_list.append((item[1], item[0]))
    heap.build_heap(items_list)
    return heap


if __name__ == "__main__":
    user_input = sys.argv[1]
    tokenized_array = tokenize(user_input)
    histogram = count_tokens(tokenized_array)
    heap = convert_to_heap(histogram)
    print(heap.delete_max())
    print(heap.delete_max())
    print(heap.delete_max())
    print(heap.delete_max())
    print(heap.delete_max())
    print(heap.delete_max())
