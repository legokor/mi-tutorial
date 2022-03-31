# mi-tutorial
##Generate SSH-key
1. Open Git-Bash
2. Paste the text below, substituting in your GitHub email address
		`$ ssh-keygen -t ed25519 -C "your_email@example.com"`

3. When you're prompted to "Enter a file in which to save the key," press Enter. This accepts the default file location.
		`> Enter a file in which to save the key (/c/Users/you/.ssh/id_algorithm):[Press enter]`
		
4. At the prompt, type a secure passphrase.(can be left empty)
		```> Enter passphrase (empty for no passphrase): [Type a passphrase]
		> Enter same passphrase again: [Type passphrase again]```
		
##Adding your SSH key to the ssh-agent
1. Ensure the ssh-agent is running
		```$ eval "$(ssh-agent -s)"
			> Agent pid 59566```

2. Add your SSH private key to the ssh-agent. If you created your key with a different name, or if you are adding an existing key that has a different name, replace id_ed25519 in the command with the name of your private key file.
		`$ ssh-add ~/.ssh/id_ed25519`