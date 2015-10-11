import random


class Markov_Chain(object):

    # storage stores "word": {"word": frequency}
    table = {}

    def choose_random_word(self, dictionary):
        # choose word based on probility weight
        random_int = random.uniform(0, 1)
        total_word_count = sum(dictionary.values())
        cumulative_prob = 0.0
        if len(dictionary) == 0:
            return None
        for key, val in dictionary.items():
            cumulative_prob += (val / total_word_count)
            if random_int < cumulative_prob:
                break
        return key

    def random_walk(self, word_count):
        string = ""
        prev_word = None
        for i in range(word_count):
            if prev_word is not None:
                words = list(self.table)
                next_word = self.choose_random_word(self.table[prev_word])
                if next_word is None:
                    return string
                string += next_word + " "
                prev_word = next_word
            else:
                words = list(self.table)
                random_word = random.choice(words)
                string += random_word + " "
                prev_word = random_word
        return string

    def build_chain(self, list_of_words):
        for word in list_of_words:

            self.table[word] = {}
        prev_word = None
        for word in list_of_words:
            if prev_word is not None:
                try:
                    self.table[prev_word][word] += 1
                except:
                    self.table[prev_word][word] = 1
            prev_word = word

if __name__ == "__main__":
    markov_chain = Markov_Chain()
    sample_list = [
        "A", "man,", "a", "plan,", "a",
        "canal:", "Panama!", "A", "dog,",
        "a", "panic", "in", "a", "pagoda!"
    ]
    markov_chain.build_chain(sample_list)
    string = markov_chain.random_walk(8)
    print(string)
