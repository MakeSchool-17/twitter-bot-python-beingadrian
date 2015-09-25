import random
import os

dict_file = open("/usr/share/dict/words", "r").readlines()


def generate_random_word():
    random_word = random.choice(dict_file).rstrip("\n")
    return random_word


def print_with_style(word):
    print("="*len(word))
    print(word.upper())
    print("="*len(word))


if __name__ == "__main__":
    while True:
        random_word = generate_random_word()
        os.system('cls' if os.name == 'nt' else 'clear')
        print_with_style(random_word)
        user_input = input()
        if user_input == "q":
            break
        elif user_input == "s":
            # todo: show
            pass
        else:
            # next
            pass
