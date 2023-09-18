is_year_leap = input("напишите год: ")
is_year_leap = int (is_year_leap)
if is_year_leap % 4 == 0:
    print(is_year_leap, "год високосный")
else:
     print(is_year_leap, "год не високосный")