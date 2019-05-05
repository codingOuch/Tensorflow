# *_*coding:utf-8 *_*
def fib(max):
    n, a, b = 1, 0, 1
    while n <= max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

