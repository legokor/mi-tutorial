# SSH key

Using the SSH protocol, you can connect and authenticate to remote servers and services. With SSH keys, you can connect to GitHub without supplying your username and personal access token at each visit. SSH keys are preferred over password authentication and are easy to use once set up.

Check out the official [GitHub docs about SSH key generation]https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent.

## Generate SSH-key
1. Open Git-Bash
2. Paste the text below, substituting in your GitHub email address

	`$ ssh-keygen -t ed25519 -C "your_email@example.com"`

3. When you're prompted to "Enter a file in which to save the key," press Enter. This accepts the default file location.

	`> Enter a file in which to save the key (/c/Users/you/.ssh/id_algorithm):[Press enter]`
		
4. At the prompt, type a secure passphrase.(can be left empty)

	`> Enter passphrase (empty for no passphrase): [Type a passphrase]`

	`> Enter same passphrase again: [Type passphrase again]`
		
## Adding your SSH key to the ssh-agent
1. Ensure the ssh-agent is running

	`$ eval "$(ssh-agent -s)"`

2. Add your SSH private key to the ssh-agent. If you created your key with a different name, or if you are adding an existing key that has a different name, replace id_ed25519 in the command with the name of your private key file.
		
	`$ ssh-add ~/.ssh/id_ed25519`
		
## Adding the SSH key to your account on GitHub
1. Go to your github settings. Click on your icon->settings
2. Go to Access/ SSH and GPG keys
3. Get your public key from git bash.(copy all of it)

	`cat ~/.ssh/id_ed25519`

4. Add the public key to your account with new SSH key
