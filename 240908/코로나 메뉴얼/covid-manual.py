arr_1 = []
arr_2 = []
c = 0
for _ in range(3):
    x, y = input().split()
    arr_1.append(x)
    arr_2.append(y)
for i in range(3):
    if arr_1[i] == "Y":
        if int(arr_2[i]) >=37:
            c += 1
if c>= 2:
    print("E")
else:
    print("N")