def bank(x,y):
    print("ваш вклад на ", x, "лет")
    print("ваша сумма ", y, "рублей")
    for i in range (0, x):
        y = y + y*0.1
    print("через ", x, "лет у вас будет ", y, "рублей")
    
bank(2,100)
