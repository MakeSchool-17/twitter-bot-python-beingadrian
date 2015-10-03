import re
import sys

def clean_text(file_dir):
    read_file = open(file_dir, 'r').read()
    # remove sentences not said by Elon
    pattern = r'[\[].*?[\]]'
    cleaned = re.sub(pattern, "", read_file)
    # create new clean file
    cleaned_file = open('cleaned_corpus.txt', 'w+')
    cleaned_file.write(cleaned)


if __name__ == "__main__":
    usr_input = sys.argv[1]
    clean_text(usr_input)
