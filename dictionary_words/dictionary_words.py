import random
import sys
import cProfile


the_file = open("/usr/share/dict/words", "r").readlines()


def generate_sentence(number_of_words):
    words_in_sentence = []
    for i in range(0, number_of_words):
        word = random.choice(the_file).rstrip("\n")
        words_in_sentence.append(word)
    sentence = " ".join(words_in_sentence)
    return sentence


if __name__ == "__main__":
    number_input = int(sys.argv[1])
    the_sentence = generate_sentence(number_input)
    print(the_sentence)
    # note: cProfile testing indicates that it is 0.00s anyways
