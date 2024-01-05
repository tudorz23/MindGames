*Designed by Marina Oprea (323CA), Alexandra Ionita (32_CB), Marius-Tudor Zaharia (323CA),
Mihnea ___() in January 2024*

# MindGames

---

## Table of contents
1. [What is MindGames?](#what-is-mindgames)
2. [Prerequisites](#prerequisites)
3. [Run procedure](#run-procedure)
4. [Playing the games](#playing-the-games)
    * [Sudoku gameplay](#sudoku-gameplay)
    * [HangMan gameplay](#hangman-gameplay)
5. [Implementation details](#implementation-details)
    * [Sudoku creation](#sudoku-creation)
    * [HangMan creation](#hangman-creation)
6. [Conclusions](#conclusions)

---

## What is MindGames?
* MindGames is a collection of games that stimulate players' problem-solving
capacities.
* It currently consists of two separate games:
  * ***Sudoku***
  * ***HangMan***

---

## Prerequisites
* To successfully run the games, it is necessary that the user has python3
installed on his machine.

---

## Run procedure
* *TBC*

---

## Playing the games
### Sudoku gameplay
* The game's goal is to complete a 9x9 grid with digits from 1 to 9, without
repeating them on any row, column or 3x3 mini-grid.
* There are 4 levels of difficulty, from 0 to 3.
* Press the `Play` button to start the first level.
* Use the mouse to select a square to place a digit.
* If the digit is already placed on any row, column or mini-grid, it will be
invalid and colored in red, else it will appear blue.
* There are a pre-determined number of hints for every level.
* For grid navigation, `TAB` and `Left and Right Arrows` can be used.

### HangMan gameplay
* *TBC*

---

## Implementation details
### Sudoku creation
* This game was developed by Marina Oprea and Tudor Zaharia, together.
* We used the `Code with me` feature of PyCharm to simultaneously edit the
project, while on a call on Messenger :).
* It is written fully in Python, using the `pygame` and `numpy` libraries.
* OOP concepts have been used, all functionalities being placed in `classes`.
* `GameSession` is the control class, responsible with linking the
functionalities, while `GameRunner` controls the sudoku game per se.
* Each menu has a different source class, and their respective `run()` method
returns 1 in case the user wants to exit the game, or 0 if the game should
go on.

### HangMan creation
* *TBC*

---

## Conclusions
* The main and obvious difficulty was that we had no previous experience with
Python, so thorough documentation and tutorial watching was necessary to get
the thing going, but, overall, it was a fun experience.
