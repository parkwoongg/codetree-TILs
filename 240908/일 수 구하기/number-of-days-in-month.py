31
28
31
30
31
30
31
31
30
31
30
31

a = int(input());
if a == 2:
    print(28)
elif a <= 7:
    if a%2==0:
        print(30)
    else:
        print(31)
else:
    if a%2==0:
        print(31)
    else:
        print(30)