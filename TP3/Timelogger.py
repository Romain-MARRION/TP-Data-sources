import time
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt


def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return end_time - start_time
    return wrapper


@execution_time
def count_words_dict(filename):
    data = open(filename).read()
    corpus = data.lower().replace('\n', ' ').split(" ")
    word_counts = {}
    for word in corpus:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


@execution_time
def count_words_counter(filename):
    data = open(filename).read()
    return Counter(data.split())


if __name__ == "__main__":
    filename = 't8.shakespeare.txt'
    time_dict_method = []
    time_counter_method = []
    for i in range(100):
        time_dict_method.append( count_words_dict(filename))
        time_counter_method.append(count_words_counter(filename))
    time_dict_method = np.array(time_dict_method)
    time_counter_method = np.array(time_counter_method)
    print('dict method')
    print(f'mean: {time_dict_method.mean()} | std: {time_dict_method.std()} \n')
    print('counter method')
    print(f'mean: {time_counter_method.mean()} | std: {time_counter_method.std()} \n')
    fig, ax = plt.subplots()
    plt.plot(range(100), time_dict_method, label='dict_method')
    plt.plot(range(100), time_counter_method, label='counter_method')

