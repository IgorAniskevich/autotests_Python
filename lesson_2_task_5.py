#def month_to_season():
n = input("введите номер месяца ")
n = int (n)
if n > 12 or n < 1:
    print ("такого месяца не существует")
if n == 12 or n==1 or n==2:
    print("у вас сейчас зима")
elif n == 3  or n==4 or n==5:
    print("у вас сейчас весна")
elif n == 6  or n==7 or n==8:
     print("у вас сейчас лето")
elif n == 9  or n==10 or n==11:
    print("у вас сейчас осень")
    