from typing import List, NoReturn

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr_list as parameter.
#


def plus_minus(iterable: List[int]) -> NoReturn:
    positive_ints = list(filter(lambda x: x > 0, iterable))
    negative_ints = list(filter(lambda x: x < 0, iterable))
    zeros = list(filter(lambda x: x == 0, iterable))
    positive_ints_ratio: float = len(positive_ints) / n
    negative_ints_ratio: float = len(negative_ints) / n
    zeros_ratio: float = len(zeros) / n
    print(
        "{:.6f}".format(positive_ints_ratio),
        "{:.6f}".format(negative_ints_ratio),
        "{:.6f}".format(zeros_ratio),
        sep="\n",
    )


if __name__ == "__main__":
    n = int(input().strip())

    arr_list = list(map(int, input().rstrip().split()))

    plus_minus(iterable=arr_list)
