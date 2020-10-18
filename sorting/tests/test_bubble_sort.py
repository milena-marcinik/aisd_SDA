from unittest import TestCase, main

from sorting.algorithms import bubble_sort


class TestStack(TestCase):
    def test_sorting(self):
        numbers = [5, 3, 1, 9]
        bubble_sort(numbers)

        self.assertEqual([1, 3, 5, 9], numbers)


if __name__ == '__main__':
    main()