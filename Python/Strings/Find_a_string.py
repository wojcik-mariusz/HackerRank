def count_substring(text: str, sub_string: str) -> int:
    counter: int = 0
    len_of_text: int = len(text)
    len_of_sub_string: int = len(sub_string)
    index: int = 0
    for i in list(text):
        if index < (len_of_text - len_of_sub_string + 1):
            success = text.find(sub_string, index, index + len_of_sub_string)
            if success != -1:
                counter += 1
            index += 1
    return counter


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
