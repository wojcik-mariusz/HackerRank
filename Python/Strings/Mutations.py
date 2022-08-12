def mutate_string(text: str, position: int, character: str) -> str:
    text = list(text)
    text[position] = character
    conv_text = "".join(text)
    return conv_text


if __name__ == "__main__":
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
