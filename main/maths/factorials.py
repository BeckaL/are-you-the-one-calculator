
def double_factorial(n):
    if n <= 0:
        return 1
    else:
        return n * double_factorial(n - 2)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

