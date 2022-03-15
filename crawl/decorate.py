from functools import wraps
from retrying import retry

def decorator (func) :
    '''
    @wraps(func)
    def decorated (*arg, **kwarg) :
        print("Calculating...")
        return func(*arg, **kwarg)
    return decorated
    '''
    print("Calculating...")
    return func

@decorator
def calc (x,y) :
    return x+y

print(calc(5,3))
