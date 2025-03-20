r = 2


def fib_recursion(a, b):
    global r
    if r <= 19:
        new_fib = a + b
        print(new_fib)
        a = b
        b = new_fib
        r += 1
        fib_recursion(a, b)
    else:
        return


fib_recursion(1, 0)
