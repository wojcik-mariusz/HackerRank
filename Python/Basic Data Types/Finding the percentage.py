if __name__ == '__main__':
    # n = int(input())
    # student_marks = {}
    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    # query_name = input()

    student_marks = {"Krishna": [67, 68, 69],
                     "Arjun": [70, 98, 63],
                     "Malika": [52, 56, 60]}

    query_name = "Malika"

    scores = [x for x in student_marks.get(query_name)]
    mark = 0
    for score in scores:
        mark += score
    result = float((mark/len(scores)))

    print(" %.2f" %result)