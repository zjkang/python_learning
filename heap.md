# Python Max/Min heap

## default: always use min priority-queue

```python
import heapq

nums = [1,2,3,10]
heapq.heapify(nums) # min-heap
heapq.heappush(nums, 4)
heapq.heappop(nums) # 1

nums = []
num = 5
heapq.heappush(nums, -num) # max-heap
num = -heapq.heappop(nums) # 5
```

## remove an element from heap

https://stackoverflow.com/questions/10162679/python-delete-element-from-heap

```python
# remove index i from a heap quite easily O(n)
nums[i] = nums[-1]
nums.pop()
heapq.heapify(nums)

# call a couple of the internal heapify functions
h[i] = h[-1]
h.pop()
if i < len(h):
    # heapq._siftup(h, i) # do not need
    heapq._siftdown(h, 0, i)
```

## heap sorting based on tuple value

1. can change from min-heap to max-heap by adding ‘-’ but remember to convert back

2. 利用一个key函数，封装data变成一个tuple key，
然后按照key排序https://stackoverflow.com/questions/8875706/heapq-with-custom-compare-predicate

```python
# 1. max-heap, long dist -> short dist
heapq.heappush(heap, (-dist, -p.x, -p.y)) # sorting from long dist -> short dist

# 2. sort based on key in tuple
def compute_key(item):
  return 10 / (item + 1)

nums = []
heapq.heappush(nums, (compute_key(1), 1))
heapq.heappush(nums, (compute_key(2), 2))
heapq.heappush(nums, (compute_key(3), 3))
```

## Lambda function: rewrite __lt__ function

```python
class ListNode(object):
   def __init__(self, val, next=None):
       self.val = val
       self.next = next
# overwrite the compare function 
# so that we can directly put ListNode into heapq (override 'less than' method)
ListNode.__lt__ = lambda x,y: x.val < y.val # min-heap
def less_than(s, o):
    return s.val < o.val
ListNode.__lt__ = less_than

import heapq
nums = []
heapq.heappush(nums, ListNode(5))
heapq.heappush(nums, ListNode(3))
heapq.heappush(nums, ListNode(1))

while len(nums):
   print(heapq.heappop(nums).val) # 1 3 5
```

## Customized class: rewrite __lt__ function

```python
import heapq

class Node:
 def __init__(self, val):
   self.val = val

 def __lt__(self, o):
   return self.val > o.val  # max-heap(>)
#   return self.val < o.val  # min-heap(<)

node1 = Node(1)
node2 = Node(2)
node3 = Node(10)
node4 = Node(0)

nums = []
heapq.heappush(nums, node1)
heapq.heappush(nums, node2)
heapq.heappush(nums, node3)

while len(nums) > 0:
 print(heapq.heappop(nums).val)
```

