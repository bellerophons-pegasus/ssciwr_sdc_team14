# ssciwr_sdc_team14
A repository for the course: [sustainable software development](https://github.com/ssciwr/sustainable_development_course) (team 14)

The task was to create a small software package with some modules in Python including documentation, testing and automated actions. The aim of the course was to learn what constitutes sustainable software and put this into practice with the provided example.

The software example was given in unit 1 in a [Jupyter Notebook](). After working on it in the notebook, we created a module layout via [a Google Jamboard](https://jamboard.google.com/d/1s-L8ETmGIws289NFmPOz2I0ORVLDQs6y5oH2lCLe4ac/viewer). For the modules we discerned, we created issues on this GitHub repository and assigned them to the responsible team members. The documentation is done with Sphinx and is published on [readthedocs](https://ssciwr-sdc-team14.readthedocs.io/).

## Things we could have done better

* Think twice or thrice about naming conventions. This becomes quite important when packaging and pushing to e.g. PIP.
* Not only focus on the individual tasks, but have a more active exchange in the team and e.g. explain what we did in the code. Feedback and questions from the team members can help in detecting code issues in terms of functioning, readability, interoperability, and understandability.
* Think about input and output (e.g. locations).

Below follows a list of commands and useful links and comments for working with git and Sphinx.

## Useful commands for working wit git
Create Repository:
1. cloning existing
```
git clone <somue-URL>
```
2. initialising a local directory as git repo
```
git init
```

Get newest stuff from remote
```
git pull
```

Show local status of repository
```
git status
```

Display local differences compared to last pull
```
git diff
then exit with 'q'
```

### Branches
Create branch
```
git branch <some-branch-name>
```

Change to some branch for working on it
```
git checkout <some-branch-name>
```

Push branch to remote
```
git push -u origin <some-branch-name>
```

List local branches (those marked with * are checked out)
```
git branch
```

List remote branches
```
git branch -r
```

Delete local branch
```
git branch -d <some-branch-name>
```

Delete remote branch
```
git push origin -delete <some-branch-name>
```

Move changes to another branch: https://stackoverflow.com/questions/7217894/moving-changed-files-to-another-branch-for-check-in

### Stage, commit and push
After changes are done add to staging
```
git add <some-file-path>
```

Commit the staged change
```
git commit -m 'a short meaningful message'
```

Push to remote
```
git push
```

## File naming and other conventions
* [PEP8](https://www.python.org/dev/peps/pep-0008)
* [Python Naming Conventions](https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html)

## Documentation with Sphinx

initialise documentation with: (when you are in doc); executing it once suffices unless new modules come in
```
sphinx-apidoc -o source/ ../src/
```

clean everything; execute in doc (`where make.bat` and `Makefile` lie)
```
make clean
```

update html with docstrings
```
make html
```

### Including extra text

#### Inside rst files
* Just add additional content in [rst syntax](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-primer)
* You can also create your own rst pages in `source` and add them by including them in the relevant table of contents (`toctree`). E.g. in `index.rst`

#### Additional md files
* You will need the additional module [recommonmark](https://www.sphinx-doc.org/en/master/usage/markdown.html)
* Then you can create your md pages and add them by including them in the relevant table of contents (`toctree`).

### Sphinx troubleshooting

If for some reason not all modules are properly parsed by Sphinx (i.e. an rst file is missing for them) you will have take manual action.
In `source` open `modules.rst`. After the lines starting with `.. toctree::` add your module name to the list of modules.

```src
===

.. toctree::
   :maxdepth: 4

   io14
   filter14
   numeric_methods
   statistics14
   <yourModuleHere>

```

## other useful links

* https://ssc.iwr.uni-heidelberg.de/resources
