from functools import reduce

def fibonacci(limit):
    numbers = [1,1]
    if limit  <= 2:
        return numbers[limit-1]
    else:
        for i in range(0,limit-2):
            accum = reduce(lambda x,y : x + y, numbers)
            numbers[0] = numbers[1]
            numbers [1] = accum
    return numbers[1]

print(fibonacci(1000)/)
