import random

quotes = ("What is thy bidding, my master?", "May the Force be with you.")


def random_quote():
    random_index = random.randint(0, len(quotes) - 1)
    return quotes[random_index]

if __name__ == '__main__':
    quote = random_quote()
    print(quote)
