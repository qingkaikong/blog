Recently, I am trying to experiment some deep learning models on my Macbook. I want to enable the GPU support on my Macbook Pro, since it can train the model faster. I am currently using [Keras](https://keras.io/) on top of [Theano](http://deeplearning.net/software/theano/) backend.  Here I document how I did it, hope it will also useful for you.  

### First check the specification

This is the Graphics on my Macbook Pro (Mid 2014 model), with OS X Yosemite 10.10.5. This step is mainly for you to get a sense what food you have before cooking \^)^ You can find the information from 'System Preferences' or using the following command to find it out. For this purpose, **NVIDIA GeForce GT 750M** is what I am looking for. 

```bash
$system_profiler | grep -A35 Graphics/Displays
Graphics/Displays:

    Intel Iris Pro:

      Chipset Model: Intel Iris Pro
      Type: GPU
      Bus: Built-In
      VRAM (Dynamic, Max): 1536 MB
      Vendor: Intel (0x8086)
      Device ID: 0x0d26
      Revision ID: 0x0008
      gMux Version: 4.0.8 [3.2.8]

    NVIDIA GeForce GT 750M:

      Chipset Model: NVIDIA GeForce GT 750M
      Type: GPU
      Bus: PCIe
      PCIe Lane Width: x8
      VRAM (Total): 2048 MB
      Vendor: NVIDIA (0x10de)
      Device ID: 0x0fe9
      Revision ID: 0x00a2
      ROM Revision: 3776
      gMux Version: 4.0.8 [3.2.8]
```

### Install CUDA 

CUDA is a parallel computing platform and application programming interface model created by Nvidia. To enable the capability on Mac, we need install the driver and toolkit from [NVIDIA](https://developer.nvidia.com/cuda-downloads). Do download the one corresponding to your operating system. At the time of writing, my Macbook Pro is running 10.10.5 which is an older version of operating system, therefore, I need to download the corresponding CUDA from the [Archive](https://developer.nvidia.com/cuda-75-downloads-archive). 

After installing the correct version of CUDA, we can verify the install by run some samples.  


```bash
$cd /usr/local/cuda/samples
$sudo make -C 1_Utilities/deviceQuery
$./bin/x86_64/darwin/release/deviceQuery

## output
./bin/x86_64/darwin/release/deviceQuery Starting...

 CUDA Device Query (Runtime API) version (CUDART static linking)

Detected 1 CUDA Capable device(s)

Device 0: "GeForce GT 750M"
  CUDA Driver Version / Runtime Version          7.5 / 7.5
  CUDA Capability Major/Minor version number:    3.0
  Total amount of global memory:                 2048 MBytes (2147024896 bytes)
  ( 2) Multiprocessors, (192) CUDA Cores/MP:     384 CUDA Cores
  GPU Max Clock rate:                            926 MHz (0.93 GHz)
  Memory Clock rate:                             2508 Mhz
  Memory Bus Width:                              128-bit
  L2 Cache Size:                                 262144 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(65536), 2D=(65536, 65536), 3D=(4096, 4096, 4096)
  Maximum Layered 1D Texture Size, (num) layers  1D=(16384), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(16384, 16384), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 1 copy engine(s)
  Run time limit on kernels:                     Yes
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Disabled
  Device supports Unified Addressing (UVA):      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 1 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 7.5, CUDA Runtime Version = 7.5, NumDevs = 1, Device0 = GeForce GT 750M
Result = PASS
```

If you see the output as mine, that means you successfully installed it. (Note that, if you choose the wrong version, you will likely have problems, especially if you install cuda directly from brew using 'brew cask info cuda', be sure which version you installed). 

### Install NVIDIA's cuDNN library

NVIDIA cuDNN is a GPU-accelerated library of primitives for deep neural networks. NVIDIA requires you to sign up to download packages, therefore, first sign up here:   
https://developer.nvidia.com/accelerated-computing-developer

Download cuDNN (choose the one corresponding to your cuda version):  
https://developer.nvidia.com/cudnn

```bash
$tar zxvf ~/Downloads/cudnn-7.5-osx-x64-v6.0tgz
$sudo cp ./cuda/include/cudnn.h /usr/local/cuda/include/
$sudo cp ./cuda/lib/libcudnn* /usr/local/cuda/lib/
```

Add the following library path to the bottom of .bashrc or .bash_profile file:

```bash
export PATH=/usr/local/cuda/bin:$PATH  
export DYLD_LIBRARY_PATH="/usr/local/cuda/lib":$DYLD_LIBRARY_PATH
```

### Install pygpu

The last step to enable GPU on your mac is to install pygpu. Using conda to install it and all the dependencies. 

```bash
$conda install pygpu
```

### Config Theano to use GPU

Add the following to your .theanorc config file in home directory (vi ~/.theanorc), device = cuda is telling theano to use GPU instead of CPU. 

```shell
[global]
device = cuda
floatX = float32
```

### Test

All right, now we should be able to use GPU on Macbook Pro. Let's do a simple test. In a terminal, open ipython, and import theano, you should see something similar to the following. (Don't worry about the warning, it is just saying I am using a higher version of cuDNN than 5.1). 

```ipython
In [1]: import theano
/Users/qingkaikong/miniconda2/lib/python2.7/site-packages/theano/gpuarray/dnn.py:135: UserWarning: Your cuDNN version is more recent than Theano. If you encounter problems, try updating Theano or downgrading cuDNN to version 5.1.
  warnings.warn("Your cuDNN version is more recent than "
Using cuDNN version 6020 on context None
Mapped name None to device cuda: GeForce GT 750M (0000:01:00.0)

```

