
We talked about a simple way to parallel your python code by using joblib in [a former blog](http://qingkaikong.blogspot.com/2016/06/python-module-joblib-make-parallelism.html). Today, I want to use it to parallel a method in a class, but I encountered some problem. In this week's blog, I will show you how we can solve the problem by using the joblib (You can use python's [multiprocessing](https://docs.python.org/2/library/multiprocessing.html) as well). You can download the script at [Qingkai's Github](https://github.com/qingkaikong/blog/tree/master/42_parallel_method_in_class). 

## Error! If we parallel directly


```python
from joblib import Parallel, delayed
```


```python
# let's re-write the exact function before into a class
class square_class:
    def square_int(self, i):
        return i * i
     
    def run(self, num):
        results = []
        results = Parallel(n_jobs= -1, backend="threading")\
            (delayed(self.square_int)(i) for i in num)
        print(results)
```


```python
square_int = square_class()
square_int.run(num = range(10))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-54-63d78c56401c> in <module>()
          1 square_int = square_class()
    ----> 2 square_int.run(num = range(10))
    

    <ipython-input-53-c2a13f8e0fa7> in run(self, num)
          6     def run(self, num):
          7         results = []
    ----> 8         results = Parallel(n_jobs= -1, backend="threading")            (delayed(self.square_int)(i) for i in num)
          9         print(results)


    /Users/qingkaikong/miniconda2/lib/python2.7/site-packages/joblib/parallel.pyc in __call__(self, iterable)
        798             # was dispatched. In particular this covers the edge
        799             # case of Parallel used with an exhausted iterator.
    --> 800             while self.dispatch_one_batch(iterator):
        801                 self._iterating = True
        802             else:


    /Users/qingkaikong/miniconda2/lib/python2.7/site-packages/joblib/parallel.pyc in dispatch_one_batch(self, iterator)
        651             batch_size = self.batch_size
        652         with self._lock:
    --> 653             tasks = BatchedCalls(itertools.islice(iterator, batch_size))
        654             if not tasks:
        655                 # No more tasks available in the iterator: tell caller to stop.


    /Users/qingkaikong/miniconda2/lib/python2.7/site-packages/joblib/parallel.pyc in __init__(self, iterator_slice)
         66 
         67     def __init__(self, iterator_slice):
    ---> 68         self.items = list(iterator_slice)
         69         self._size = len(self.items)
         70 


    <ipython-input-53-c2a13f8e0fa7> in <genexpr>((i,))
          6     def run(self, num):
          7         results = []
    ----> 8         results = Parallel(n_jobs= -1, backend="threading")            (delayed(self.square_int)(i) for i in num)
          9         print(results)


    /Users/qingkaikong/miniconda2/lib/python2.7/site-packages/joblib/parallel.pyc in delayed(function, check_pickle)
        156     # using with multiprocessing:
        157     if check_pickle:
    --> 158         pickle.dumps(function)
        159 
        160     def delayed_function(*args, **kwargs):


    /Users/qingkaikong/miniconda2/lib/python2.7/copy_reg.pyc in _reduce_ex(self, proto)
         68     else:
         69         if base is self.__class__:
    ---> 70             raise TypeError, "can't pickle %s objects" % base.__name__
         71         state = base(self)
         72     args = (self.__class__, base, state)


    TypeError: can't pickle instancemethod objects


## Solution to the problem

Why we got the above error? 

joblib or Multiprocessing is based on pickling to pass functions around to achieve parallelization. In order to pickle the object, this object must capable of being referred to in the global context for the unpickle to be able to access it. The function we want to parallel above is not in global context, therefore, causing the error.    

Therefore, one solution I found [online](http://www.rueckstiess.net/research/snippets/show/ca1d7d90) is to create a function outside the class to unpack the self from the arguments and calls the function again. Here's the example:  


```python
def unwrap_self(arg, **kwarg):
    return square_class.square_int(*arg, **kwarg)

class square_class:
    def square_int(self, i):
        return i * i
     
    def run(self, num):
        results = []
        results = Parallel(n_jobs= -1, backend="threading")\
            (delayed(unwrap_self)(i) for i in zip([self]*len(num), num))
        print(results)
```


```python
square_int = square_class()
square_int.run(num = range(10))
```

    [0, 1, 4, 9, 16]


We can see from above, by simply write a function outside of the class, we can parallel the method in class as before. You may wonder what we passed to the function, if we print out the argument we passed to unwrap_self function, you will have a better understanding:   


```python
num = range(10)
# note, I use a string "self" here to print it out
print(zip(["self"]*len(num), num))
```

    [('self', 0), ('self', 1), ('self', 2), ('self', 3), ('self', 4), ('self', 5), ('self', 6), ('self', 7), ('self', 8), ('self', 9)]

