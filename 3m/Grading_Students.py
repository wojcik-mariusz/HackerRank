#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades: list[int]) -> List[int]:
    output_list = []
    for grade in grades:
        if grade < 38 or not grade % 5 >= 3:
            output_list.append(grade)
        else:
            grade += (5 - grade%5)
            output_list.append(grade)
    return output_list


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # grades_count = int(input().strip())

    grades = [2, 5, 0, 4, 73, 67, 38, 33]

    # for _ in range(grades_count):
    #     grades_item = int(input().strip())
    #     grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

    gr = 73
    print(gr%5)
    gr += (5 - gr%5)
    print(gr)
    gr = 67
    print(gr % 5)
    gr += (5 - gr % 5)
    print(gr)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
