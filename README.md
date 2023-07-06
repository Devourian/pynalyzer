<p align="center">
  <img alt="Logo" src="assets/img/binary-code.png" />
</p>

<h2 align="center">pynalyzer</h2>
<h4 align="center">Meta code analysis tool for Python, 
bundling together multiple code analysis libraries. </h4>
<hr></hr>
<p align="center">
<a href="https://docs.python.org/"><img alt="python" src="https://img.shields.io/badge/Python-3.7+-3776ab?style=flat-square&logo=python&labelColor=dddddd"></a>
<a href="https://pypi.org/project/pynalyzer/"><img alt="pypi" src="https://img.shields.io/pypi/dm/pynalyzer?style=flat-square&logo=pypi&label=pypi%20downloads&labelColor=dddddd&color=3776ab"></a>
<a href="https://python-poetry.org/docs/"><img alt="poetry" src="https://img.shields.io/badge/dependencies-poetry-60a5fa?style=flat-square&logo=poetry&labelColor=dddddd"></a>
<a href="https://docs.pytest.org/"><img alt="pytest" src="https://img.shields.io/badge/tests-pytest-0a9edc?style=flat-square&logo=pytest&labelColor=dddddd"></a>
<a href="https://black.readthedocs.io/en/stable/"><img alt="black" src="https://img.shields.io/badge/code%20style-black-000000?style=flat-square&logoColor=000000&labelColor=dddddd"></a>
<a href="https://pycqa.github.io/isort/"><img alt="isort" src="https://img.shields.io/badge/imports-isort-ef8336?style=flat-square&labelColor=dddddd"></a>
<a href="https://mypy.readthedocs.io/en/stable/"><img alt="mypy" src="https://img.shields.io/badge/type%20checker-mypy-1f5082?style=flat-square&labelColor=dddddd"></a>
<a href="https://bandit.readthedocs.io/en/latest/"><img alt="bandit" src="https://img.shields.io/badge/security-bandit-fad23f?style=flat-square&labelColor=dddddd"></a>
</p>


## Table of Contents

