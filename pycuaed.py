import curses

# https://docs.python.org/3/howto/curses.html

class PyCUAEd:
    key_mapping = {}

    def __init__(self):
        self.curses_window = 0
        self.buffer = [""] # list of lines
        self.cursor = (0,0)
        self.top_left = (0,0) # where in the text is the window "viewport" anchored
        self.history = []

    def loop(self, stdscr):
        self.curses_window = stdscr
        self.curses_window.clear()
        while 1:
            self.curses_window.redraw()
            pressedkey=self.curses_window.getkey()
            self.curses_window.addstr(pressedkey)

    def keystroke(self, f, modifier, key):
        PyCUAEd.key_mapping[(modifier, key)] = f

    @keystroke("Ctrl", "z")
    def undo(self):
        pass
    @keystroke("Ctrl", "y")
    def redo(self):
        pass

    @keystroke("Ctrl", "x")
    def cut(self):
        pass
    @keystroke("Ctrl", "c")
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
    def print(self):
        pass

    @keystroke("Ctrl", "f")
    def find(self):
        pass

    @keystroke("Ctrl", "w")
    def quit(self):
        pass

    @keystroke("Shift", "Up|Down|Left|Right")
    def shift_arrows(self):
        pass
    @keystroke("", "Up|Down|Left|Right")
    def arrows(self):
        pass

    @keystroke("", ".")
    def std(self):
        pass
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
    def format(self):
        pass


def main():
    pycuaed = PyCUAEd()
    curses.wrapper(pycuaed.loop)

if __name__=="__main__":
    main()