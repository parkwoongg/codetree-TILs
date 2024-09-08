arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

if arr_1[0] > arr_2[0]:
    print("A")
elif arr_1[0] == arr_2[0]:
    if arr_1[1] > arr_2[1]:
        print("A")
    else:
        print("B")
else:
    print("B")