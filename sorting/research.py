import json

from abc import ABC, abstractmethod

from sorting.algorithms import generate_random_list, generate_ordered_list, generate_reversed_list

RESERVED = 'reserved'
ORDERED = 'ordered'
RANDOM = 'random'


class SortingAlgorithm(ABC):
    def __init__(self):
        self.comparisons = 0

    def gt(self, value_1, value_2) -> bool:
        self.comparisons += 1
        return value_1 > value_2

    def gte(self, value_1, value_2) -> bool:
        self.comparisons += 1
        return value_1 >= value_2

    def lt(self, value_1, value_2) -> bool:
        self.comparisons += 1
        return value_1 < value_2

    def lte(self, value_1, value_2) -> bool:
        self.comparisons += 1
        return value_1 <= value_2

    def eq(self, value_1, value_2) -> bool:
        self.comparisons += 1
        return value_1 == value_2

    @abstractmethod
    def sort(self, values):
        pass


class BubbleSort(SortingAlgorithm):
    def sort(self, values):
        self.comparisons = 0
        length = len(values)
        n = 0
        swap_occurred = True

        while n < length and swap_occurred:
            swap_occurred = False
            for index in range(length - 1):
                if self.gt(values[index], values[index + 1]):
                    values[index], values[index + 1] = values[index + 1], values[index]
                    swap_occurred = True

            n += 1


def simulate(algorithm: SortingAlgorithm, max_length):
    """
    Przyjmuje algorytm, za pomocą którego zostanie wykonane sortowanie list:
    uporządkowanej, odwrotnie uporządkowanej i losowo uporządkowanej
    o dlugosciach od 1 do max_length.

    {'ordered': {10: 9, 20:19, ..., 1000: 999}
    'reversed': {10: 9000 ..., 20: ..., ..., 1000: 999000}
    'random': {10: 9000 ..., 20: ..., ..., 1000: 999000}
    }

    """

    result = {
        ORDERED: {},
        RANDOM: {},
        RESERVED: {}
    }

    for length in range(1, max_length + 1):
        ordered_list = generate_ordered_list(length)
        algorithm.sort(ordered_list)
        result[ORDERED][length] = algorithm.comparisons

        reversed_list = generate_reversed_list(length)
        algorithm.sort(reversed_list)
        result[RESERVED][length] = algorithm.comparisons

        random_list = generate_random_list(length, 0, 10)
        algorithm.sort(random_list)
        result[RANDOM][length] = algorithm.comparisons

    filename = f'{algorithm.__class__.__name__}_{max_length}.json'
    with open(filename, 'w') as f:
        json.dump(result, f, indent=4, sort_keys=True)


if __name__ == "__main__":
    # length = 1000
    # ordered_list = generate_ordered_list(length)
    # reversed_list = generate_reversed_list(length)
    # random_list = generate_random_list(length, 0, 10)
    #
    # experiment_list = random_list
    # algorithm = BubbleSort()
    # algorithm.sort(experiment_list)
    # print(algorithm.comparisons)
    algorithm = BubbleSort()
    simulate(algorithm, 100)
