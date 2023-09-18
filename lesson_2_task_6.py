lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
for i in range (0, len(lst)):
    n = lst[i]
    if n < 30 and n % 3 == 0:
        print(lst[i])
