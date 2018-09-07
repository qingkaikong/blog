
I use [pandas](https://pandas.pydata.org/) a lot for dealing with time series. Especially the function that it could easily slice the time range you want. But recently, I need to slice between two timestamps with milliseconds, then it is not straightforward. It took me some time to figure it out (I didn't find any useful information online). Therefore, I just document it here if you have the same problem. 


```python
import pandas as pd
```

## First generate a dataframe with datetime as the index

Let's first generate a dataframe with datatime as the index and a counter as another column. 


```python
## define the start and end of the time range
t0 = '2018-01-01 00:00:00.000'
t1 = '2018-01-02 00:00:00.000'

## generate the sequence with a step of 100 milliseconds
df_times = pd.date_range(t0, t1, freq = '100L', tz= "UTC")

## put this into a dataframe
df = pd.DataFrame()
df['datetime'] = df_times
df['count'] = range(len(df_times))
df = df.set_index('datetime')
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
    </tr>
    <tr>
      <th>datetime</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2018-01-01 00:00:00+00:00</th>
      <td>0</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:00.100000+00:00</th>
      <td>1</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:00.200000+00:00</th>
      <td>2</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:00.300000+00:00</th>
      <td>3</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:00.400000+00:00</th>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



## Let's slice a time range

We first slice the data between two times. We can see it works well without the milliseconds in the start and end time


```python
df['2018-01-01 00:00:00':'2018-01-01 00:00:01']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
    </tr>
    <tr>
      <th>datetime</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2018-01-01 00:00:00+00:00</th>
      <td>0</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:00.100000+00:00</th>
      <td>1</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:00.200000+00:00</th>
      <td>2</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:00.300000+00:00</th>
      <td>3</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:00.400000+00:00</th>
      <td>4</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:00.500000+00:00</th>
      <td>5</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:00.600000+00:00</th>
      <td>6</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:00.700000+00:00</th>
      <td>7</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:00.800000+00:00</th>
      <td>8</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:00.900000+00:00</th>
      <td>9</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:01+00:00</th>
      <td>10</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:01.100000+00:00</th>
      <td>11</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:01.200000+00:00</th>
      <td>12</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:01.300000+00:00</th>
      <td>13</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:01.400000+00:00</th>
      <td>14</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:01.500000+00:00</th>
      <td>15</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:01.600000+00:00</th>
      <td>16</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:01.700000+00:00</th>
      <td>17</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:01.800000+00:00</th>
      <td>18</td>
    </tr>
    <tr>
      <th>2018-01-01 00:00:01.900000+00:00</th>
      <td>19</td>
    </tr>
  </tbody>
</table>
</div>



What if I want to slice two times with milliseconds as the following, we could see that we experience an error that has no information to help us to identify what happened. 


```python
df['2018-01-01 00:00:00.500':'2018-01-01 00:00:01.200']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    ~/miniconda2/envs/python3/lib/python3.6/site-packages/pandas/core/indexes/datetimes.py in slice_indexer(self, start, end, step, kind)
       1527         try:
    -> 1528             return Index.slice_indexer(self, start, end, step, kind=kind)
       1529         except KeyError:


    ~/miniconda2/envs/python3/lib/python3.6/site-packages/pandas/core/indexes/base.py in slice_indexer(self, start, end, step, kind)
       3456         start_slice, end_slice = self.slice_locs(start, end, step=step,
    -> 3457                                                  kind=kind)
       3458 


    ~/miniconda2/envs/python3/lib/python3.6/site-packages/pandas/core/indexes/base.py in slice_locs(self, start, end, step, kind)
       3657         if start is not None:
    -> 3658             start_slice = self.get_slice_bound(start, 'left', kind)
       3659         if start_slice is None:


    ~/miniconda2/envs/python3/lib/python3.6/site-packages/pandas/core/indexes/base.py in get_slice_bound(self, label, side, kind)
       3583         # to datetime boundary according to its resolution.
    -> 3584         label = self._maybe_cast_slice_bound(label, side, kind)
       3585 


    ~/miniconda2/envs/python3/lib/python3.6/site-packages/pandas/core/indexes/datetimes.py in _maybe_cast_slice_bound(self, label, side, kind)
       1480             _, parsed, reso = parse_time_string(label, freq)
    -> 1481             lower, upper = self._parsed_string_to_bounds(reso, parsed)
       1482             # lower, upper form the half-open interval:


    ~/miniconda2/envs/python3/lib/python3.6/site-packages/pandas/core/indexes/datetimes.py in _parsed_string_to_bounds(self, reso, parsed)
       1317         else:
    -> 1318             raise KeyError
       1319 


    KeyError: 

    
    During handling of the above exception, another exception occurred:


    KeyError                                  Traceback (most recent call last)

    <ipython-input-4-803941334466> in <module>()
    ----> 1 df['2018-01-01 00:00:00.500':'2018-01-01 00:00:01.200']
    

    ~/miniconda2/envs/python3/lib/python3.6/site-packages/pandas/core/frame.py in __getitem__(self, key)
       2125 
       2126         # see if we can slice the rows
    -> 2127         indexer = convert_to_index_sliceable(self, key)
       2128         if indexer is not None:
       2129             return self._getitem_slice(indexer)


    ~/miniconda2/envs/python3/lib/python3.6/site-packages/pandas/core/indexing.py in convert_to_index_sliceable(obj, key)
       1978     idx = obj.index
       1979     if isinstance(key, slice):
    -> 1980         return idx._convert_slice_indexer(key, kind='getitem')
       1981 
       1982     elif isinstance(key, compat.string_types):


    ~/miniconda2/envs/python3/lib/python3.6/site-packages/pandas/core/indexes/base.py in _convert_slice_indexer(self, key, kind)
       1462         else:
       1463             try:
    -> 1464                 indexer = self.slice_indexer(start, stop, step, kind=kind)
       1465             except Exception:
       1466                 if is_index_slice:


    ~/miniconda2/envs/python3/lib/python3.6/site-packages/pandas/core/indexes/datetimes.py in slice_indexer(self, start, end, step, kind)
       1536                 if start is not None:
       1537                     start_casted = self._maybe_cast_slice_bound(
    -> 1538                         start, 'left', kind)
       1539                     mask = start_casted <= self
       1540 


    ~/miniconda2/envs/python3/lib/python3.6/site-packages/pandas/core/indexes/datetimes.py in _maybe_cast_slice_bound(self, label, side, kind)
       1479                            getattr(self, 'inferred_freq', None))
       1480             _, parsed, reso = parse_time_string(label, freq)
    -> 1481             lower, upper = self._parsed_string_to_bounds(reso, parsed)
       1482             # lower, upper form the half-open interval:
       1483             #   [parsed, parsed + 1 freq)


    ~/miniconda2/envs/python3/lib/python3.6/site-packages/pandas/core/indexes/datetimes.py in _parsed_string_to_bounds(self, reso, parsed)
       1316             return (Timestamp(st, tz=self.tz), Timestamp(st, tz=self.tz))
       1317         else:
    -> 1318             raise KeyError
       1319 
       1320     def _partial_date_slice(self, reso, parsed, use_lhs=True, use_rhs=True):


    KeyError: 


## The solution

I found out an easy solution to the problem, instead of directly slice the data, we first find the index that meets our requirements, and then use the index to find the data as shown below:


```python
ix = (df.index >= '2018-01-01 00:00:00.500') & (df.index <='2018-01-01 00:00:01.200')
df[ix]
```
