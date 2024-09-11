

def fatorial(n):
    """ Aqui é uma docstring """
    if n <= 1:
        return 1
    return n * fatorial(n-1)
x = fatorial(5)
print(x)


