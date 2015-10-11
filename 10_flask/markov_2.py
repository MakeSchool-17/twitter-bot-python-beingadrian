import random


class Markov_Chain(object):

    # storage stores "word": {"word": frequency}
    table = {}

    def choose_random_key(self, dictionary):
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
        prev_key = None
        for i in range(word_count):
            if prev_key is not None:
                next_key = self.choose_random_key(self.table[prev_key])
                # print("===> Prev_key: {}".format(prev_key))
                # print("===> Next_key: {}".format(next_key))
                if next_key is None:
                    return string
                split_key = next_key.split()
                string += split_key[1] + " "
                prev_key = next_key
            else:
                keys = list(self.table)
                random_key = random.choice(keys)
                string += random_key + " "
                prev_key = random_key
        return string.capitalize()

    def build_chain(self, list_of_words):
        for word in list_of_words:
            self.table[word] = {}
        prev_word = None
        prev_prev_word = None
        for word in list_of_words:
            if prev_word and prev_prev_word is None:
                prev_word = word
            elif prev_prev_word is None and prev_word is not None:
                prev_prev_word = prev_word
                prev_word = word
            elif prev_word and prev_prev_word is not None:
                try:
                    key = prev_prev_word + " " + prev_word
                    self.table[key][word] += 1
                except:
                    key = prev_prev_word + " " + prev_word
                    new_key = prev_word + " " + word
                    self.table[key] = {new_key: 1}
            try:
                prev_prev_word = prev_word
                prev_word = word
            except:
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
