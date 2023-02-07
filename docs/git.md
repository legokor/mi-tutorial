# Git tutorial

Git is a distributed version control solution.

## Setting up

Before starting with git two fields are to be set
```
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```
Where we set our e-mail address and name used in git.

You can set git repository specific settings by omiting the `--global` flag.

## Terminology

### Branch

Git's version handling can be see as a Directed Non-Circle Free Tree Graph. There can be Points where two path merges. One of these paths is a branch and can have a name and handled uniquely from other branches.

### Commit

A stage of development, which within the git repository is stored as a differentiation file from the previous version.
A commit can have name and connected signature and always has an Id

### Repository

The main containment unit of a project in git. It can contains branches, commits, pull requrests, history.

## Remote vs local

### Local

A repository cloned locally with 
```
git clone <repository-url>
```
Which downloads the data structure to continue development with git on the local machine.

Local branches and commits are useful to contain changes which achieved something, but not necesarry meant to published.

We can create local branches and commits with `git checkout -b <branch-name>`and git commit.

TODO: read from here

### Remote

Git would still be useful if it could only be managed locally, but its real power comes when it has its remote.

In this case, we have a remote repository connected to our locally cloned repository. Usually, this repository is called the origin.

To upload the current state of a branch to remote server, `git push` can be used, if no remote corresponding branch has been set: `$ git push --set-upstream <remote> <branch>`.

You can use `git pull` to download changes from the remote.

`git fetch` can be used to update the local knowledge of the remote state.


## Commit 

Git has tracked and untracked files. Git is only interested in tracked files and tracks their changes. To add a file to be tracked we can use 

```sh
git add <files>
```

To untrack files: 

```sh
git rm --cached <filename>
```

We can also specify files that git doesn't track with `.gitignore`. When a file is placed in a folder, the folder and all subfolders are affected, unless the subfolders have their own `.gitignore`.

[Useful gitignore generator](https://www.toptal.com/developers/gitignore)


If we have changed the source code, we must first add it to the commit with the previously mentioned command.
```sh
git add <files>
```

After all files have been added, it is useful to check if 
- we added all files we need
- did not add files which we do not need

with command:
```
git status
```

If everything is okay we can create a commit with 

```sh
git commit -m "Commit message" -S 
```
Where `-m` argument sets the commit message which should be descriptive. `-S` is used to sign a commit with a key to prove who uploaded it(if you have one it can be useful, but it is not required in most places.

Previously created commits can be reverted with 

```sh
git revert <commitId>
```

And the whole branch set back to a previous state with 

```sh
git reset ~<numberOfCommitsToBeReset>
```

## Stash

Git allows us to save a state of the branch locally, temporally, which can be useful if for example we are not yet ready for committing a change, but have to change task for a short time, or if we want to try a new solution.
To stash away our current non commit changes we can use:

```sh
git stash
```
Or to retrieve them we can use:
```
git stash pop
```
## Branches
We can checkout a branch to work on/start from with 

```
git checkout <branchname>
```

A new local branch from our current position can be created with. To be branched from a specific poitn either we should navigate there iwth checkout or set it with parameters

```
git checkout -b <branchname>
```

Deleted with:

```
git branch -d <branchname>
```

or if there are complications in deletion with 

```
git branch -D <branchname>
```

Pushed to remote with

```
git push
```

If there been resets or rebasing it is needed to use push with `-f` force flag,

```
git push -f
```

A branch can be pulled (updated with remote changes) 

```
git pull
```

## Log

Most IDE has commit log viusalisation, but it can be useful to know how to see which commits. It shows which commits are the last commits of different branches.

## Rebase

If a branch has been alive for a long time rebease from the originator branch could be useful, does teh following:

1. Add all commits which were commited after brnaching on originator to the branch we are on
2. Applyies the commits to over this commits.
 
It can be used to get new changes from the originator branch, which can be useful to have less merge-conflict when merging our Pull Requests

## Pull requests

Pull request are the request to one branches changes to bemerged to an other branch. It is used to keep changes to branches clearly readable.
There can be even be branch protection rules set up for branches wihich are requiring pull request to merge.
Many tool provides possbility to enforce requirement for pull-request to be approved by other developer.

## Merge conflicts

If there has been from the branching point of two branch two different change made to the same part of the code, git is detecting it, and creates a so called merge conflict. It can be resolved manually by editing the file and after all file have been edited commiting the changes, or many useful tools for IDE have been created.

```
<<<<<<< HEAD
this is some content to mess with
content to append
=======
totally different content to merge later
>>>>>>> new_branch_to_merge_later
```

Here is an example a merge conflict. HEAD means the state our current branch is in and it shows  currently the `this is some content to mess with
content to append` has been added, which in in contrast with the branch `new_branch_to_merge_later`'s change of `totally different content to merge later.
**To solve it you must delete the added lines and write/select the line which in the future should be there**
`
## Hooks

In git we can set up hooks which can be used to verify commits content before commit, after pushing to remote. It is many times used for linting, static code analysis, generating reports or even for initiated CI-CD scripts for auto-deploy.

## Squash

There can be situation when locally we had many commits (for example because of many context switches), but we want to push one commit.

For this git's bash command is very helpful. It can be used to create one commit out of many on the same branch (local or remote). 

Usual best practice can be squashing the pull requests code into one commit before merging. (Github provide an easy GUI option for it)

[A tutorial of git squash](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts)
[An other tutorial](http://git-scm.com/docs/git-rebase#_interactive_mode)

## Tools

* gitKraken are stated to be useful.
* Jetbrains integrated git plugin: I personally like it - @martonoravecz
* github bash: basic cli tool, but with every capability
* Github Desktop: could be an easy helper during learning phases. I does provide a more streamlined experienced if everything is according to the plan… I 

Would say it is useful for learning, but you are better off with git bash - @martonoravecz