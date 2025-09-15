# Hangman Game

A simple command-line Hangman game.
The player chooses a category (animals, fruits, countries, sports, technology), then tries to guess the hidden word letter by letter before running out of lives.

## Features

- Category selection (Animals, Fruits, Countries, Sports, Technology)
- 6 lives with ASCII art hangman stages
- Input validation (only single letters allowed)
- Duplicate guess prevention
- Replay option after each game

## Python Concepts

- Functions
- Loops with `continue` and `break` statements
- Lists
- Dictionaries
- String manipulation
- Modules and imports
- Random module
- Conditional statements

## How To Run

1. Clone the repository and change to the project folder

```bash
git clone https://github.com/trucanhng/python-mini-projects.git
cd hangman
```

2. Run the script

```bash
python3 hangman.py
```

## Sample Run

```text
Welcome to The Hangman World.
Pick a category (animals/fruits/countries/sports/technology): animals
The word has 5 letters.
_____

      +---+
          |
          |
          |
         ===

You have 6/6 lives left

==============================

Guess a letter: a
__a_a

      +---+
          |
          |
          |
         ===

You have 6/6 lives left

==============================

Guess a letter: a
You already guessed that letter.
Guess a letter: k
k_a_a

      +---+
          |
          |
          |
         ===

You have 6/6 lives left

==============================

Guess a letter: m
k_a_a

      +---+
      O   |
          |
          |
         ===

You have 5/6 lives left

==============================

Guess a letter: n
k_a_a

      +---+
      O   |
      |   |
          |
         ===

You have 4/6 lives left

==============================

Guess a letter: q
k_a_a

      +---+
      O   |
     /|   |
          |
         ===

You have 3/6 lives left

==============================

Guess a letter: p
k_a_a

      +---+
      O   |
     /|\  |
          |
         ===

You have 2/6 lives left

==============================

Guess a letter: d
k_a_a

      +---+
      O   |
     /|\  |
     /    |
         ===

You have 1/6 lives left

==============================

Guess a letter: w
k_a_a

      +---+
      O   |
     /|\  |
     / \  |
         ===

You have 0/6 lives left

==============================

Sorry. You lost!
The correct word was koala
Do you want to start a new game (y/n)? y
Pick a category (animals/fruits/countries/sports/technology): fruits
The word has 10 letters.
__________

      +---+
          |
          |
          |
         ===

You have 6/6 lives left

==============================

Guess a letter: m
m_________

      +---+
          |
          |
          |
         ===

You have 6/6 lives left

==============================

Guess a letter: a
ma________

      +---+
          |
          |
          |
         ===

You have 6/6 lives left

==============================

Guess a letter: n
man______n

      +---+
          |
          |
          |
         ===

You have 6/6 lives left

==============================

Guess a letter: g
mang_____n

      +---+
          |
          |
          |
         ===

You have 6/6 lives left

==============================

Guess a letter: st
Please enter a single letter.
Guess a letter: s
mang_s___n

      +---+
          |
          |
          |
         ===

You have 6/6 lives left

==============================

Guess a letter: 3
Please enter a single letter.
Guess a letter: t
mang_st__n

      +---+
          |
          |
          |
         ===

You have 6/6 lives left

==============================

Guess a letter: e
mang_steen

      +---+
          |
          |
          |
         ===

You have 6/6 lives left

==============================

Guess a letter: o
mangosteen

      +---+
          |
          |
          |
         ===

You have 6/6 lives left

==============================

Congratulations. You got it!
Do you want to start a new game (y/n)? n
```
