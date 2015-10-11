import tokenize
from markov_2 import Markov_Chain


if __name__ == "__main__":
    words_list = tokenize.tokenize("cleaned_corpus.txt")
    markov_chain = Markov_Chain()
    markov_chain.build_chain(words_list)
    string = markov_chain.random_walk(50)
    print(string)
