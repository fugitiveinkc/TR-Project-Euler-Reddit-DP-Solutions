"""
Write a program that finds the maximum product of three numbers in a given
array of integers.

https://programmingpraxis.com/2017/06/30/maximum-product-of-three-revisited/
"""

from itertools import combinations

from nose.tools import *

example_solutions = [
    ([1, 5, 2, 4, 3], 3 * 4 * 5),
    ([-1, 0, 1, 2, 3], 6),
    ([-2, -1, 0, 1, 2], 4),
    ([-10, -10, 1, 2, 3], 300),
    ([-5, -4, -3, -2, -1], -6)
]


@nottest
def test_product_of_three(func):
    """
    Test given maximum-product-of-three function on a number of inputs.
    """
    for problem_input, solution in example_solutions:
        assert_equal(func(problem_input), solution)


"""
The most intuitive way to do this is by trying every possible combination of
three numbers in the list to see which is the largest:
"""

def combinations_product_of_three(seq):
    """
    Compute the maximum product of three numbers from the list, by trying every
    possible combination of three numbers to see which has the highest product.
    """
    return max(a * b * c for a, b, c, in combinations(seq, 3))


def test_combinations():
    for problem_input, solution in example_solutions:
        assert_equal(combinations_product_of_three(problem_input), solution)


"""
What is the complexity of this approach? The numbers of combinations we need to
try is "n choose k" where n is the length of the sequence and the number of
items to be chosen (which in this case is three) or
n * (n - 1) * (n - 1) / (3!) which is O(n^3).

Another way to see this is with nested for loops: we'll need to run through the
inner loop (n - 2) * (n - 2) * (n - 2) times, so this is still O(n^3).
"""

def nested_for_product_of_three(seq):
    """
    Compute the maximum product of three numbers from the list, by trying every
    combination of three numbers. Find the combinations using nested for loops.
    """
    length = len(seq)
    max_product = float("-inf")
    for a_index in range(length - 2):
        a = seq[a_index]
        for b_index in range(a_index + 1, length - 1):
            b = seq[b_index]
            for c_index in range(b_index + 1, length):
                c = seq[c_index]
                prod = a * b * c
                if prod > max_product:
                    max_product = prod
    return max_product


def test_nested_for():
    for problem_input, solution in example_solutions:
        assert_equal(combinations_product_of_three(problem_input), solution)


if __name__ == "__main__":
    pass
