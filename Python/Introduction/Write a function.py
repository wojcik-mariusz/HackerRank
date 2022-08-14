def is_leap(year):
    leap = False

    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
        return leap
    else:
        if year % 4 == 0:
            leap = True
            return leap

    return leap


year = int(input())