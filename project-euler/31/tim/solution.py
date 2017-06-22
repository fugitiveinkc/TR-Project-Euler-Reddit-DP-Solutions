def recursive_make_change(amount, coins, start=0):
    """
    Return a list of all ways to make a certain amount from the given
    denominations, starting from the given coin size.
    """
    # base case
    if start == len(coins):
        if amount > 0:  # If we ran out of coins to use
            return []  # return a list of no solutions;
        else:  # If we've already made change for everything
            return [[]]  # list with a single empty solution.

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

if __name__ == "__main__":
    two_pounds = recursive_make_change(200, [200, 100, 50, 20, 10, 5, 2, 1])
    print(len(two_pounds))
