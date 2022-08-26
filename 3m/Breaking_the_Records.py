import math
import os
import random
import re
import sys
from typing import List

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores) -> List[int]:
    break_min_counter: int = 0
    break_max_counter: int = 0
    min_score = List[0]
    max_score = List[0]
    for actual_score in List[1:]:
        if actual_score < min_score:
            min_score = actual_score
            break_min_counter += 1
        elif actual_score > max_score:
            max_score = actual_score
            break_max_counter += 1
    result = [break_max_counter, break_min_counter]
    return result


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
