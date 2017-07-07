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


def sort2(a, b):
    """Return two numbers, sorted."""
    if a <= b:
        return (a, b)
    else:
        return (b, a)


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
        assert_equal(nested_for_product_of_three(problem_input), solution)


"""
If all of the numbers are positive, we know the highest product of three
numbers from the list will be the product of its highest three numbers. If
there are at least two negative numbers we know that the highest product could
potentially be the product of the largest number with the two negative numbers
with the highest magnitude.

If we sort the list first, we can grab those numbers right off the top and
bottom and return the largest one. Since this requires sorting the list it is
O(n log n).
"""


def sorting_product_of_three(seq):
    """
    Compute the maximum product of three numbers from the list, by sorting the
    list and seeing which number is bigger, the product of the three largest
    positive numbers, or the product of the largest positive number and the two
    largest magnitude negative numbers.
    """
    seq = sorted(seq)
    return max([seq[0] * seq[1] * seq[-1], seq[-3] * seq[-2] * seq[-1]])


def test_sorting_product_of_three():
    for problem_input, solution in example_solutions:
        assert_equal(sorting_product_of_three(problem_input), solution)


"""
But, we don't care about the order of the middle part of the list, or even the
order of the smallest two, or the second- and third-largest numberes. We can
find these numbers by looping through the list once, which is linear!!!
"""


def product_of_three(seq):
    """
    Compute the maximum product of three numbers from the list, by looping
    through the list once to find the smallest two and largest 3 numbers, and
    seeing which number is bigger, the product of the three largest positive
    numbers, or the product of the largest positive number and the two largest-
    magnitude negative numbers.
    """
    largest = float("-inf")
    second_largest = float("-inf")
    third_largest = float("-inf")
    smallest = float("inf")
    second_smallest = float("inf")
    for item in seq:
        tmp = item
        tmp, largest = sort2(tmp, largest)
        tmp, second_largest = sort2(tmp, second_largest)
        tmp, third_largest = sort2(tmp, third_largest)

        tmp = item
        smallest, tmp = sort2(smallest, tmp)
        second_smallest, tmp = sort2(second_smallest, tmp)

    return max(
        largest * second_largest * third_largest,
        smallest * second_smallest * largest)


def test_product_of_three():
    for problem_input, solution in example_solutions:
        assert_equal(product_of_three(problem_input), solution)


if __name__ == "__main__":
    pass
