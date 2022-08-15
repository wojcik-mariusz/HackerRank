from typing import List, NoReturn


def miniMaxSum(arr: List[int]) -> NoReturn:
    arr.sort(reverse=True)
    print(sum(arr[1:]), sum(arr[:-1]), sep=" ")


if __name__ == "__main__":

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
