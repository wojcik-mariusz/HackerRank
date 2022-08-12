
def swap_case(s: str) -> str:
    return s.swapcase()

if __name__ == '__main__':
    string_to_swap: str = input()
    swap_cased: str = swap_case(string_to_swap)
    print(swap_cased)