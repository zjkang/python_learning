# Foundation

## Basic knowledge

```python
# a is None and b is not None
None

# division
l // length #int(l/length)
l % length (module)

# power calculation
x**y # 2**3 = 8

# iteration
for index,item in enumerate(nums) # index, val

# range([start], stop[, step])
range(5) # numbers range(0,5); convert to list: list(range(5)): [0,1,2,3,4]

# max or min integer
import sys
max = sys.maxsize
min = -sys.maxsize -1

# max or min float
float('inf') <=> math.inf
float('-inf')  <=> -math.inf



# Generate random number <https://pythonspot.com/random-numbers/>
import random
for _ in range(10):
    # random int between [1,100]; closed intervals
    random.randint(1,100)
```

---------------------------

## Class / Object

```python
Class Test:
  def __init__(self):
    pass
  
  def __str__(self):
    pass
  
  def __cmp__(self):
    pass

  def __lt__(self):
    pass
  
  # look up supported methods in class
  def __dict__(self):
```

---------------------------

## Python map/filter/reduce

Map function (https://www.w3schools.com/python/ref_func_map.asp)

```python
def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
#convert the map into a list, for readability:
print(list(x))

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(x)

#convert the map into a list, for readability:
print(list(x))
```

---------------------------
