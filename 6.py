#Дан массив чисел и число. Найти 2 числа в массиве, которые в сумме дают данное число/
a = [1,3,2,6,7,2]
b = 8
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[i] + a[j] == b:
            print(a[i], a[j])

