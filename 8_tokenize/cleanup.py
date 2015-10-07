import re
import sys


def clean_text(file_dir):
    read_file = open(file_dir, 'r')
    text = read_file.read()
    read_file.close()
    # remove unecessary characters
    patterns = [
        r'[\[].*?[\]]',
        r'["!*()]',
        r'[\n]',
        r'\s-\s',
        # r'\w+.(.)+'
        # r'\w(-)'
    ]
    for pattern in patterns:
        text = re.sub(pattern, "", text)
    cleaned_file = open('cleaned_corpus.txt', 'w')
    cleaned_file.write(text)
    cleaned_file.close()


if __name__ == "__main__":
    usr_input = sys.argv[1]
    clean_text(usr_input)
