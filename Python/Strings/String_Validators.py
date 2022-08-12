from typing import NoReturn


def is_any_alphanum(s: str) -> NoReturn:
    flag = False
    for i in list(s):
        if i.isalnum():
            flag = True
            break
        else:
            continue
    print(flag)


def is_any_alphabetical(s: str) -> NoReturn:
    flag = False
    for i in list(s):
        if i.isalpha():
            flag = True
            break
        else:
            continue
    print(flag)


def is_any_digit(s: str) -> NoReturn:
    flag = False
    for i in list(s):
        if i.isdigit():
            flag = True
            break
        else:
            continue
    print(flag)


def is_any_lowercase(s: str) -> NoReturn:
    flag = False
    for i in list(s):
        if i.islower():
            flag = True
            break
        else:
            continue
    print(flag)


def is_any_uppercase(s: str) -> NoReturn:
    flag = False
    for i in list(s):
        if i.isupper():
            flag = True
            break
        else:
            continue
    print(flag)


if __name__ == "__main__":
    s = input()
    is_any_alphanum(s)
    is_any_alphabetical(s)
    is_any_digit(s)
    is_any_lowercase(s)
    is_any_uppercase(s)
