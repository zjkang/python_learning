# Python Hash (dict)

## dictionary init, key, values, functions

https://www.w3schools.com/python/python_dictionaries.asp

```python
dict = {} 
dict = dict(brand="Ford", model="Mustang", year=1964)
list(dict.keys())     # list of keys, convert to key: list(dict.keys())
list(dict.values())   # list of values
list(dict.items())    # list of (key,value), list(dict.items()): [(key, val),...]

for x in thisdict:         # x is key of dict
if "model" in thisdict     # Check if Key Exists
len(thisdict)              # the number of items in the dictionary
thisdict["color"] = "red"  # Adding items
thisdict.pop("model")      # Removing items  
del dict[k]                # clear key
del thisdict               # empties the dictionary

# dict update
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})

car.get('abc', 'default')

# concatenate 2 dictionary
context = {**default, **user}
```

## Write your own hash function with customized object as key

override __hash__, __eq__ methods

https: // stackoverflow.com/questions/4901815/object-of-custom-type-as-dictionary-key

```python
class MyThing:
   def __init__(self, name, location, length):
       self.name = name
       self.location = location
       self.length = length

   def __hash__(self):
       return hash((self.name, self.location, self.length))

   def __eq__(self, other):
       return (self.name, self.location, self.length) == (other.name, other.location, self.length)

   def __ne__(self, other):
       # Not strictly necessary, but to avoid having both x==y and x!=y
       # True at the same time
       return not(self == other)
  
   def __str__(self):
       return 'name: {}, location: {}, length: {}'.format(
           self.name, self.location, self.length)

dict = {}
dict[MyThing("name1", "location1", 1)] = 1
dict[MyThing("name2", "location2", 2)] = 2
for k, v in dict.items():
   print(k, v)

my_set = set()
my_set.add(MyThing("name1", "location1", 1))
my_set.add(MyThing("name2", "location2", 2))
for k in my_set:
   print(k)
```

----------------------------------------------
## defaultdict usage & example with inner type

https://docs.python.org/3/library/collections.html#collections.defaultdict

```python
# initialize a dict with [] value
from collections import defaultdict
dict = defaultdict(list) # int, set
dict['key'].append(1) # otherwise need to check if 'key' not in dict, dict['key'] = []
```

```python
def constant_factory(value):
    return lambda: value
d = defaultdict(constant_factory('<missing>'))
d.update(name='John', action='ran')
'%(name)s %(action)s to %(object)s' % d
# 'John ran to <missing>'
```

can use setdefault() instead, similar dict.setdefault(“key”, []).append(1)

----------------------------------------------
## OrderedDict example

https://docs.python.org/3/library/collections.html#collections.OrderedDict

Initialize an ordered dictionary, the (k,v) is ordered by insertion order

OrderedDict是有序的字典，它继承自dict，不过会记住每个key的插入顺序；
注意OrderedDict的排序并不是通过key的值来排序的，而是通过key的插入顺序来排序的

Implementation details: double linked list + hash map 
主要思路是用构建一个双端循环链表，该链表初始化时有一个哨兵节点（该节点永远不会被删除，这样可以简化算法） 
链表起于该哨兵节点，终于该哨兵节点；链表中每个节点格式为 [PREV, NEXT, KEY] 使用 self.__map 
来保存 Key 值和对应的双端循环链表中的节点的映射关系 使用继承的 dict 功能来保存 Key 和对应 Value 的映射关系

```python
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['A'] = 'a'
ordered_dict['B'] = 'b'
ordered_dict['1'] = '1'
for k, v in ordered_dict.items():
    print k, v
#最后的输出为
#A a
#B b
#1 1
```

----------------------------------------------
## comprehension dict/list

```python
dict_v = {i: [] for i in range(numCourses)}
list_v = [i for i in range(numCourses)]
```


----------------------------------------------
# Python Set

https://www.w3schools.com/python/python_sets.asp

```python
thisset = {"apple", "banana", "cherry"}       # Create a set
for x in thisset:                             # Print the values
  print(x)
"banana" in thisset                           # Check "banana" is present in the set

thisset.add("orange")                         # Add one item to a set use the add() method
thisset.update(["orange", "mango", "grapes"]) # Add multiple items to a set

len(thisset)                                  # Get the number of items in a set
thisset.remove("banana")                      # Use the remove(), or the discard() method
thisset.discard("banana")
thisset.clear()                               # clear() method empties the set
del thisset                                   # del keyword will delete the set completely
```




