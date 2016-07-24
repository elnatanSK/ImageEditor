from Tkinter import *


class MyMenu:
    def __init__(self, root):
        menu = Menu(root)
        root.config(menu=menu)

        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Project...", command=do_nothing)
        file_menu.add_command(label="New File...", command=do_nothing)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

        edit_menu = Menu(menu)
        menu.add_cascade(label="File", menu=edit_menu)
        edit_menu.add_command(label="Copy", command=do_nothing)
        edit_menu.add_command(label="Paste", command=do_nothing)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=do_nothing)


def do_nothing():
    print "Nothing at all"
