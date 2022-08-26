import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.


def is_am(input_time: str) -> bool:
    return True if input_time.endswith("AM") else False


def timeConversion(s: str) -> str:
    hour: str = s[:2]
    minute_and_second: str = s[2:-2]
    if is_am(s):
        if hour == "12":
            hour = "00"
        converted_time = hour + minute_and_second

    else:
        if hour == "12":
            hour: str = "12"
        else:
            hour = str(int(hour) + 12)
        converted_time = hour + minute_and_second
    return converted_time


if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