<!-- TOC -->
  * [Table of Contents](#table-of-contents)
  * [About](#about)
    * [Advantages](#advantages)
    * [CI/CD](#cicd)
  * [Installation](#installation)
  * [Prerequisites](#prerequisites)
    * [Tools configuration](#tools-configuration)
  * [Usage](#usage)
    * [Running static code analysis checks locally](#running-static-code-analysis-checks-locally)
    * [Automatically fixing code analysis issues](#automatically-fixing-code-analysis-issues)
  * [Credits](#credits)
<!-- TOC -->


## About

The main idea behind `pynalyzer` is to improve and simplify 
experience of python developers using multiple code analysis 
tools at once.
  
`pynalyzer` provides easy to use Command Line Interface to
run all the code analysis checks you would ever need.

It is bundling together multiple cutting-edge 
code analysis libs for Python, specifically:
- [`isort`](https://pycqa.github.io/isort/) for import sorting
- [`black`](https://black.readthedocs.io/en/stable/) for code formatting
- [`mypy`](https://mypy.readthedocs.io/en/stable/) for typing checks
- [`bandit`](https://bandit.readthedocs.io/en/latest/) for security issues


### Advantages

`pynalyzer` is super simple to use with two easy to memorize commands: `check` and `fix`

`pynalyzer` is **OS-independent**, so you can use 
it wherever you want:
- Windows / Linux / MacOS
- CMD / Powershell / Bash / zsh / others

It is also **project-structure-independent**, meaning 
you can use it in all types of Python projects:
- projects containing only `requirements.txt` for dependencies
- projects using `setup.py` for dependencies and/or packaging
- project using `pyproject.toml` for dependencies and/or packaging
- etc.

Easily configurable with industry standard - `pyproject.toml` file

It can be used in CI/CD, to prevent false positive checks between local and remote runs.

Freedom of configuration - you decide how you want to configure every static code analysis tool,
that `pynalyzer` bundles (e.g. `mypy`) by configuring them through `pyproject.toml` file.


### CI/CD
  
The main use-case for `pynalyzer` is to run all code analysis checks 
with single command locally, but it can also be used to simplify 
CI/CD pipelines like GitHub Actions Workflow, GitLab Pipelines, Jenkins, etc.

Using `pynalyzer` in CI/CD has one huge advantage,
you won't face a problem where checks pass locally, 
but fail on a remote, which is a pretty popular scenario,
when using standalone commands.

This is not the case in `pynalyzer`, as it will use the 
same commands and the same configuration file to configure
code analysis tools, both on remote and locally.


## Installation

Install using [`pip`](https://pip.pypa.io/en/stable/):
```shell
pip install pynalyzer
```
or using [`poetry`](https://python-poetry.org/):
```shell
poetry add pynalyzer
```


## Prerequisites

In order to successfully run `pynalyzer`, you need to:
1. [Install `pynalyzer` package](#installation)
2. Create `pyproject.toml` file in root directory of the project (if it doesn't already exist)
3. Configure `pynalyzer`, by adding `[tool.pynalyzer]` section to `pyproject.toml` file
4. Under `[tool.pynalyzer]` section specify the `paths` key with value being an array of strings,
which holds all paths that need to be checked by pynalyzer code analysis checks.
  
    *Example*
    ```toml
    [tool.pynalyzer]
    paths = ["tests", "scripts/my_script.py"]
    ```
    > **Note**  
    > - paths can be absolute or relative to project root directory
    > - paths can lead to single file or to directory with files
5. [Configure static analysis tools in `pyproject.toml` file to suit your likings](#tools-configuration)


### Tools configuration

All code analysis tools are configured through `pyproject.toml` file,
which you need to put at the root of your project.
  
For the instruction of how to configure each tool
using `pyproject.toml` check their docs:
- [isort](https://pycqa.github.io/isort/docs/configuration/options.html)
- [black](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-via-a-file)
- [mypy](https://mypy.readthedocs.io/en/stable/config_file.html#using-a-pyproject-toml-file)
- [bandit](https://bandit.readthedocs.io/en/latest/config.html#bandit-settings)

Minimal configuration example:
```toml
[tool.black]
line-length = 88
target-version = ["py37"]

[tool.isort]
profile = "black"

[tool.mypy]
disallow_untyped_defs = true

[tool.bandit.assert_used]
skips = ["*_test.py", "*/test_*.py"]

[tool.pynalyzer]
paths = ["some_dir", "some_file.py"]  # Fill this with paths to dirs and files you want to analyze
```


> **Note**  
> 1. Other configuration files than `pyproject.toml`, e.g. `.bandit` will **not** be 
> taken into account when running `pynalyzer`.
> Configuration for every code analysis tool will only be taken from `pyproject.toml`.
> 2. `pynalyzer` is not configuring / forcing any configuration of 
any tool.  
> This approach gives you freedom of configuration, 
you can configure every tool to suit your preferences and needs.

     
## Usage

Make sure you have done all the steps in [Prerequisites](#prerequisites) before running `pynalyzer`


### Running static code analysis checks locally

To run all static code analysis checks:
1. Go to project root directory (where you created `pyproject.toml` file)
2. Execute `check` command (without any arguments):
    ```shell
    check
    ```
    This will run all the code analysis checks at once on all files  
    and directories, one provided in `paths` in `pyproject.toml` configuration file.

> **Note**  
> To not waste any time and / or resources, this command will **not** continue 
> to run other checks, if one of them failed.  
> 
> For example, if 2nd check (e.g. `isort`) failed, then 3rd and 4th checks won't execute.  
> Developer should firstly fix the issues that caused the 2nd check to fail, 
> in order to continue checking code with checks 3rd and 4th.
> 
> This is done this way to be easy to use with CI/CD,
> where every minute is precious using paid runners.


### Automatically fixing code analysis issues

Some code analysis issues can be automatically fixed:
- code formatting (`black`) 
- import sorting (`isort`)

To run all fixes at once, one can use `fix` command:
1. Go to project root directory (where you created `pyproject.toml` file)
2. Execute `fix` command (without any arguments):
    ```shell
    fix
    ```


## Credits

Image used for logo was downloaded from: <a href="https://www.flaticon.com/free-icons/binary" title="binary icons">Binary icons created by Freepik - Flaticon</a>
