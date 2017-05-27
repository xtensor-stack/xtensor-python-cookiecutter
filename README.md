![cookicutter-logo](./cookiecutter.png)

[![Travis](https://travis-ci.org/QuantStack/xtensor-python-cookiecutter.svg?branch=master)](https://travis-ci.org/QuantStack/xtensor-python-cookiecutter)
[![Appveyor](https://ci.appveyor.com/api/projects/status/ek0yq62h61r1pwbj?svg=true)](https://ci.appveyor.com/project/QuantStack/xtensor-python-cookiecutter)
[![Documentation Status](https://readthedocs.org/projects/xtensor/badge/?version=latest)](https://xtensor.readthedocs.io/en/latest/?badge=latest)
[![Join the Gitter Chat](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/QuantStack/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

#### A [cookicutter](https://github.com/audreyr/cookiecutter) template for creating a custom Python extension with xtensor

## What is xtensor-cookiecutter?

`xtensor-cookiecutter` helps extension authors create Python extension modules making use of xtensor.

It takes care of the initial work of generating a project skeleton with

- A complete `setup.py` compiling the extension module
- A few examples included in the resulting project including

    - A universal function defined from C++
    - A function making use of an algorithm from the STL on a numpy array
    - Unit tests
    - The generation of the HTML documentation with sphinx

## Usage

Install [cookiecutter](https://github.com/audreyr/cookiecutter):

    $ pip install cookiecutter

After installing cookiecutter, use the xtensor-cookiecutter:

    $ cookiecutter https://github.com/QuantStack/xtensor-cookiecutter.git

As xtensor-cookiecutter runs, you will be asked for basic information about
your custom extension project. You will be prompted for the following
information:

- `author_name`: your name or the name of your organization,
- `author_email`: your project's contact email,
- `github_project_name`: name of the GitHub repository for your project,
- `github_organization_name`: name of the GithHub organization for your project,
- `python_package_name`: name of the Python package created by your extension,
- `cpp_namespace`: name for the cpp namespace holding the implementation of your extension,
- `project_short_description`: a short description for your project.
  
This will produce a directory containing all the required content for a minimal extension
project making use of xtensor with all the required boilerplate for package management,
together with a few basic examples. The generated Python extension requires an installation
of  `xtensor` `^0.8.1`, `xtensor-python` `^0.9.0`, `numpy`, and `pybind11` `^2.1.0`.

Install the module:

    $ pip install ./{{ cookiecutter.github_project_name }}/


If you have [Jupyter](jupyter.org) installed, run the [Test_Run notebook](http://nbviewer.jupyter.org/github/QuantStack/xtensor-cookiecutter/blob/master/Test_Run.ipynb):

    $ cd {{ cookiecutter.github_project_name }}
    $ jupyter notebook

Otherwise just run the test script:

    $ cd {{ cookiecutter.github_project_name }}
    $ python Test_Run.py


## Resources

- [Documentation of xtensor](https://xtensor.readthedocs.io/en/latest/)
- [Documentation of xtensor-python](https://xtensor-pyhton.readthedocs.io/en/latest/)
- [Documentation of xtensor-julia](https://xtensor-julia.readthedocs.io/en/latest/)
