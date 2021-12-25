def simple_numbers(limit):
    flag = False
    for i in range(1,limit+1):
        for j in range(2,i):
            if i % j == 0:
                flag = True
                break
        if flag:
            flag = False
        else:
            yield i

print(list(simple_numbers(12)))