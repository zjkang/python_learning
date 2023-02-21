# https://www.runoob.com/w3cnote/python-func-decorators.html
# https://www.geeksforgeeks.org/args-kwargs-python/
# https://docs.python.org/3/library/functools.html


# *args = arg1, arg2, ... (0 -> multiple args)
# **kargs = arg1=val1, arg2=val2, ... (0 -> multiple key args)

# def myFun(arg1, arg2, arg3):
#     print("arg1:", arg1)
#     print("arg2:", arg2)
#     print("arg3:", arg3)
  
  
# # Now we can use *args or **kwargs to
# # pass arguments to this function :
# args = ("Geeks", "for", "Geeks")
# myFun(*args)
  
# kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
# myFun(**kwargs)

from functools import wraps

from functools import wraps

# 装饰器模板
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated
 
@decorator_name
def func():
    return("Function is running")
 
can_run = True
print(func())
# Output: Function is running
 
can_run = False
print(func())
# Output: Function will not run

# --------------------------------------------

# 用函数记录decorator
from functools import wraps
 
def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging
 
@logit
def addition_func(x):
   """Do some math."""
   return x + x
 
result = addition_func(4)
# Output: addition_func was called


# 用类记录decorator
class MyCache:
    def __init__(self, func):
        self.func = func
        self.cache = {}
    
    def __call__(self, *args):
        print(*args)
        print(f'args is {args}')
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]


@MyCache
def fib(n):
    if n == 1: return 1
    if n == 2: return 2
    return fib(n - 1) + fib(n - 2)

@MyCache
def add(a, b, c):
    return a + b + c

# print(fib(3))
print(add(1,2,3))


