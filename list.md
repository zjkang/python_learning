# Python List

https://www.w3schools.com/python/python_ref_list.asp

## list basic functions

```python
nums = [1, 2, 3, 4]
nums.append(1)
nums.extend([1,2,3])
nums.pop()             # removes the specified index, (or the last item if index is not specified)
nums.insert(pos=1, 10) # insert the item at specific position
del(nums[0])           # delete the first item

# slice returns a partial copy of nums 
a = nums[:3]
a[0] = 100 # nums = [1, 2, 3, 4]
```

## list iterator

```python
a = [10,20,30]
for i in a:
    print(i)   # print 10,20,30
for i, v in enumerate(a):
    print(i,v) # print(0 10) - (1 20) - (2 30)
for i in range(0, len(a), 1): # start, end, step
    print(a[i])   # print 0, step, 2*step
```

## 在recursion中，需要append a new list with deep copy

```python
new_list.append(list(old_list))

# copy list with deep copy
a = [1,2,3]
b = list(a)
b = a[:]
b = a.copy()
import copy
b = copy.deepcopy(a)
```

## swap element in a list

```python
# swap
a[i],a[j] = a[j], a[i]
```

## reverse list

```python
a=[1,2,3,4,5]
# a.reverse() change a
# a[::-1] not change a
# list(reversed(a)) not change a
```

## initialize 1-d array

```python
a = [0 for _ in range(10)] #[0] * 10
a = [0] * 10
```

## initialize 2-d array

```python
# Incorrect Approach
# [[None] * n] * m
# x[0][0] = 34
#  [[34, None, None, None, None], 
#   [34, None, None, None, None], 
#   [34, None, None, None, None], 
#   [34, None, None, None, None], 
#   [34, None, None, None, None]
#  ]

# Correct Approach
rows, cols = 3, 2
r = [[None for i in range(cols)] for j in range(rows)]
r = [[0] * cols for _ in range(rows)]

# Flattern 2d array
array_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [element for row in array_2d for element in row]

print(flattened)

```

## list sorting algorithm

```
a = [1,2,4,3,5]
a.sort(reverse=True, key=lambda x: (x[0])) # change a
b = sorted(a, reverse=True, key=lambda x: (x[0])) # not change a

# partial sort
a = range(20,0,-1) # [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
a[10:15] = sorted(a[10:15])

# 俄罗斯套娃 https://www.lintcode.com/problem/russian-doll-envelopes/description
# 二维数组 (x[0]从小到大，x[1]从大到小)排序
height = [a[1] for a in sorted(envelopes, key=lambda x: (x[0], -x[1]))]
```

Python3 does not support cmp function nativaly, it only supports key. To make it work, need to use from functools import cmp_to_key, and then embed compare function into cmp_to_key
https://stackoverflow.com/questions/5213033/sort-list-of-list-with-custom-compare-function-in-python

```python
from functools import cmp_to_key

def fitness(item):
    return item[0]+item[1]+item[2]+item[3]


def compare(item1, item2):
    if fitness(item1) < fitness(item2):
        return -1
    elif fitness(item1) > fitness(item2):
        return 1
    else:
        return 0


l = [list(range(i, i+4)) for i in range(10,1,-1)]
print(sorted(l, key=cmp_to_key(compare)))
```

## binary search package

```python
import bisect                                 # binary insert value k
bisect.bisect_left(list, number, start, end)  # 插入后有序靠左，>=k的第一个
bisect.bisect_right(list, number,start, end)  # 插入后有序靠右，>k的第一个

import bisect

a = [1,2,2,3,5,5]
assert(bisect.bisect_left(a, 2) == 1)
assert(bisect.bisect_left(a, 4) == 4)

assert(bisect.bisect_right(a, 2) == 3)
assert(bisect.bisect_right(a, 4) == 4)
assert(bisect.bisect_right(a, 5) == 6)
```

## string vs list

```python
str = 'abcdefgh'
num_list = list(str) # ['a', 'b', ..., 'h']
nums = []
nums.extend(str) # ['a', 'b', ..., 'h']
```

## difference between .append() and +=[]

```python
# https://stackoverflow.com/questions/725782/in-python-what-is-the-difference-between-append-and/725882
# In the example you gave, there is no difference, in terms of output, between append and +=. 
# But there is a difference between append and + (which the question originally asked about).

a = []
id(a)  # 11814312
a.append("hello")
id(a)  # 11814312

b = []
id(b)  # 11828720
c = b + ["hello"]
id(c)  # 11833752

b += ["hello"]
id(b)  # 11828720
```

## Numpy array vs Python native List

numpy array enforces the same type of elements.

```python
# numpy array: 2d array access
np_baseball[i,j]   # i-row, j-col data
np_baseball[:,0]   # the first column of data
np_baseball.shape  # 2-d dimention
```


