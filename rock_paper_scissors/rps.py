#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    answer = []
    choices = ["rock", "paper", "scissors"]  # possible choices

    # inner recursive function to add result
    def get_result(pending_rounds, result=[]):
        # base case: no rounds remain
        if pending_rounds == 0:
            answer.append(result)
            return
        for choice in choices:
            get_result(pending_rounds - 1, result + [choice])

    get_result(n)
    return answer


rock_paper_scissors(12)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
