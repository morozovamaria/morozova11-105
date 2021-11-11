a = [5, 10, 11, 8, 4, 10, 3]
max_square = 0
first_max = 0
second_max = 0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        current_square = ((a[i]+a[j])/2)*(j-i)
        if current_square > max_square:
            max_square = current_square
            first_max = i
            second_max = j
print(max_square, first_max, second_max)