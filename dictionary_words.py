import random


the_file = open("/usr/share/dict/words", "r").readlines()

total_lines = sum(1 for line in the_file)


def generate_sentence(number_of_words):
    words_in_sentence = []
    for i in range(0, number_of_words):
        random_int = random.randint(0, total_lines)
        word = the_file[random_int].rstrip('\n')
        words_in_sentence.append(word)
    sentence = " ".join(words_in_sentence)
    return sentence


if __name__ == "__main__":
    the_sentence = generate_sentence(3)
    print(the_sentence)
