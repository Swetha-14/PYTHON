def is_leap(year):
    leap = False
    if year >= 1900:
        if (year % 400) == 0:
            leap = True
            return  leap
        elif (year % 4) == 0 and (year % 100) != 0:
            leap = True
            return  leap
        else:
            return leap

year = int(raw_input())
