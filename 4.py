# Являются ли анаграммами "автор" "товар"?
def anagramma(a = "", b = ""):
    return sorted(a) == sorted(b)
a = "товар"
b = "автор"
print(anagramma(a,b))
