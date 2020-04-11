#!/usr/bin/env python3.7
def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop :
        yield num
        num += step

# when run >>>
# generated_numbers = gen_range(10)
#>>> next(generated_numbers)
#>>> 1
#>>> next(generated_numbers)
#>>> 2
# when loop ends it generates stopitenation error

for num in gen_range(10):
    print(num)


def gen_fib():
    a , b = 0, 1
    while True:
        a , b = b , a+b
        yield a

# fib = gen_fib()
#>>> [next(fib) for x in range(50)]
