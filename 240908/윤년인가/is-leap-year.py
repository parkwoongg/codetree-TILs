year = int(input())
if year%4 == 0:
    if year%100 == 0 and year%400 != 0:
        print("false")
    print("true")
else:
    print("false")