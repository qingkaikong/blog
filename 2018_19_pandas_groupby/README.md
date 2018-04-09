
Pandas groupby function is really useful and powerful in many ways. This week, I am going to show some examples of using this groupby functions that I usually use in  my analysis. 


```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-poster')

%matplotlib inline
```

Let's first create a DataFrame, that contains the name, score and round for some games. 


```python
a = ['Qingkai', 'Ironman', 'Batman', 'Qingkai', 'Ironman', 'Qingkai', 'Batman']
b = [3., 4, 2., 4, 5, 1, 2]
c = range(len(a))

d = [[x,y,z] for x,y,z in zip(a,b,c)]

df = pd.DataFrame(d, columns=['name', 'score', 'round'])
df
```

Now I want to calculate the mean scores for different users across all the games and the standard deviations. It could be quite simple with Pandas. As I am showing below:


```python
df.groupby('name').mean()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>score</th>
      <th>round</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Batman</th>
      <td>2.000000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>Ironman</th>
      <td>4.500000</td>
      <td>2.500000</td>
    </tr>
    <tr>
      <th>Qingkai</th>
      <td>2.666667</td>
      <td>2.666667</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby('name').std()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>score</th>
      <th>round</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Batman</th>
      <td>0.000000</td>
      <td>2.828427</td>
    </tr>
    <tr>
      <th>Ironman</th>
      <td>0.707107</td>
      <td>2.121320</td>
    </tr>
    <tr>
      <th>Qingkai</th>
      <td>1.527525</td>
      <td>2.516611</td>
    </tr>
  </tbody>
</table>
</div>



Or I can loop through the groupby object once to calculate them all. 


```python
for ix, grp in df.groupby('name'):
    print('Name: %s, mean: %.1f, std: %.1f'%(ix, grp['score'].mean(), grp['score'].std()))
```

    Name: Batman, mean: 2.0, std: 0.0
    Name: Ironman, mean: 4.5, std: 0.7
    Name: Qingkai, mean: 2.7, std: 1.5


But also, we could do it with one liner using the agg function:


```python
df.groupby('name').agg({'score':['mean','std'],'round':'count'})
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">score</th>
      <th>round</th>
    </tr>
    <tr>
      <th></th>
      <th>mean</th>
      <th>std</th>
      <th>count</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Batman</th>
      <td>2.000000</td>
      <td>0.000000</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Ironman</th>
      <td>4.500000</td>
      <td>0.707107</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Qingkai</th>
      <td>2.666667</td>
      <td>1.527525</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



Besides, you can also use some customized functions in the agg as well. For example, if we want to calculate the RMS value of the score, we could do the following:


```python
def cal_RMS(x):
    return np.sqrt(sum(x**2/len(x)))
```


```python
df.groupby('name').agg({'score':['mean',cal_RMS],'round':'count'})
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">score</th>
      <th>round</th>
    </tr>
    <tr>
      <th></th>
      <th>mean</th>
      <th>cal_RMS</th>
      <th>count</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Batman</th>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Ironman</th>
      <td>4.500000</td>
      <td>4.527693</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Qingkai</th>
      <td>2.666667</td>
      <td>2.943920</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>


