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

 _* Working with Pull Requests *_

There are two major things of importance when you are collaborating (in life, not just on github).  Creating pull requests and reviewing pull requests.  These are of equal importance!  Because creating pull requests is like talking (or writing) and reviewing pull requests is like listening (or reading).  So, how do we do either?

For this project, we'll be creating pull requests and merging pull requests via github.  There are nice friendly buttons that look like the following:

![PR button](https://github.com/hackingagainstslavery/django-demo-site/blob/master/docs/images/pr_button.png)

![Merge button](https://github.com/hackingagainstslavery/django-demo-site/blob/master/docs/images/merge_button.png)

You'll be creating pull requests from your fork.  And you'll be reviewing pull requests, also from your fork.  This keeps the canonical source pollution free, until after review!  Which is super good times magical fantastic.  In order to review changes, you'll be making use of git's command line review.

```
git checkout -b Github User Name-branch name branch name
git pull https://github.com/Github User Name/reponame.git branch name
```

You should then run the changes (if possible check off all of the following options):

* Run the server
* Run all the tests the person you are reviewing wrote (as well as all other tests). 
	* If there are no tests, go ahead and write some for the person and then publicly shame them
	for not using test best practices (tests are important!)
* If possible, refactor the source code (source code can *almost* always be refactored)

Then push your changes to the Pull request (if you had to make any).  Otherwise go ahead and leave a nice comment, and then merge in the changes with the big green merge button!

If you did make changes to the Pull Request, make a comment with the github user's name (@GithubUserName).  And then ping them to make sure they see it.  After that, go ahead and get them to review your changes.  If everything looks good, they'll go ahead and merge their changes as well as your updated changes.

Rule of thumb:  The last person to make changes to a Pull Request, should not merge that pull request in.  

Obviously best practice falls away under deadlines (duh).

### Setting up virtual env

Python 3.6 is cutting edge.  As a result some things are "wonky".  

In order to get virtual env working you'll need to do:

`virtualenv -p $(which python3) venv` 

to set up the virtual env.

