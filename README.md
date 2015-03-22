NQueens
-------
This is a python script that solves the classical AI problem NQueens.
The problem is to try to place N number of queens on an NxN chess board
without having any of the queens attack any other queen. This program
places the queens on the board without violating the attack rule.

The program uses Python's itertools library which is part of the Python
Standard Library. From itertools i specifically use the permutations
function which generates all valid horizontal and vertical permutations.
I then filter the resulted permutation to allow only for valid vertical,
horizontal and diagonal results. You can view the solve() method in
NQueensModel class for the exact code that solves the NQueens problem.

I used the MVC (Model, View, Controller) design pattern to implement the
program. It is very helpful to separate the data (Model), UI (View), and
code (Controller). This design pattern simplifies implementing the
solution.

Moreover, this program wouldn't have been possible withouth the urwid
python library. For more information on urwid please visit:
http://urwid.org/index.html


Dependencies
------------
python 2.7.9
urwid 1.2.1


Run
---
To run the program make sure you install urwid first. Either pip install
or if you're on Mac OSX you can use macports or brew to install the urwid
library. After you do so you can simply:

$ python nqueens.py

![Alt text](screenshot.png?raw=true "NQueens")
