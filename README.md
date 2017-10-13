![alt text](https://github.com/stoychevvasko/Python/blob/master/.resources/python-logo.png "Python Logo")**Python**
TILs

To export dependencies requirements, run this script as administrator:
```shell
pip freeze > requirements.txt
```

To install dependencies from the list thusly created, use:
```shell
pip install -r requirements
```

To set up virtual environment on project level use this script and add VIRTUAL/ directory to gitignore:
```shell
virtualenv VIRTUAL
Scripts/activate.bat
```

To run code tests and linter, run this script through the terminal:
```shell
clear && py.test -v --color=yes && pylint -d locally-disabled *.py
```
