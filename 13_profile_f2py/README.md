
This example is prepared by [Qingkai Kong](https://github.com/qingkaikong/) (qingkai.kong@gmail.com) from [Berkeley Seismological Lab](http://seismo.berkeley.edu/) for the lightning talk at [The Hacker Within](http://www.thehackerwithin.org/berkeley/) at BIDS on April 6th 2016. 

> The purpose of this script is to show how I usually do to speedup my python script. And hope this is useful to you. 

## Line_profiler

Many times, you find your python script is slow, but you just don't know which part drags the whole performance down. To get an idea, I usually use the [line_profiler](https://github.com/rkern/line_profiler) from Robert Kern, this is really good if you want to identify which line uses more time than you expceted, and how often each line executed. Here's a blog talking about profile python [Marco Bonzanini](http://marcobonzanini.com/2015/01/05/my-python-code-is-slow-tips-for-profiling/)

You can use line_profiler either in command line or in ipython notebook. 

### 1 Command line

In a typical workflow, one only cares about line timings of a few functions because wading through the results of timing every single line of code would be overwhelming. However, LineProfiler does need to be explicitly told what functions to profile. The easiest way to get started is to use the kernprof script.

Steps:
> 
1. in your script, you decorate the functions you want to profile with @profile. For example:
```python
@profile
def function_to_profile(a, b, c):
    ...
```
2. Run the following command in the terminal:
```sh
kernprof -v -l profile_test.py
```


### 2 Run in Ipython notebook

To run line_profiler in the notebook, you need load the extension first, and then use the magic commands %lprun to profile the script. 


```python
%load_ext line_profiler
```


```python
def example_function(myRange):
    # directly convert range to string list
    str_list = []
    for i in myRange:
        str_list.append(str(i))
        
def example_function2(myRange):
    # use list comprehension to convert range to string list
    str_list = [str(i) for i in myRange] 
        
```


```python
%lprun -f example_function example_function(range(1000000))
```


```python
%lprun -f example_function2 example_function2(range(1000000))
```

## Using f2py

f2py - Fortran to Python interface generator, is used to call Fortran 77/90/95 external subroutines and Fortran 90/95 module subroutines as well as C functions. It is part of the Numpy now. You can find more details [here](http://docs.scipy.org/doc/numpy-dev/f2py/). 

Let's grab the example from the above link, and compare a python version and a fortran version for speed. 

### Python version


```python
import numpy as np

def fib(A):
    '''
    CALCULATE FIRST N FIBONACCI NUMBERS
    '''
    n = len(A)
    
    for i in range(n):
        if i == 0:
            A[i] = 0.
        elif i == 1:
            A[i] = 1.
        else:
            A[i] = A[i-1] + A[i-2]
            
    return A
```


```python
dat_in = np.zeros(10) 
dat_out = fib(dat_in)
dat_out
```




    array([  0.,   1.,   1.,   2.,   3.,   5.,   8.,  13.,  21.,  34.])




```python
dat_in = np.zeros(1000) 
```


```python
%lprun -f fib fib(dat_in)
```

### Fortran version

let's first write a simple fortran subroutine


```python
!ls
```

    Profile python script and f2py.ipynb example.py
    README.md



```python
%%writefile fib1.f
C FILE: FIB1.F
      SUBROUTINE FIB(A,N)
C
C     CALCULATE FIRST N FIBONACCI NUMBERS
C
      INTEGER N
      REAL*8 A(N)
      DO I=1,N
         IF (I.EQ.1) THEN
            A(I) = 0.0D0
         ELSEIF (I.EQ.2) THEN
            A(I) = 1.0D0
         ELSE 
            A(I) = A(I-1) + A(I-2)
         ENDIF
      ENDDO
      END
C END FILE FIB1.F
```

    Writing fib1.f



```python
!f2py -c fib1.f -m fib1
```

    [39mrunning build[0m
    [39mrunning config_cc[0m
    [39munifing config_cc, config, build_clib, build_ext, build commands --compiler options[0m
    [39mrunning config_fc[0m
    [39munifing config_fc, config, build_clib, build_ext, build commands --fcompiler options[0m
    [39mrunning build_src[0m
    [39mbuild_src[0m
    [39mbuilding extension "fib1" sources[0m
    [39mf2py options: [][0m
    [39mf2py:> /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fib1module.c[0m
    [39mcreating /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7[0m
    Reading fortran codes...
    	Reading file 'fib1.f' (format:fix,strict)
    Post-processing...
    	Block: fib1
    			Block: fib
    Post-processing (stage 2)...
    Building modules...
    	Building module "fib1"...
    		Constructing wrapper function "fib"...
    		  fib(a,[n])
    	Wrote C/API module "fib1" to file "/var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fib1module.c"
    [39m  adding '/var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fortranobject.c' to sources.[0m
    [39m  adding '/var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7' to include_dirs.[0m
    [39mcopying /Library/Python/2.7/site-packages/numpy/f2py/src/fortranobject.c -> /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7[0m
    [39mcopying /Library/Python/2.7/site-packages/numpy/f2py/src/fortranobject.h -> /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7[0m
    [39mbuild_src: building npy-pkg config files[0m
    [39mrunning build_ext[0m
    [39mcustomize UnixCCompiler[0m
    [39mcustomize UnixCCompiler using build_ext[0m
    [39mcustomize Gnu95FCompiler[0m
    [39mFound executable /usr/local/bin/gfortran[0m
    [39mcustomize Gnu95FCompiler[0m
    [39mcustomize Gnu95FCompiler using build_ext[0m
    [39mbuilding 'fib1' extension[0m
    [39mcompiling C sources[0m
    [39mC compiler: cc -fno-strict-aliasing -fno-common -dynamic -arch x86_64 -arch i386 -g -Os -pipe -fno-common -fno-strict-aliasing -fwrapv -DENABLE_DTRACE -DMACOSX -DNDEBUG -Wall -Wstrict-prototypes -Wshorten-64-to-32 -DNDEBUG -g -fwrapv -Os -Wall -Wstrict-prototypes -DENABLE_DTRACE -arch x86_64 -arch i386 -pipe
    [0m
    [39mcreating /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/var[0m
    [39mcreating /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/var/folders[0m
    [39mcreating /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/var/folders/xh[0m
    [39mcreating /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn[0m
    [39mcreating /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T[0m
    [39mcreating /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ[0m
    [39mcreating /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7[0m
    [39mcompile options: '-I/var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7 -I/Library/Python/2.7/site-packages/numpy/core/include -I/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c'[0m
    [39mcc: /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fib1module.c[0m
    In file included from /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fib1module.c:19:
    In file included from /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fortranobject.h:13:
    In file included from /Library/Python/2.7/site-packages/numpy/core/include/numpy/arrayobject.h:4:
    In file included from /Library/Python/2.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
    In file included from /Library/Python/2.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1777:
    /Library/Python/2.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
    #warning "Using deprecated NumPy API, disable it by " \
     ^
    /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fib1module.c:122:12: warning: implicit conversion loses integer precision: 'npy_intp' (aka 'long') to 'npy_int' (aka 'int') [-Wshorten-64-to-32]
          sz = PyArray_SIZE(var);
             ~ ^~~~~~~~~~~~~~~~~
    /Library/Python/2.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:91:25: note: expanded from macro 'PyArray_SIZE'
    #define PyArray_SIZE(m) PyArray_MultiplyList(PyArray_DIMS(m), PyArray_NDIM(m))
                            ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    /Library/Python/2.7/site-packages/numpy/core/include/numpy/__multiarray_api.h:1029:9: note: expanded from macro 'PyArray_MultiplyList'
            (*(npy_intp (*)(npy_intp *, int)) \
            ^
    /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fib1module.c:128:14: warning: implicit conversion loses integer precision: 'npy_intp' (aka 'long') to 'npy_int' (aka 'int') [-Wshorten-64-to-32]
            sz = PyArray_DIM(var, dim-1);
               ~ ^~~~~~~~~~~~~~~~~~~~~~~
    /Library/Python/2.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1526:29: note: expanded from macro 'PyArray_DIM'
    #define PyArray_DIM(obj,n) (PyArray_DIMS(obj)[n])
                                ^~~~~~~~~~~~~~~~~~~~
    /Library/Python/2.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1524:27: note: expanded from macro 'PyArray_DIMS'
    #define PyArray_DIMS(obj) (((PyArrayObject_fields *)(obj))->dimensions)
                              ^
    /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fib1module.c:144:10: warning: implicit conversion loses integer precision: 'long' to 'int' [-Wshorten-64-to-32]
        *v = PyInt_AS_LONG(tmp);
           ~ ^~~~~~~~~~~~~~~~~~
    /System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7/intobject.h:52:51: note: expanded from macro 'PyInt_AS_LONG'
    #define PyInt_AS_LONG(op) (((PyIntObject *)(op))->ob_ival)
                               ~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
    /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fib1module.c:232:30: warning: implicit conversion loses integer precision: 'npy_intp' (aka 'long') to 'int' [-Wshorten-64-to-32]
      if (n_capi == Py_None) n = len(a); else
                               ~ ^~~~~~
    /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fib1module.c:73:18: note: expanded from macro 'len'
    #define len(var) shape(var,0)
                     ^~~~~~~~~~~~
    /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fib1module.c:69:24: note: expanded from macro 'shape'
    #define shape(var,dim) var ## _Dims[dim]
                           ^~~~~~~~~~~~~~~~~
    <scratch space>:100:1: note: expanded from here
    a_Dims
    ^
    /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fib1module.c:112:12: warning: unused function 'f2py_size' [-Wunused-function]
    static int f2py_size(PyArrayObject* var, ...)
               ^
    6 warnings generated.
    In file included from /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fib1module.c:19:
    In file included from /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fortranobject.h:13:
    In file included from /Library/Python/2.7/site-packages/numpy/core/include/numpy/arrayobject.h:4:
    In file included from /Library/Python/2.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
    In file included from /Library/Python/2.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1777:
    /Library/Python/2.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
    #warning "Using deprecated NumPy API, disable it by " \
     ^
    /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fib1module.c:112:12: warning: unused function 'f2py_size' [-Wunused-function]
    static int f2py_size(PyArrayObject* var, ...)
               ^
    2 warnings generated.
    [39mcc: /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fortranobject.c[0m
    In file included from /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fortranobject.c:2:
    In file included from /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fortranobject.h:13:
    In file included from /Library/Python/2.7/site-packages/numpy/core/include/numpy/arrayobject.h:4:
    In file included from /Library/Python/2.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
    In file included from /Library/Python/2.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1777:
    /Library/Python/2.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
    #warning "Using deprecated NumPy API, disable it by " \
     ^
    /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fortranobject.c:60:73: warning: implicit conversion loses integer precision: 'npy_intp' (aka 'long') to 'int' [-Wshorten-64-to-32]
                                        NPY_STRING, NULL, fp->defs[i].data, fp->defs[i].dims.d[n],
                                                                            ^~~~~~~~~~~~~~~~~~~~~
    2 warnings generated.
    In file included from /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fortranobject.c:2:
    In file included from /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fortranobject.h:13:
    In file included from /Library/Python/2.7/site-packages/numpy/core/include/numpy/arrayobject.h:4:
    In file included from /Library/Python/2.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
    In file included from /Library/Python/2.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1777:
    /Library/Python/2.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
    #warning "Using deprecated NumPy API, disable it by " \
     ^
    1 warning generated.
    [39mcompiling Fortran sources[0m
    [39mFortran f77 compiler: /usr/local/bin/gfortran -Wall -g -ffixed-form -fno-second-underscore -arch x86_64 -fPIC -O3 -funroll-loops
    Fortran f90 compiler: /usr/local/bin/gfortran -Wall -g -fno-second-underscore -arch x86_64 -fPIC -O3 -funroll-loops
    Fortran fix compiler: /usr/local/bin/gfortran -Wall -g -ffixed-form -fno-second-underscore -Wall -g -fno-second-underscore -arch x86_64 -fPIC -O3 -funroll-loops[0m
    [39mcompile options: '-I/var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7 -I/Library/Python/2.7/site-packages/numpy/core/include -I/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c'[0m
    [39mgfortran:f77: fib1.f[0m
    [39m/usr/local/bin/gfortran -Wall -g -arch x86_64 -Wall -g -undefined dynamic_lookup -bundle /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fib1module.o /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/src.macosx-10.10-intel-2.7/fortranobject.o /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ/fib1.o -L/usr/local/Cellar/gcc/5.3.0/lib/gcc/5/gcc/x86_64-apple-darwin14.5.0/5.3.0 -lgfortran -o ./fib1.so[0m
    Removing build directory /var/folders/xh/r5lqt0053l5d6xf9tq49tkgm0000gn/T/tmpKc3cnJ



```python
!ls
```

    Profile python script and f2py.ipynb fib1.f
    README.md                            [31mfib1.so[m[m
    example.py                           [34mfib1.so.dSYM[m[m


You can see it created an python interface fib1.so. Now you can import the function into python.


```python
import fib1
import numpy as np
```


```python
print fib1.fib.__doc__
```

    fib(a,[n])
    
    Wrapper for ``fib``.
    
    Parameters
    ----------
    a : input rank-1 array('d') with bounds (n)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: len(a)
    



```python
a = np.zeros(9)
```


```python
fib1.fib(a)
```


```python
a
```




    array([  0.,   1.,   1.,   2.,   3.,   5.,   8.,  13.,  21.])



Let's compare the time of both function, we can see for this exmaple, the fortran version is about 100 times faster than the python version.


```python
a = np.zeros(1000)
```


```python
%timeit fib1.fib(a)
```

    100000 loops, best of 3: 2.66 µs per loop



```python
%timeit fib(a)
```

    1000 loops, best of 3: 363 µs per loop


## My workflow

When I start some script, I usually use the following workflow to speedup:

1. write python script
2. profile it line by line
3. finding some stupid thing that can be easily fix (I found this many times)
4. parallel the part that used a lot of time
5. use a f2py to take advantage of the fotran speed
