# Password Generator

A simple and secure Python program that generates random passwords.

## Features

- Options to generate passwords based on a total length or specific number of letters, numbers, and symbols
- Cryptographically secure randomization using the `secrets` module
- Retry on invalid input and generate multiple passwords in one session

## Python Concepts

- Modules (`secrets` and `string`)
- Functions
- Loops (`while` and `for` loops)
- Conditional statements
- Error handling with `try/except` block
- Lists
- List shuffling
- Convert a list of characters into a string
- `continue` and `break` statements

## How To Run

1. Clone the repository and change to the project folder

```bash
git clone https://github.com/trucanhng/python-mini-projects.git
cd password-generator
```

2. Run the script

```bash
python3 password-generator.py
```

## Sample Run

```text
Welcome to The Password Generator.
There are 2 options:
1. Enter the total password length.
2. Specify the number of letters, numbers, and symbols separately.
Do you want to enter a total length? (y/n) y
Enter total password length: 12
Your password is: &$c%jn5x1o81
Do you want to generate another password? (y/n) n
```
