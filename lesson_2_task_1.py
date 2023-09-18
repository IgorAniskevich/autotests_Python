frut = ["виноград", "персик", "апельсин", "груша", "банан", "яблоко"]

# Реение первое
# print (frut[0])
# print (frut[5])


# рещение второе
for i in range(0, len(frut)):
    if i == 0 or  i+1 == len(frut):
        print (frut[i])
    