#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#
from typing import NoReturn


def print_full_name(first, last) -> NoReturn:
    text_to_return: str = f"Hello {first} {last}! You just delved into python."
    print(text_to_return)


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)