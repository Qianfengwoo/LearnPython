# TensorFlow的安装教程

```Python
系统：deepin 15.3桌面版
版本：Python 2.7
```
> TensorFlow is an open source software library for machine learning in various kinds of perceptual and language understanding tasks.
  It is currently used for both research and production by 50 different teams in dozens of commercial Google products, such as speech 
  recognition, Gmail, Google Photos, and search, many of which had previously used its predecessor DistBelief. TensorFlow was originally
  developed by the Google Brain team for Google's research and production purposes and later released under the Apache 2.0 open source 
  license on November 9, 2015


TensorFlow同时支持Python2.7 和 Python 3.5+，其安装方式也很多，我的电脑上原先安装有anaconda2，下面用Anaconda install的方式来安装：

同Virtualenv建立虚拟的独立环境一样，conda 也可以建立一个虚拟的环境，在安装TensorFlow时，其所需要的依赖也不会覆盖掉已经存在的符合anaconda的依赖。

- 安装 Anaconda
- 创建 Anaconda environment
- 激活Anaconda environment 环境并安装TensorFlow
- 完成

## Create a conda environment called tensorflow:

```Python
$ conda create -n tensorflow python=2.7
```
## Using conda

A community maintained conda package is available from conda-forge.

Only the CPU version of TensorFlow is available at the moment and can be installed in the conda environment for Python 2 or Python 3.


```Python

$ source activate tensorflow
(tensorflow)$ 

# Linux/Mac OS X, Python 2.7/3.4/3.5, CPU only:
(tensorflow)$ conda install -c conda-forge tensorflow

```
## Using pip
If using pip make sure to use the --ignore-installed flag to prevent errors about easy_install.

```Python
$ source activate tensorflow
(tensorflow)$ 
```
然后，选择合适的版本，可以选择只cpu，也可选择GPU加速，这二者并没有什么大的区别，只不过是计算速度的事儿，作为
入门学习，我选择的是cpu版本：
```Python

# Ubuntu/Linux 64-bit, CPU only, Python 2.7
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0-cp27-none-linux_x86_64.whl

```

最后，安装TensorFlow：

```Python

# Python 2
(tensorflow)$ pip install --ignore-installed --upgrade $TF_BINARY_URL

```

收工！
