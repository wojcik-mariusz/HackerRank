def print_formatted(number):
    for i in range(n):
        if i < 10:
            print(" "+ str(i), oct(i), hex(i), bin(i), sep="   ")
        else:
            print(i, oct(i), hex(i), bin(i), sep="    ")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)