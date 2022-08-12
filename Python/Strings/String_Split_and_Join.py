from typing import List, NoReturn


def split_and_join(line: str) -> str:
    text_to_split: List[str] = line.split(" ")
    splitted_text: str = "-".join(word for word in text_to_split)
    return splitted_text


def print_to_console(arg:str) -> NoReturn:
    print(arg)


if __name__ == '__main__':
    text = input()
    print_to_console(split_and_join(text))