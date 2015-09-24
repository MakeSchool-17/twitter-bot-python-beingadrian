def reverse_word(word):
    word_reversed = word[::-1]
    return word_reversed


if __name__ == "__main__":
    word = "Greetings"
    reversed_word = reverse_word(word)
    print(reversed_word)
