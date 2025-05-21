import numpy as np
import itertools
from collections import Counter


def load_corpus(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def generate_permutations(chars, max_length):
    permuted_tokens = set()
    for length in range(1, max_length + 1):
        for p in itertools.permutations(chars, length):
            permuted_tokens.add("".join(p))
    return permuted_tokens


def count_permuted_frequencies(corpus, permuted_tokens):
    frequencies = Counter()
    for token in permuted_tokens:
        frequencies[token] += corpus.count(token)
    return frequencies


def get_top_tokens(frequencies, max_tokens):
    return frequencies.most_common(max_tokens)


def main(file_path, max_length, max_tokens):
    corpus = load_corpus(file_path)

    unique_chars = set(corpus)

    permuted_tokens = generate_permutations(unique_chars, max_length)

    frequencies = count_permuted_frequencies(corpus, permuted_tokens)

    top_tokens = get_top_tokens(frequencies, max_tokens)

    tokens = [token for token, _ in top_tokens]


file_path = "input.txt"
max_length = 4
max_tokens = 600

main(file_path, max_length, max_tokens)
