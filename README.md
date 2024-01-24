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

TBA

### Install packages

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