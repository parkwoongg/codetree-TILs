def mid(a, b, c):
    if a > b and a < c:
        return a
    elif a > b and c < a:
        if b > c:
            return b
        else:
            return c
    elif a < b and b < c:
        return b
    elif a < b and b > c:
        if a > c:
            return a
        else:
            return c

a, b, c = map(int, input().split())
print(mid(a, b, c))