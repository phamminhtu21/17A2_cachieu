def fun(n):
    if (n>50):
        return n-3
    return fun(fun(n+5))
print(fun(9))