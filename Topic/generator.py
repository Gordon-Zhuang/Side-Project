import sys
def fibonacci_normal(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_normal(n-1)+fibonacci_normal(n-2)

def fibonacci_loop(n):
    i = 2
    array = [0,1]
    while i <= n:
        array.append(array[-1]+array[-2])
        i += 1
    return array
def fibonacci_generation(n):
    counter = 0
    previous = 0
    previous_2 = 1
    while counter <= n:
        yield previous
        previous_2 = previous_2+previous
        previous = previous_2-previous
        counter += 1





print(fibonacci_normal(10))
print(fibonacci_loop(10))
fib = fibonacci_generation(10)
while True:
    try:
        next(fib)
    except:
        print(fib)
        sys.exit()
