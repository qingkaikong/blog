
This week, we will briefly talk about [kernel density estimation](https://en.wikipedia.org/wiki/Kernel_density_estimation), which is a useful way to estimate the probability density function of a random variable. The idea is quite simple, let's start by showing you example of density estimation using a gaussian kernel for 1D case. 


```python
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

%matplotlib inline
```

### Generate a random 1D dataset

We first generate a bi-modal distribution using two gaussians. 


```python
np.random.seed(12)
X = np.concatenate((np.random.normal(loc = -5, scale= 2, size = 100), np.random.normal(loc = 10, scale= 3, size = 100)))
# let's shuffle the order of the data (this is most for the animation later)
np.random.shuffle(X)

plt.figure(figsize = (10,8))
plt.hist(X, bins = 15, normed=True)
plt.plot(X, np.zeros(len(X)), '*k')
plt.ylim((-0.01, 0.1))
plt.xlabel('Values')
plt.ylabel('Frequencies')
plt.show()
```


![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_25_kernel_density_estimation/figures/Kernel_density_estimation_3_0.png)


### Define gaussian kernels

We define the gaussian kernels as the following function, and we generate a grid and plot a example of gaussian kernel centered at 5. 


```python
def gaussian_kernel(x, mu, sigma):
    return 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 / (2 * sigma**2) )

# generate grid
min_v = np.min(X)
max_v = np.max(X)
grid = np.linspace(min_v, max_v, 100)

# plot out the example
plt.figure(figsize = (10,8))
plt.plot(grid, gaussian_kernel(grid, mu = 5, sigma = 1.0))
plt.title('Example of a kernel centered at 5')
plt.show()
```


![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_25_kernel_density_estimation/figures/Kernel_density_estimation_5_0.png)


### Estimate the density using the kernels

The kernel density estimation is actually very simple, you can think that for each data point, we will center a gaussian kernel at it, and then we just sum all the kernels, we will have the kernel density estimation. The following is an animation that shows this process, we add one kernel at a time (the grey curves), the red curve is our density estimation that sum up all the grey curves. Note that, the width of the kernel has an effect of the smoothness of the density estimation, see the following example. 


```python
density_estimation = np.zeros(len(grid))

FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Kernel density estimation', artist='Qingkai Kong',
                comment='This is for gaussian kernels')
writer = FFMpegWriter(fps=10, metadata=metadata)
fig = plt.figure(figsize = (10,8))

line1, = plt.plot(grid, density_estimation, 'r-', label = 'Sum of all kernels')
plt.ylim(-0.01, 0.1)
plt.legend()
plt.xlabel('Values')
plt.ylabel('Density')

with writer.saving(fig, "Kernel_density_estimation.mp4", 100):

    for x in X:
        plt.plot(x, 0, '*k')

        kernel = gaussian_kernel(grid, mu = x, sigma = 1.0)
        density_estimation += kernel / len(X)
        plt.plot(grid, kernel / 8, 'k', alpha = 0.1)
        line1.set_data(grid, density_estimation)
        
        writer.grab_frame()
```


![gif](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_25_kernel_density_estimation/figures/Kernel_density_estimation.gif)


Let's see the effect on the density estimation using a wider kernel. 

![gif](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_25_kernel_density_estimation/figures/Kernel_density_estimation_2.gif)

## Kernel density estimation using Scipy

The above code is just to show you the basic idea of the kernel density estimation. In reality, we don't need to write the code by ourselves, we could use the existing packages, either scipy or sklearn. Here we show the example using scipy. We could see that the derived density estimation is very similar to what we got above. 


```python
from scipy import stats
```


```python
kernel = stats.gaussian_kde(X, 0.1)
plt.figure(figsize = (10,8))
plt.plot(grid,kernel.evaluate(grid), 'r-')
plt.xlabel('Values')
plt.ylabel('Density')
plt.show()
```


![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_25_kernel_density_estimation/figures/Kernel_density_estimation_11_0.png)


### 2D density estimation

Besides, we could expand this density estimation into 2 dimensions. The idea is still the same, instead of using the 1D gaussian kernel to add up to the density estimation, now we use the 2D gaussian kernels to do the estimation. Let's see the example using scipy for this 2D case. 


```python
# generate data
np.random.seed(12)
X = np.concatenate((np.random.normal(loc = -5, scale= 2, size = (100,2)), np.random.normal(loc = 10, scale= 3, size = (100,2))))

# get the mesh
m1, m2 = X[:, 0], X[:, 1]
xmin = m1.min()
xmax = m1.max()
ymin = m2.min()
ymax = m2.max()

# get the density estimation 
X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
positions = np.vstack([X.ravel(), Y.ravel()])
values = np.vstack([m1, m2])
kernel = stats.gaussian_kde(values)
Z = np.reshape(kernel(positions).T, X.shape)

# plot the result

fig, ax = plt.subplots(figsize = (10,8))

plt.imshow(np.rot90(Z), cmap=plt.cm.jet,
           extent=[xmin, xmax, ymin, ymax])

plt.colorbar()
ax.plot(m1, m2, 'k.', markersize=5)
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])
plt.xlabel('X values')
plt.ylabel('y values')
plt.show()
```


![png](https://raw.githubusercontent.com/qingkaikong/blog/master/2018_25_kernel_density_estimation/figures/Kernel_density_estimation_13_0.png)

