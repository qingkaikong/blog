
We discussed using profiler to profile your code and find out where it is slow in the [previous blog](http://qingkaikong.blogspot.com/2016/01/profile-your-python-code.html), and but you need to run from command line. Today, we will have a look of the profile code in jupyter notebook. Note that, if you haven't installed 'line_profiler', install it first:

```python
pip install line_profiler
```



Let's first define some functions to calculate random things. There are three functions that calling one by one. 


```python
def square_the_value(x, y):
    
    a = add_1000_times(x, y)
    
    return a**2

def add_1000_times(x, y):
    z = 0
    for i in range(1000):
        z += x
        for j in range(1000):
            z += y
        
    return z

def calculate_my_value(x, y):
    
    a = x + y
    b = x - y
    
    print(square_the_value(a, b))
```


```python
calculate_my_value(1, 2)
```

    994009000000


Now we want to have an idea of which part of the code running fast and which part running slow. We could use the line_profiler to do the job. First, we need to load the extension:


```python
%load_ext line_profiler
```

Let's profile the top level function that we run. We can see that we use '%lprun', which basically run the line_profiler, the '-f' flag is to tell it which function or method we want to profile, and the calculate_my_value(1, 2) is the real statement that we want to run:


```python
%lprun -f calculate_my_value calculate_my_value(1, 2)
```

    994009000000



    Timer unit: 1e-06 s
    
    Total time: 0.295409 s
    File: <ipython-input-1-0c3fada21717>
    Function: calculate_my_value at line 16
    
    Line #      Hits         Time  Per Hit   % Time  Line Contents
    ==============================================================
        16                                           def calculate_my_value(x, y):
        17                                               
        18         1          3.0      3.0      0.0      a = x + y
        19         1          1.0      1.0      0.0      b = x - y
        20                                               
        21         1     295405.0 295405.0    100.0      print(square_the_value(a, b))


Now we could see that the line_profiler give us the time to run each line, and what's the percentage of this line takes. We could see that the last line used all the time. We can continue to profile the last time by entering into the square_the_value function:


```python
%lprun -f square_the_value calculate_my_value(1, 2)
```

    994009000000



    Timer unit: 1e-06 s
    
    Total time: 0.39605 s
    File: <ipython-input-1-0c3fada21717>
    Function: square_the_value at line 1
    
    Line #      Hits         Time  Per Hit   % Time  Line Contents
    ==============================================================
         1                                           def square_the_value(x, y):
         2                                               
         3         1     396048.0 396048.0    100.0      a = add_1000_times(x, y)
         4                                               
         5         1          2.0      2.0      0.0      return a**2


Similarly, we could profile the add_1000_times function to figure out which line really takes all the time:


```python
%lprun -f add_1000_times calculate_my_value(1, 2)
```

    994009000000



    Timer unit: 1e-06 s
    
    Total time: 0.829793 s
    File: <ipython-input-1-0c3fada21717>
    Function: add_1000_times at line 7
    
    Line #      Hits         Time  Per Hit   % Time  Line Contents
    ==============================================================
         7                                           def add_1000_times(x, y):
         8         1          1.0      1.0      0.0      z = 0
         9      1001        382.0      0.4      0.0      for i in range(1000):
        10      1000        423.0      0.4      0.1          z += x
        11   1001000     388197.0      0.4     46.8          for j in range(1000):
        12   1000000     440788.0      0.4     53.1              z += y
        13                                                   
        14         1          2.0      2.0      0.0      return z


The profiler is really useful, I use it all the time to optimize my code to remove some of the inefficient code. Hope you will find it useful as well. 
