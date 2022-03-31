# Lego MI Tutorial

## SSH key

### Generate SSH-key
1. Open Git-Bash
2. Paste the text below, substituting in your GitHub email address

	`$ ssh-keygen -t ed25519 -C "your_email@example.com"`

3. When you're prompted to "Enter a file in which to save the key," press Enter. This accepts the default file location.

	`> Enter a file in which to save the key (/c/Users/you/.ssh/id_algorithm):[Press enter]`
		
4. At the prompt, type a secure passphrase.(can be left empty)

	`> Enter passphrase (empty for no passphrase): [Type a passphrase]`

	`> Enter same passphrase again: [Type passphrase again]`
		
### Adding your SSH key to the ssh-agent
1. Ensure the ssh-agent is running

	`$ eval "$(ssh-agent -s)"`

	`> Agent pid 59566`

2. Add your SSH private key to the ssh-agent. If you created your key with a different name, or if you are adding an existing key that has a different name, replace id_ed25519 in the command with the name of your private key file.
		
	`$ ssh-add ~/.ssh/id_ed25519`
		
### Adding the SSH key to your account on GitHub
1. Go to your github settings. Click on your icon->settings
2. Go to Access/ SSH and GPG keys
3. Get your public key from git bash.(copy all of it)

	`cat ~/.ssh/id_ed25519`

4. Add the public key to your account with new SSH key



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
