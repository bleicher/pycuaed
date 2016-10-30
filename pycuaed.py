#!/usr/bin/python

import curses
import re

# doc https://docs.python.org/3/howto/curses.html

# usage: download from https://raw.githubusercontent.com/bleicher/pycuaed/master/pycuaed.py, start with
# python pycuaed.py

def keystroke(modifier, key):
    return lambda f: store_key((modifier, key), f)

def store_key(modifierkey, f):
    key_mapping[modifierkey] = f

key_mapping = {}

modern_to_curses_mapping = {
    ("", "Left") : "KEY_LEFT",
    ("", "Right"): "KEY_RIGHT",
    ("", "Up"): "KEY_UP",
    ("", "Down"): "KEY_DOWN",

    ("Shift", "Up"): "\^\[\[A",
    ("Shift", "Down"): "\^\[\[B",
    ("Shift", "Right"): "\^\[\[C",
    ("Shift", "Left"): "\^\[\[D",

    ("Ctrl", "u"): "\^U",
    ("Ctrl", "y"): "\^Y",
    ("Ctrl", "x"): "\^X",
    ("Ctrl", "g"): "\^G",
    ("Ctrl", "v"): "\^V",
    ("Ctrl", "o"): "\^O",
    ("Ctrl", "s"): "\^S",
    ("Ctrl", "p"): "\^P",
    ("Ctrl", "f"): "\^F",
    ("Ctrl", "r"): "\^R",
    ("Ctrl", "w"): "\^W",
    ("Ctrl", "a"): "\^A",

    ("", "Newline"): "\n",
    ("", "Backspace"): "KEY_BACKSPACE",
    ("", "Delete"): "KEY_DC"
}

class PyCUAEd:

    def __init__(self):
        self.curses_window = 0
        self.buffer = [""] # list of lines
        self.cursor = (0,0) # x,y (right, down), not as curses unconventional y,x
        self.top_left = (0,0) # where in the text is the window "viewport" anchored
        self.history = []

    def loop(self, stdscr):
        self.curses_window = stdscr
        self.curses_window.clear()
        while 1:
            self.curses_window.refresh()
            pressedkey=self.curses_window.getkey()
            for key, value in key_mapping.items():
                if re.fullmatch(key, pressedkey, re.ASCII):
                    value(pressedkey)
#           self.curses_window.addstr(pressedkey)

    @keystroke("Ctrl", "u") # TODO: Ctrl-z is suspend, so either catch it or use a different key
    def undo(self):
        pass
    @keystroke("Ctrl", "y")
    def redo(self):
        pass

    @keystroke("Ctrl", "x")
    def cut(self):
        pass
    @keystroke("Ctrl", "g") # TODO: Ctrl-c is kill, so either catch it or use a different key
    def copy(self):
        pass
    @keystroke("Ctrl", "v")
    def paste(self):
        pass

    @keystroke("Ctrl", "o")
    def open(self):
        pass
    @keystroke("Ctrl", "s")
    def save(self):
        pass

    @keystroke("Ctrl", "p")
    def print_(self):
        pass

    @keystroke("Ctrl", "f")
    def find(self):
        pass

    @keystroke("Ctrl", "w")
    def quit(self):
        pass

    @keystroke("Ctrl", "a")
    def select_all(self):
        pass

    @keystroke("Shift", "Up|Down|Left|Right")
    def shift_arrows(self):
        pass
    @keystroke("", "Up|Down|Left|Right")
    def arrows(self):
        pass

    @keystroke("", ".")
    def std(self, pressedkey):
        self.cursor[0]
        self.curses_window.addstr(pressedkey)

    @keystroke("", "Newline")
    def newline(self):
        pass
    @keystroke("", "Delete")
    def delete(self):
        pass
    @keystroke("", "Backspace")
    def backspace(self):
        pass

    @keystroke("Alt", "r")
    def run(self):
        pass

    @keystroke("Alt", "f")
    def find(self):
        pass

def main():
    pycuaed = PyCUAEd()
    curses.wrapper(pycuaed.loop)

if __name__=="__main__":
    main()