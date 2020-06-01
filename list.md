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


