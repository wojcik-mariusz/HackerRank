N, M = map(int, input().split(" "))
pattern_height = N
pattern_width = M
welcome_str = "WELCOME"
welcome_pattern = welcome_str.center(pattern_width, "-")
up_down_pattern = ".|."
for i in range(((pattern_height - 1) // 2)):
    x = up_down_pattern * (i * 2 + 1)
    print(x.center(M, "-"))

print(welcome_pattern)

for i in range(((pattern_height - 1) // 2), 0, -1):
    x = up_down_pattern * (i * 2 - 1)
    print(x.center(M, "-"))
