from time import time, sleep

def calc_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        return start_time, result, end_time
    return wrapper

@calc_time
def summa(*args):
    sum = 0
    for i in args:
        sum += i
        sum = sum**4
    return sum

start_time, result, end_time = summa(1,2,3,4,5,6,7,34,2,2,2,2,2)

with open("records.txt", 'w') as file:
    file.write("Входные данные: 1,2,3,4,5,6,7,34,2,2,2,2,2\n")
    file.write(f"{start_time}\n")
    file.write(f"{end_time}\n")
    file.write(f"{end_time-start_time}\n")


