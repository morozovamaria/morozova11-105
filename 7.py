#Реверсировать строку
a = "informatika"
a1 = list(str(a))
a1.reverse()
a2 = ''.join(map(str, a1))
print(a2)

a = "informatika"
a1 = a[::-1]
print(a1)