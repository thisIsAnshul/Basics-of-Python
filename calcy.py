from guietta import _, Gui, Quit

gui = Gui(
    ["Enter number 1: ", _, "__n1__"],
    ["Enter number 2: ", _, "__n2__"],
    [["Add"], ["Sub"], ["Multiply"]],
    ["Result = ", _, "result"],
)


def add(gui):
    gui.result = int(gui.n1) + int(gui.n2)


def sub(gui):
    gui.result = int(gui.n1) - int(gui.n2)


def mult(gui):
    gui.result = int(gui.n1) * int(gui.n2)


gui.Add = add
gui.Sub = sub
gui.Multiply = mult

gui.run()
