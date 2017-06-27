def recursive_make_change(amount, coins, start=0):
    """
    Return a list of all ways to make a certain amount from the given
    denominations, starting from the given coin size.
    """
    # base case
    if start == len(coins) - 1:
        # There is only one coin left. Can we make this amount with that coin?
        if amount % coins[-1] == 0:
            return [[amount / coins[-1]]]  # yes, this is the only possibility
        else:
            return []  # impossible; return a list of no solutions

    # For each possible amount of the highest coin, recurse for the rest of
    # the solutions.
    results = []
    coin = coins[start]
    for n in range(amount // coin + 1):
        rest = recursive_make_change(amount - coin * n, coins, start + 1)
        for partial_solution in rest:
            results.append([n] + partial_solution)
    return results


def test_recursive_make_change():
    # expected solution for 10 cents
    assert (recursive_make_change(10, [25, 10, 5, 1]) == [
        [0, 0, 0, 10], [0, 0, 1, 5], [0, 0, 2, 0], [0, 1, 0, 0]]), "10 cents"

    for pennies in range(1, 100):
        assert (recursive_make_change(pennies, [1]) == [[pennies]])

    two_pounds = recursive_make_change(200, [200, 100, 50, 20, 10, 5, 2, 1])
    assert (len(two_pounds) == 73682)


# test_recursive_make_change()  # passing


# takes .412 seconds- doesn't really seem to save much time!
def memoization_make_change(amount, coins, start=0, memos=dict()):
    """
    Return a list of all ways to make a certain amount from the given
    denominations, starting from the given coin size.

    Cache solutions in the "memos" dictionary, using (amount, coins, start) as
    a key. Before recursing and building solutions, check to see if we've
    already solved this problem.
    """
    # base case
    if start == len(coins) - 1:
        # There is only one coin left. Can we make this amount with that coin?
        if amount % coins[-1] == 0:
            return [[amount / coins[-1]]]  # yes, this is the only possibility
        else:
            return []  # impossible; return a list of no solutions

    # Check memos for cached solution
    key = (amount, tuple(coins), start)
    if key in memos:
        return memos[key]

    # For each possible amount of the highest coin, recurse for the rest of
    # the solutions.
    results = []
    coin = coins[start]
    for n in range(amount // coin + 1):
        rest = memoization_make_change(
            amount - coin * n, coins, start + 1, memos)
        for partial_solution in rest:
            results.append([n] + partial_solution)

    # Cache solution before returning
    memos[key] = results
    return results


def test_memoization_make_change():
    # expected solution for 10 cents
    assert (memoization_make_change(10, (25, 10, 5, 1)) == [
        [0, 0, 0, 10], [0, 0, 1, 5], [0, 0, 2, 0], [0, 1, 0, 0]]), "10 cents"

    for pennies in range(1, 100):
        assert (memoization_make_change(pennies, (1,)) == [[pennies]])

    two_pounds = memoization_make_change(200, (200, 100, 50, 20, 10, 5, 2, 1))
    assert (len(two_pounds) == 73682)


# test_memoization_make_change()  # Passing!


if __name__ == "__main__":
    two_pounds = memoization_make_change(200, [200, 100, 50, 20, 10, 5, 2, 1])
    assert (len(two_pounds) == 73682)
    print(len(two_pounds))
