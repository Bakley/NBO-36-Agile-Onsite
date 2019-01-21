# NBO-36-Agile-Onsite
Agile Group Project

# Setting up your system

Make sure you already have Python3, Pip and Virtualenv installed in your system.

# How to get started

Start by making a directory where we will work on. Simply Open your terminal and then:

```
mkdir NBO-36-AGILE-ONSITE
```

Afterwhich we go into the directory:

```
cd NBO-36-AGILE-ONSITE
```

Then git clone the project into your directory

```
https://github.com/Bakley/NBO-36-Agile-Onsite.git .
```

## Create a Python Virtual Environment for our Project

Since we are using Python 3, create a virtual environment by typing:

```
virtualenv -p python3 venv
```

Before we install our project's Python requirements, we need to activate the virtual environment. You can do that by typing:

```
source venv/bin/activate
```

We add the packages to the requirements file.

```
pip freeze > requirements.txt
```