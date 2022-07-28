## Prerequisites:
1. Python version: >3.6
2. To run programs from the repository install prerequisite Python modules with:
```shell
python3 -m pip install black flake8 ipython mypy pylint pytest yapf
```
Or install via requirements file:
```shell
python3 -m pip install -r requirements.txt
```

## Formatter usage:
To format code in-place (original file will be overwritten) use `-i` paramater with `yapf` formatter:
```shell
yapf -i my_file.py
```

## Reference:
1. [The uncompromising Python code formatter](https://github.com/psf/black)
2. [Flake8: Your Tool For Style Guide Enforcement](https://flake8.pycqa.org/en/latest/)
3. [IPython](https://ipython.org/)
4. [Optional static type checker for Python](http://mypy-lang.org/)
5. [Pylint is a static code analyser for Python 2 or 3](https://pylint.pycqa.org/en/latest/)
6. [pytest: helps you write better programs](https://docs.pytest.org/en/7.1.x/)
7. [A formatter for Python files](https://github.com/google/yapf)