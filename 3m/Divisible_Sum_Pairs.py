#!/bin/python3

import math
import os
import random
import re
import sys

from typing import List
from itertools import combinations

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#


def divisibleSumPairs(n: int, k: int, ar: List[int]) -> int:
    list_of_pairs = []
    possible_pairs = list(combinations(ar, 2))
    for pair in possible_pairs:
        if (pair[0] + pair[1]) % k == 0:
            list_of_pairs.append(pair)
    return len(list_of_pairs)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + "\n")

    fptr.close()
