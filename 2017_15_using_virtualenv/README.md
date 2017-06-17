Many times, we find ourselves need to use some of the python packages that we don't want to install in our system or certain version. For example, with pandas updated to version 0.20.2, but you find out you have some old codes depend on the version 0.19.2. In this situation, using a virtual environment to manage it will be really handy. Or you find some cool python packages online, but they require Python 3 instead of 2. This week, I will write here what I usually do in these situations. 

## Using Virtualenv

I usually use [virtualenv](https://virtualenv.pypa.io/en/stable/) to create an environment that isolated from my main python environment. As we mentioned in one situation, I have pandas version 0.20.2 installed in my python environment, but I want to use pandas version 0.19.2 in some of my old scripts.

```bash
# if you don't have virtualenv, you need to install it first
$ pip install virtualenv
# enter into your project folder
$ cd path_to_old_project/
# create the virtual environment
$ virtualenv venv
# activate the virtual environment
$ source venv/bin/activate

# after the activation, we should see a (venv) at the beginning of 
# the terminal prompt indicating that we are working inside the 
# virtual environment now. 

# install the old package I need, i.e. pandas 0.19.2
$ pip install pandas==0.19.2
```

When I work in my virtual environment, I usually add venv to my project's .gitignore file in case I accidentally commit all the virtual environment. 

After working in the virtual environment, to leave it:

```bash
$ deactivate
```

## Using Python 3 to create virtual environment

If you are using Python 3, things will be easier, since you can create the virtual environment directly, for example: python3 -m venv /path/to/new/virtual/environment

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

## Managing Python 2 and 3 on MAC using conda

Sometimes, we want to have both Python 2 and 3 on our machine. Since I am using conda as the package manager, I also use it to manage different environments. On default, I am using Python 2.7, and I usually create and activate Python 3 environment [this way](https://conda.io/docs/py2or3.html):

```bash
# create an environment that have Python 3 installed
$ conda create -n py3 python=3
# start the Python 3 environment
$ source activate py3
# You can use the following to check different environment
$ conda info -e
```

## Create Python 3 environment using Virtualenv

The other way is to use Virtualenv to create a Python 3 environment. 

```bash
$ virtualenv -p python3 env
$ source ./env/bin/activate
```

