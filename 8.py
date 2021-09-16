#Палиндром. Строка зеркальна за исключением пробелов и спецсимволов (запятых например).
a = str("ТОПОТ")
a1 = a[::-1]
if a == a1:
    print(True)
else:
    print(False)

a = str("ТОПОР")
a1 = a[::-1]
if a == a1:
    print(True)
else:
    print(False)
