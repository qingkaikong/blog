
This week, we will talk about how to debug in the jupyter notebook. From this week, I will also try to use Python3 as much as possible in my code. 

Let's start by showing you some examples:

### Activate debugger after we run the code

The first example is after we have an error occurred, for example, we have a function that squares the input number, but:


```python
def square_number(x):
    
    sq = x**2
    sq += x
    
    return sq
```


```python
square_number('10')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-2-e429f5113bd2> in <module>()
    ----> 1 square_number('10')
    

    <ipython-input-1-822cf3bc7b4e> in square_number(x)
          1 def square_number(x):
          2 
    ----> 3     sq = x**2
          4     sq += x
          5 


    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'


After we have this error, we could activate the debugger by using the magic command - %debug, which will open an interactive debugger for you. You can type in commands in the debugger to get useful information. 


```python
%debug
```

    ipdb> h
    
    Documented commands (type help <topic>):
    ========================================
    EOF    cl         disable  interact  next    psource  rv         unt   
    a      clear      display  j         p       q        s          until 
    alias  commands   down     jump      pdef    quit     source     up    
    args   condition  enable   l         pdoc    r        step       w     
    b      cont       exit     list      pfile   restart  tbreak     whatis
    break  continue   h        ll        pinfo   return   u          where 
    bt     d          help     longlist  pinfo2  retval   unalias  
    c      debug      ignore   n         pp      run      undisplay
    
    Miscellaneous help topics:
    ==========================
    exec  pdb
    
    ipdb> p x
    '10'
    ipdb> type(x)
    <class 'str'>
    ipdb> p locals()
    {'x': '10'}
    ipdb> q


Here, the magic command '%debug' activate the interactive debugger pdb in the notebook, and you can type to see the value of the variables after the error occurs, like the ones I typed in above. There are some most frequent commands you can type in the pdb, like:

* n(ext) line and run this one
* c(ontinue) running until next breakpoint
* p(rint) print varibles
* l(ist) where you are
* 'Enter' Repeat the previous command
* s(tep) Step into a subroutine
* r(eturn) Return out of a subroutine
* h(elp) h
* q(uit) the debugger

You can find more information about the pdb from [here](https://docs.python.org/3/library/pdb.html)

### Activate debugger before run the code

We could also turn on the debugger before we even run the code:


```python
%pdb on
```

    Automatic pdb calling has been turned ON



```python
square_number('10')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-e429f5113bd2> in <module>()
    ----> 1 square_number('10')
    

    <ipython-input-1-822cf3bc7b4e> in square_number(x)
          1 def square_number(x):
          2 
    ----> 3     sq = x**2
          4     sq += x
          5 


    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

    ipdb> p sq
    *** NameError: name 'sq' is not defined
    ipdb> p x
    '10'
    ipdb> c



```python
# let's turn off the debugger
%pdb off
```

    Automatic pdb calling has been turned OFF


## Add a breakpoint

Sometimes we want to add breakpoints to the code


```python
import pdb
```


```python
def square_number(x):
    
    sq = x**2
    
    # we add a breakpoint here
    pdb.set_trace()
    
    sq += x
    
    return sq
```


```python
square_number(3)
```

    > <ipython-input-8-4d6192d84091>(8)square_number()
    -> sq += x
    (Pdb) l
      3  	    sq = x**2
      4  	
      5  	    # we add a breakpoint here
      6  	    pdb.set_trace()
      7  	
      8  ->	    sq += x
      9  	
     10  	    return sq
    [EOF]
    (Pdb) p x
    3
    (Pdb) p sq
    9
    (Pdb) c
    12


