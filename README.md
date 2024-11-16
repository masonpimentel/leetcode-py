# Leetcode Filter

This is a script that will get all problems from your LeetCode account that are:

* Not yet completed (does not have `ac` status)
* Medium difficulty
* Has more user likes than dislikes (the 'thumbs up' from users, not acceptance rate)
* Supports a specified programming language (currently set to `Python3`)

The last I checked LeetCode did not have any public documentation for their GraphQL API so this is super hacky, especially getting authentication details.

## Running

The steps to run this script are:

1. Install Python
2. Install `pipenv`
3. Install packages
4. Get your auth info from LeetCode
5. Run the script

### Install Python

Download and install the latest (3.x) version of Python for your system.

#### Mac

For Mac my recommendation would be to use pyenv: https://github.com/pyenv/pyenv (using the installer from https://www.python.org/downloads/ causes a mess with the `python` and `pip` aliases in my experience).

If using the `pyenv` approach, the following should work (note that at time of writing `pipenv` in the next step prefers v3.11, but you can list all available versions using `pyenv install -l`):

```
$ brew update
$ brew install pyenv
$ pyenv install 3.11.7
$ pyenv global 3.11.7
```

Then follow the appropraite steps in https://github.com/pyenv/pyenv?tab=readme-ov-file#set-up-your-shell-environment-for-pyenv

#### Windows

Give `pyenv-win` a try: https://github.com/pyenv-win/pyenv-win

See the quick start guide: https://github.com/pyenv-win/pyenv-win?tab=readme-ov-file#quick-start

### Install pipenv

Install `pipenv` to manage virtualenv: https://pipenv.pypa.io/en/latest/



```
$ pip install --user pipenv
```

#### Mac note

Note that if you see the output

```
WARNING: The scripts pipenv and pipenv-resolver are installed in '/Users/masonpimentel/.local/bin' which is not on PATH.
```

You might have do adjust your PATH accordingly, for example on latest MacOS, add this to your `.zshrc`:

```
export PATH=/Users/masonpimentel/.local/bin:$PATH
```

#### Windows note

You might need to add the pipenv executable to your path, for example

`C:\Users\<username>\AppData\Roaming\Python\Python312\Scripts`

### Install packages

```
$ pipenv run sync
```

### Get your auth info from LeetCode

Two values need to be filled in:

`LEETCODE_SESSION`: https://github.com/masonpimentel/leetcode-py/blob/cc7e321782e25f8fc7d49048924ef0c142c1c0eb/src/main.py#L7

`CSRF_TOKEN`: https://github.com/masonpimentel/leetcode-py/blob/cc7e321782e25f8fc7d49048924ef0c142c1c0eb/src/main.py#L8

To obtain these, go to https://leetcode.com/problemset/ and inspect your network requests (ex. for Chrome: https://developer.chrome.com/docs/devtools/network)

Find any request to https://leetcode.com/graphql/:

![](assets/GraphQLRequest.png) |
------------ | 
_Finding a GraphQL request_ | 

And find the `LEETCODE_SESSION` value and `csrftoken` value (stored as `CSRF_TOKEN` in code) in Request Headers -> Cookie:

![](assets/GettingValues.png) |
------------ | 
_Taking LEETCODE_SESSION and CSRF_TOKEN values_ | 

Be sure not to check these in to version control!

### Run the script

```
$ cd src
$ pipenv run python main.py
```

## Development

### Fix linting in VS Code

In VS Code to fix import lint error, set the interpreter to the one in your virtual env:

![](assets/Step1.png) |
------------ | 
_Step 1 - click here on the bottom right part in VS Code_ | 


![](assets/Step2.png) |
------------ | 
_Step 2_ - select your current workspace | 

![](assets/Step3.png) |
------------ | 
_Step 3_ - set this to the right interpreter | 

## Testing

### Run tests

```
$ cd tests
$ pipenv run pytest
```

### Get coverage report

```
$ cd tests
$ pipenv run coverage run -m pytest
$ pipenv run coverage report -m
```

## Linting

```
$ pipenv run pylint_check
```

## Type check

```
$ pipenv run mypy src
```
