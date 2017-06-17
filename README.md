# django-demo-site

## Installation

Build specification:

* Python 3.6

### Collaboration

 _*Setting up your remote*_

In this project we make use of git's awesome multiple remote functionality.  Everyone working on the project will need to fork the repository and then set up the following:

First run:

`git remote -v`

This will show you all the existing remotes you have set up for your fork (should just be origin right now).

Then run:

`git remote add canonical https://github.com/hackingagainstslavery/django-demo-site.git`

The reason we call the main branch canonical is because it is the canonical source code for the repository.

Now run:

`git remote -v` again.

You should see two more remotes.

For more information on this go checkout [https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes).

 _* Pulling in changes *_

Once you have your remote's all set up, you can pull down changes, periodically from the canonical source.  It's probably best to switch to your local master branch and pull changes into there, rather than pulling any changes into any open pull requests or tickets you may be working on.

To pull in changes from the canonical, it's best to do the following:

`git fetch canonical` - this will fetch any new branches or tags that have been added.  This is kind of like the meta data about the repo, rather than anything specific.

`git pull canonical master` - this will pull down any changes from the canonical master into your master.  You probably shouldn't pull in from another branch, as master is the only place that change should _ever_ be happening on canonical.  That's right, there is no dev branch here.  This way, we know that the branch on the canonical is authoritative at any given moment. If you are trying to push to dev, that's where you're local dev branch comes in, but more on that later.

### Setting up virtual env

Python 3.6 is cutting edge.  As a result some things are "wonky".  

In order to get virtual env working you'll need to do:

`virtualenv -p $(which python3) venv` 

to set up the virtual env.

