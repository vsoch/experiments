# Expfactory Library

This is the library of official experiments provided by the Experiment Factory. Adding experiments to the core expfactory family is a process centered around pull requests (PRs), one of them being to this repo. Before contributing an experiment, the following questions are important to consider:

 - is this experiment generally useful to the larger community? For example, a new task would be useful, but a slightly modified stroop would be better served from your own repo.
 - Once you experiment is added to the library, you as the author are responsible for keeping it up to date and responding to issues, of course with help from our team. Updates will follow the same process.

# The general steps
You will want to first make an experiment repo, which should conform to the [expfactory-experiments](https://www.github.com/expfactory-experiments) standard, which includes docs for your experiment as well. Then, fork this repo, add in the [experiments](experiments) folder, create a file named equivalently to your experiment. The following file should then be submit via a pull request.

### Experiment Metadata File
This file should be named corresponding to the same experiment id, and with the same rules - all lowercase with no special characters aside from an underscore. For example, if my experiment is called `stroop` I would add a file called `experiments/stroop.json` and then include the following content:


```
{

   "maintainers": [ {
                    "name":"Vanessa Sochat",
                    "email": "vsochat@example.com",
                    "github": "@vsoch"
                    },

                   {
                    "name":"Teon Brooks",
                    "email": "tbrooks@example.com",
                    "github": "@teonbrooks"
                    }
                  ],

    "github":     "https://github.com/expfactory-experiments/stroop.git"

}
```
