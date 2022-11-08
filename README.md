# Lego MI Tutorial

This repository and readme.md will guide you through the steps of creating a Python project. We focus on guidelines that are useful for Machine Learning, but should be considered in all other Python projects.

## SSH key

Using the SSH protocol, you can connect and authenticate to remote servers and services. With SSH keys, you can connect to GitHub without supplying your username and personal access token at each visit. SSH keys are preferred over password authentication and are easy to use once set up.

Check out the official [GitHub docs about SSH key generation]https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent.

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


## Setup a Python project


### Create virtual environment

It is recommended to virtual enviroments for your projects so that project dependencies don't get messed up.

There are some popular solutions such as `venv`, `pipenv`, `conda`, and many others. We will cover these later. But for now, stick with `conda`.

Create a conda environment named `mi-tutorial`:
```sh
conda create -n mi-tutorial python=3.9
conda activate mi-tutorial
```

Install all the requirements specified in the `requirements.txt`:
```sh
pip install -r requirements.txt
```

Install our custom package as editable. In this way, we can develop our code in notebooks and `.py` source files in parallel. Our package is easy to use from notebooks without having to deal with path issues.
```sh
pip install -e .
```


## Markdown language

Markdown is the most commonly used language for documenting repositories. This readme.md is also written in Markdown. GitHub automatically generates a preview of the readme.md file from the currently selected folder. Embedded readme files are allowed.

We have collected the most common basic elements of this language.

### Common elements

| Markdown syntax  | Rendered result |
| ----------- | ----------- |
| Simple line | Simple line |
| Line #1\<br><br>Line #2 | Line #1<br>Line #2 |
| Line #1(double space)<br>Line #2 | Line #1<br>Line #2 |
| \# Heading 1 | <h1>Heading 1</h1> |
| \#\# Heading 2 | <h2>Heading 2</h2> |
| \#\#\#\#\#\# Heading 6 | <h6>Heading 6</h6> |
| \*\*bold option #1\*\* | **bold option #1** |
| \_\_bold option #2\_\_ | __bold option #2__ |
| \*itallic option #1\* | *italic option #1* |
| \_italic option #2\_ | _italic option #2_ |
| \\\*\\\*bold\\\*\\\* | \*\*bold\*\* |
| Items:<br>- Item #1<br>- Item #2 | Items <ul><li>Item #1</li><li>Item #2</li></ul>|
| HTML items <br>\<ul><br>\<li>Item #1\</li><br>\<li>Item #2\</li><br>\</ul> | HTML items <ul><li>Item #1</li><li>Item #2</li></ul>|
| \<hr /> | Page #1 <hr /> Page #2|
| \[link](https://legokor.hu/) | [link](https://legokor.hu/) |
| \!\[image_name](images/logo-small.jpg) | ![image_name](images/logo-small.jpg) |
| \<img src="images/logo.jpg" width="100"> | <img src="images/logo.jpg" width="100"> |
| \[link](legokor.hu) | [link](legokor.hu) |
| Inline \`code\` sample | Inline `code` sample |
| \`\`\`python <br>print()<br>\`\`\` | ```print() ``` |
| \`\`\`sh <br>ls<br>\`\`\` | `ls` |


### Others
Others which were hard to show in a table:

-   `Source`  
    \> Block quote  
    `Result`
    > Block quote

-   Code blocks  
    `Source`     
    \`\`\`python  
    print()  
    \`\`\`  
    `Result`
    ```python
    print()
    ```

-   Code blocks in another language  
    `Source`    
    \`\`\`sh  
    ls  
    \`\`\`  
    `Result`
    ```sh
    ls
    ```
-   Horizontal rules  
    `Source`  
    \-\-\-  
    `Result`  
--- 

Check out this more extensive [Syntax guide](https://www.markdownguide.org/basic-syntax/)!
