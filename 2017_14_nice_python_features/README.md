
This week, I'd like to write a blog with the python tricks that I really like to use in my everyday work. These tricks can save me time or space. Hope these are useful to you as well. If you have good ones, let me know. You can find the notebook on [Qingkai's Github](https://github.com/qingkaikong/blog/tree/master/2017_14_nice_python_features). 

### Print path of the imported string


```python
import threading 
import socket
 
print(threading)
print(socket)
```

    <module 'threading' from '/Users/qingkaikong/miniconda2/lib/python2.7/threading.pyc'>
    <module 'socket' from '/Users/qingkaikong/miniconda2/lib/python2.7/socket.pyc'>


### Inspect an object


```python
a = [1, 2, 3, 4]
print(dir(a))
```

    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


### Reversing an iterable using negative step

This is really handy if you want to reverse an object. 


```python
a = 'Hello world'
print(a[::-1])
b = [1,2,3,4,5]
print(b[::-1])
```

    dlrow olleH
    [5, 4, 3, 2, 1]


### Using zip

I like to use zip in the loop, especially when I plot something with different colors, very handy. 


```python
a = ['H', 'O', 'H']
b = ['i', 'k', 'a']
for x, y in zip(a, b):
    print(x+y)
```

    Hi
    Ok
    Ha


### Swap two numbers 

Swap in oneliner. 


```python
a = 4
b = 2 
b, a = a, b
print(a, b)
```

    (2, 4)


### List/dictionary comprehension

One of my favorite, and it can save a lot of spaces. 


```python
print([x * x for x in range(0, 10)])
print({i: i**2 for i in range(5)})
```

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


### Enumerate

When you need the index as well in the loop. 


```python
a = ['Hello', 'world', '!']
for i, x in enumerate(a):
    print('{}, {}'.format(i, x))
```

    0, Hello
    1, world
    2, !


### Conditional assignment

A quick conditional assignment that saves a lot of spaces. 


```python
y = 3
x = 3 if (y == 1) else 2
print(x)
```

    2


### Transpose an array

A quick way to transpose an array. 


```python
a = [(1,2), (3,4), (5,6)]
print(zip(*a))
```

    [(1, 3, 5), (2, 4, 6)]


### lambda function

I like lambda funciton, especially use it to define some simple funcitons. 


```python
f = lambda x = 1, y = 1: x + y 
print(f())
print(f(1, 2))
```

    2
    3


### Map function

A quick way to apply the same operation on all the items in a container. 


```python
f = lambda x: x**2

a = [1, 2, 3, 4, 5]
print(map(f, a))
```

    [1, 4, 9, 16, 25]


### Sort

A quick sort of tuple.


```python
# sort based on the 1st item
a = [(2, "b"), (1, "a"), (4, "d"), (3, "c")]
print(sorted(a))

# sort based on the 2nd item
b = [("b", 2), ("a", 1), ("d", 4), ("c", 3)]
print(sorted(b, key=lambda x: x[1]))
```

    [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    [('a', 1), ('b', 2), ('c', 3), ('d', 4)]


### Flatting a list with sum


```python
a = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
print(sum(a, []))
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9]


### Inverting a dictionary


```python
a = {"one":1, "two":2, "three":3, "four":4, "five":5}
print(a)
print(dict(zip(a.values(), a.keys())))
```

    {'four': 4, 'three': 3, 'five': 5, 'two': 2, 'one': 1}
    {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}


### Partial function


```python
from functools import partial
bound_func = partial(range, 0, 11)
```


```python
bound_func()
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



### Start a simple server

Sometimes, I need a simple server to test. Oneliner!


```python
# in the command line run this
python -m SimpleHTTPServer
```

### Chaining comparison operators


```python
a = 5
if 0 < a < 10:
    print("Yes")
```

    Yes


### Function argument unpack


```python
def print_number(x, y):
    print("x: %d"%x)
    print("y: %d"%y)

point_foo = (3, 4)
point_bar = {'y': 3, 'x': 2}

print_number(*point_foo)
print_number(**point_bar)
```

    x: 3
    y: 4
    x: 2
    y: 3


### Get a unique random ID


```python
import uuid
print uuid.uuid4()
```

    8a479a6e-5072-48fc-99c3-7cced54bdb61


### import this


```python
import this
```

    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

