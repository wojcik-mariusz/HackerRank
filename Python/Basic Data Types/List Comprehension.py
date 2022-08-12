from itertools import permutations, combinations, combinations_with_replacement

if __name__ == '__main__':
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())
    x = 1
    y = 1
    z = 1
    n = 2

    arr = []

    for x1 in range(x+1):
        for y2 in range(y+1):
            for z1 in range(z+1):
                if x1 + y2 + z1 !=n:
                    arr.append([x1, y2, z1])



    arr.sort(key=sum)
    print(arr)

    print([[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=n])