# Lego MI Tutorial

## Markdown tutorial
Line one
line 2  
line 3

### asdasd

###### asd

- asd
- asd
- qwe

1. asd
2. qwe

*italic* 

**bold**

__bold__

[link](legokor.hu)

Ez egy kod `asd` asd.

```python
print()
```

```bash
ls
```

## Setup a Python project


### Create environment

```sh
conda create -n mi-tutorial python=3.9
conda activate mi-tutorial

pip install -e .
pip install -r requirements.txt
```

TODO: requirements.txt example

### Gitignore
`.gitignore`
Gitignore template
Exceptions
Embedded .gitignore


### Project structure

```
src
    some_features
        __init__.py
        feature.py
    utils
        __init__.py
        utils.py
```

TODO describe:

`src` folder:  
`some_features` folder:  
`__init__.py`:  
`some_features/feature.py`:  



### Best practices

- Write in .py files instead notebooks
- %load_ext autoreload %autoreload 2
- %%bash like commands
- pre-commit hook
- linting
- flake8, black, isort, mypy