### Let's see the speed gain

Let's run the imdb_cnn.py from the examples in the [keras repo](https://github.com/fchollet/keras/tree/master/examples). You can use the THEANO\_FLAGS=device=cpu or THEANO\_FLAGS=device=cuda0 to control running with cpu or gpu in the command line. 

**CPU version**  

```bash
$THEANO_FLAGS=device=cpu python imdb_cnn.py 
## Output
Using Theano backend.
Loading data...
25000 train sequences
25000 test sequences
Pad sequences (samples x time)
x_train shape: (25000, 400)
x_test shape: (25000, 400)
Build model...
Train on 25000 samples, validate on 25000 samples
Epoch 1/2
25000/25000 [==============================] - 148s - loss: 0.4157 - acc: 0.7978 - val_loss: 0.2956 - val_acc: 0.8768
Epoch 2/2
25000/25000 [==============================] - 149s - loss: 0.2483 - acc: 0.9000 - val_loss: 0.2773 - val_acc: 0.8857
```

**GPU version**

```bash
$THEANO_FLAGS=device=cuda0 python imdb_cnn.py 
## Output
Using Theano backend.
/Users/qingkaikong/miniconda2/lib/python2.7/site-packages/theano/gpuarray/dnn.py:135: UserWarning: Your cuDNN version is more recent than Theano. If you encounter problems, try updating Theano or downgrading cuDNN to version 5.1.
  warnings.warn("Your cuDNN version is more recent than "
Using cuDNN version 6020 on context None
^[bMapped name None to device cuda0: GeForce GT 750M (0000:01:00.0)
Loading data...
25000 train sequences
25000 test sequences
Pad sequences (samples x time)
x_train shape: (25000, 400)
x_test shape: (25000, 400)
Build model...
Train on 25000 samples, validate on 25000 samples
Epoch 1/2
25000/25000 [==============================] - 58s - loss: 0.4164 - acc: 0.7956 - val_loss: 0.2969 - val_acc: 0.8752
Epoch 2/2
25000/25000 [==============================] - 56s - loss: 0.2488 - acc: 0.8987 - val_loss: 0.2852 - val_acc: 0.8823
```

### Conclusion

We can see the GPU version is about 3 times faster than the CPU version on my Macbook Pro, which is a little disappointed (I was expecting more speed up when training deep learning model on GPU). I tested on a different dataset with a much deeper structure, it seems the gain is about the same, 3 times faster. It is better than nothing \^)^

### Why GPU is faster than CPU (in some cases)

GPUs is best for data parallel tasks which means that it maybe possible to make an algorithm run faster on a GPU if you can run the same computations on different pieces of data. GPUs are built on SIMD (Single Instruction Multiple Data) architecture. This means each streaming multiprocessor (SMP) (each GPU has multiple SMPs) can execute only one instruction on all the threads at a time but on potentially different data. 

This means GPUs are much faster for some tasks, such as graphics processing, linear algebra, video encoding, Monte Carlo Simulation, multiplying matrices for a machine learning algorithm, or powering a database. 

But GPUs get their speed for a cost. Usually, a single GPU core is much slower than a single CPU core to execute one instruction. But GPU has several cores (up to 16) each operating in a 32-wide SIMD mode (this is 16 * 32 = 496), which can execute the same instruction on about 500 pieces of data. In contrast, common CPUs only have up to 4 or 8 cores, and can operate in 4-wide SIMD which gives much lower parallelism. Even though GPUs can do more operations at a time, but it takes longer time than a CPU to execute the same instruction. The speed gain only comes from this same instruction is applied on multiple data at the same time. Therefore, if you have sequential tasks, CPU would be a better choice than GPUs. 

Computations on GPUs involve an additional overhead as compared to CPUs in the data copy required from the main memory to GPU memory before any computation can be done. Thus it needs to be evaluated if data copy would not make the GPU implementation slower than the actual CPU implementation.

### What Can be Accelerated on the GPU ([ref](http://deeplearning.net/software/theano/tutorial/using_gpu.html#what-can-be-accelerated-on-the-gpu))
The performance characteristics will of course vary from device to device, and also as we refine our implementation:

* In general, matrix multiplication, convolution, and large element-wise operations can be accelerated a lot (5-50x) when arguments are large enough to keep 30 processors busy.
* Indexing, dimension-shuffling and constant-time reshaping will be equally fast on GPU as on CPU.
* Summation over rows/columns of tensors can be a little slower on the GPU than on the CPU.
* Copying of large quantities of data to and from a device is relatively slow, and often cancels most of the advantage of one or two accelerated functions on that data. Getting GPU performance largely hinges on making data transfer to the device pay off.

#### References 

I thank the authors from the following links. Note that for the first two links, they are using tensorflow directly and I am using keras on top of Theano.   
   
https://gist.github.com/Mistobaan/dd32287eeb6859c6668d   
https://gist.github.com/ageitgey/819a51afa4613649bd18    
http://deeplearning.net/software/theano/install_macos.html
http://deeplearning.net/software/theano/tutorial/using_gpu.html

The following references are for why GPUs faster   
http://stackoverflow.com/questions/6435428/why-are-gpus-more-powerful-than-cpus  
https://www.quora.com/Why-are-GPUs-more-powerful-than-CPUs   
https://www.quora.com/Why-does-a-GPU-perform-certain-calculations-faster-than-a-CPU   


