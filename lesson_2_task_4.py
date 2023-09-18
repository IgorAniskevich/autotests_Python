#вариант 1
n = input("введите число ")
n = int (n)
for i in range (1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print ("FuzzBizz")
    elif i % 3 == 0:
        print("Fuzz")
    elif i % 5 == 0:
        print("Buzz")
    else:
     print (i)
# вариант 2
def  fizz_buzz (n):
    for i in range (1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print ("FuzzBizz")
        elif i % 3 == 0:
            print("Fuzz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print (i)
fizz_buzz(15)