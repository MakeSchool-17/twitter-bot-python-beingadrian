import sys
import re


def convert_to_words_list(file_name):
    file_read = open(file_name, 'r').read()
    file_stripped = re.sub(r'[\W]+', " ", file_read)
    words_list = file_stripped.lower().split()
    return words_list
