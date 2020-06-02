# Python Queue

## Message queue (multi-thread: async queue)

not used in algorithm (https://docs.python.org/3/library/queue.html)

```python
import queue 
q = queue.Queue(maxsize=20)  
q.put(5)   # put element into queue
q.get()    # take data out from the Queue and remove from the head of the queue 
q.queue[0] # indexing: get the 0 element from the queue
q.qsize() 
q.empty() 
q.full()
```

## Use deque (collections.deque)

https://docs.python.org/2/library/collections.html#collections.deque

```python
 
from collections import deque
d = deque('ghi')        # make a new deque with three items

queue = collections.deque([(source.x, source.y)]) # use [] to initialize

for elem in d:          # iterate over the deque's elements
   print elem.upper()   # G H I

d.append('j')           # add a new entry to the right side
d.appendleft('f')       # add a new entry to the left side
d                       # deque(['f', 'g', 'h', 'i', 'j'])

d.pop()                 # return and remove the rightmost item 'j'
d.popleft()             # return and remove the leftmost item 'f'

list(d)                 # list the contents of the deque ['g', 'h', 'i']
d[0]                    # peek at leftmost item 'g'
d[-1]                   # peek at rightmost item 'i'

# list the contents of a deque in reverse ['i', 'h', 'g']
list(reversed(d))
'h' in d                # search the deque True
# add multiple elements at once deque(['g', 'h', 'i', 'j', 'k', 'l'])
d.extend('jkl')

d.rotate(1)             # right rotation deque(['l', 'g', 'h', 'i', 'j', 'k'])
d.rotate(-1)            # left rotation deque(['g', 'h', 'i', 'j', 'k', 'l'])

# make a new deque in reverse order deque(['l', 'k', 'j', 'i', 'h', 'g'])
deque(reversed(d))
d.clear()               # empty the deque
d.pop()                 # cannot pop from an empty deque
queue = deque([root])   # root is TreeNode, deque initialized with []
```
