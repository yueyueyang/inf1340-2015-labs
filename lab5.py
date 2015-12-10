#!/usr/bin/env python3

""" GUI for Name that Shape """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from name_that_shape import *
import Tkinter
import tkMessageBox

"""
   Create a GUI for the Name That Shape program
   See name_shape_gui.png for specification
   Use the name_that_shape.py to perform computations
   For inputs that raise an error, pop up a modal dialog box
   For inputs that produce a shape name, display the string in the window
"""


class NameThatShapeGUI:


    def __init__(self):
        self.main_window = Tkinter.Tk()
        self.main_window.title("tk #10")
        # resize the window
        self.main_window.geometry("500x100")
        #background colour
        self.main_window.configure(background="#FFFFFF")

        # side entry
        self.entry = Tkinter.Frame(self.main_window)
        self.prompt_label = Tkinter.Label(self.entry, text='Enter the number of sides in the shape:')
        self.side_entry = Tkinter.Entry(self.entry, width=10)

        # show shape name
        self.name = Tkinter.Frame(self.main_window)
        self.name_label = Tkinter.Label(self.name, text='Name of Shape: ')
        self.shape = Tkinter.StringVar()
        self.shape.set("")
        self.shape_name = Tkinter.Label(self.name, textvariable=self.shape)

        # create button
        self.button = Tkinter.Frame(self.main_window)
        self.get_name = Tkinter.Button(self.button, text='Name', command=self.convert, width=4)
        self.quit = Tkinter.Button(self.button, text='Quit', command=self.main_window.destroy, width=3)

        # pack the widgets
        self.prompt_label.pack(side='left')
        self.side_entry.pack(side='left')

        self.name_label.pack(side='left')
        self.shape_name.pack(side='left')

        self.get_name.pack(side='left')
        self.quit.pack(side='left')

        # Pack the frames in the order they will appear
        self.entry.pack()
        self.name.pack()
        self.button.pack()


        Tkinter.mainloop()

    def error_message(self):
        tkMessageBox.showinfo("Response", "\"" + self.side_entry.get() + "\" is invalide input, please try it again!")

    def convert(self):
        shapename = name_that_shape(self.side_entry.get())
        if shapename is None:
            self.error_message()
        else:
            self.shape.set(shapename)

# Instantiating the object
ntsg = NameThatShapeGUI()
