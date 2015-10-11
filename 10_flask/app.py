from flask import Flask
from markov_2 import Markov_Chain
import tokenize

app = Flask(__name__)


@app.route('/')
def display_text():
    tokenized = tokenize.tokenize("cleaned_corpus.txt")
    markov = Markov_Chain()
    markov.build_chain(tokenized)
    text = markov.random_walk(100)
    return text

if __name__ == '__main__':
    app.run()
