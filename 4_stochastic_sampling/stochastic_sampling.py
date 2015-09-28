import random
import sys


def convert_file_to_dict(file_name):
    file_name = open(file_name, 'r').readlines()
    dictionary = {}
    for line in file_name:
        key = ""
        val = 0
        prev = ""
        for letter in line:
            try:
                try:
                    current_int = int(letter)
                    prev_int = int(prev)
                    val = int(prev + letter)
                except:
                    val = int(letter)
            except:
                key += letter
            prev = letter
        stripped_key = key.strip(" \n")
        dictionary[stripped_key] = val
    return dictionary


def random_word(hist_dictionary):
    keys_list = list(hist_dictionary.keys())
    word = random.choice(keys_list)
    return word


# inefficient way
def random_weighted_word(hist_dictionary):
    vir_list = []
    for key, value in hist_dictionary.items():
        for i in range(0, value):
            vir_list.append(key)
    word = random.choice(vir_list)
    return word


# more efficient way
def choose_random_word(hist_dictionary):
    # total number of words
    random_int = random.uniform(0, 1)
    total_word_count = sum(hist_dictionary.values())
    cumulative_prob = 0.0
    for key, val in hist_dictionary.items():
        cumulative_prob += (val / total_word_count)
        if random_int < cumulative_prob:
            break
    return key


# frequency counter to check distribution
def count_frequency(total_trials, ori_dictionary):
    counter_dict = {}
    for key in ori_dictionary.keys():
        counter_dict[key] = 0
    for i in range(0, total_trials):
        word = choose_random_word(ori_dictionary)
        counter_dict[word] += 1
    return counter_dict

if __name__ == "__main__":
    user_input = sys.argv[1]
    try:
        hist_dictionary = convert_file_to_dict(user_input)
        # random_word = random_word(hist_dictionary)
        # print(random_word)
        # weighted_word = random_weighted_word(hist_dictionary)
        # print(weighted_word)
        # result = count_frequency(10000, hist_dictionary)
        # print(result)
        word = choose_random_word(hist_dictionary)
        print(word)
    except:
        print("No such file or directory.")
