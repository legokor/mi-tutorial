# Lego MI Tutorial

## SSH key

Using the SSH protocol, you can connect and authenticate to remote servers and services. With SSH keys, you can connect to GitHub without supplying your username and personal access token at each visit.

### Generating an SSH-key

Paste the following command into Git-Bash and follow the promts.  

```sh
$ ssh-keygen -t ed25519 -C "your_email@example.com"`
```

### Adding your SSH key to the ssh-agent  
1. Ensure the ssh-agent is running.

	```sh 
	$ eval "$(ssh-agent -s)"
	> Agent pid 59566
	```

2. Add your SSH private key to the ssh-agent. 
		
	```sh
	$ ssh-add ~/.ssh/id_ed25519
	```
		
### Adding the SSH key to your account on GitHub
1. Get your public key from git bash(copy all of it).

	```sh
	cat ~/.ssh/id_ed25519
	```
2. Go to your github settings. Go to _Access/ SSH and GPG keys_.
3. Add the public key to your account with _new SSH key_.

### For more indept instructions check out this [link](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).