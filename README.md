[![Build Status](https://robertpoenaru.visualstudio.com/test-pipelines/_apis/build/status/basavyr.python-classes?branchName=master)](https://robertpoenaru.visualstudio.com/test-pipelines/_build/latest?definitionId=3&branchName=master)

# Python Classes 
Implement Python classes that provide useful features within Numerical Programming and Data Visualization.

## Modules

* The `src/` directory contains Python scripts that will be used as *modules* for other source files.
* The `tests/` directory contains some scripts that take use of the created modules, and implement the class objects into useful algorithms that can:
  * plot data to files
  * write logs 
  * operate with list objects (sort, frequency count, etc. )

## Integrations

* This project uses **CircleCI** for setting up a CI/CD pipeline.
* It also takes advantage of Docker, using a `Dockerfile` for building and running a simple image in CircleCI workfllow that tests the developed modules

## TO-DO

[ ] - Implement Azure Pipeline with Docker integration
