#!/usr/bin/python

import sys


def making_change(amount, denominations):
  # dictionary to keep track of all amounts
    count = {x: 0 for x in range(amount + 1)}
    # there is only one way to make 0 cent change
    # base case: seed that money as 1
    count[0] = 1

    for coin in denominations:
        for money in range(coin, amount + 1):
            count[money] += count[money - coin]

    return count[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
