import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from .dialog import CustomDialog, CustomDialogDrop
from PIL import Image, ImageTk
#!/usr/bin/env python3
import graphviz

root = None

class MainView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #update root
        root = parent

        #create LabelFram
        labelframeinput = LabelFrame(master=parent, text="InputView")
        labelframeinput.pack(fill=BOTH, expand=True)

        #create LabelFram
        labelframeoutput = LabelFrame(master=parent, text="OutputView")
        labelframeoutput.pack(fill="both", expand="yes")

        input = InputView(labelframeinput)
        output = OutputView(labelframeoutput)

        self.input = input
        self.output = output
        self.pack(padx=20, pady=20)
        
    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller
        self.input.controller = controller
        self.output.controller = controller

class InputView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #create a Display
        self.display = DisplayView(parent)

        #add widgets
        self.Epsilon = ttk.Label(master=self.display, text="E:", justify=LEFT)
        #self.Epsilon_var = tk.StringVar()
        #self.Epsilon_post = ttk.Entry(master=self.display, textvariable=self.Epsilon_var)
        self.Epsilon_post = ttk.Label(master=self.display, text="{}",relief=SUNKEN)
        self.Epsilon.grid(row=1, column=0, sticky=EW)
        self.Epsilon_post.grid(row=1, column=1, sticky=EW)

        self.Q = ttk.Label(master=self.display, text="Q:", justify=LEFT)
        self.Q_post = ttk.Label(master=self.display, text="{}",relief=SUNKEN)
        self.Q.grid(row=2, column=0, sticky=EW)
        self.Q_post.grid(row=2, column=1, sticky=EW)

        self.q_0 = ttk.Label(master=self.display, text="q_0:", justify=LEFT)
        self.q_0_post = ttk.Label(master=self.display, text="",relief=SUNKEN)
        self.q_0.grid(row=3, column=0, sticky=EW)
        self.q_0_post.grid(row=3, column=1, sticky=EW)
        
        self.F = ttk.Label(master=self.display, text="F:", justify=LEFT)
        self.F_post = ttk.Label(master=self.display, text="{}",relief=SUNKEN)
        self.F.grid(row=4, column=0, sticky=EW)
        self.F_post.grid(row=4, column=1, sticky=EW)

        #create dictionary to access widgets
        self.widgets = {
            "states":self.Q_post,
            "alphabet":self.Epsilon_post,
            "inital":self.q_0_post,
            "final":self.F_post,
            "delta":None
            }

        #create a control
        self.control = ControlView(parent)

        #add buttons
        self.enter_alphabet = ttk.Button(self.control, text="set alphabet", command=self.enter_alphabet_click)
        self.enter_alphabet.grid(row=0, column=0)

        self.add_state = ttk.Button(self.control, text="add state", command=self.add_state_click)
        self.add_state.grid(row=0, column=1)

        self.set_inital = ttk.Button(self.control, text="set inital", command=self.set_inital_click)
        self.set_inital.grid(row = 1, column = 0)

        self.set_Final = ttk.Button(self.control, text="set final", command=self.set_final_click)
        self.set_Final.grid(row = 1, column = 1)

        self.build = ttk.Button(self.control, text="build", command=self.build_click)
        self.build.grid(row = 2, columnspan=2, sticky=EW)

        #pack the display and control
        self.pack(side= TOP, padx=20, pady=20)

        # set the controller
        self.controller = None

    def enter_alphabet_click(self):
        if self.controller:
            selection = CustomDialog(root, "Enter language of NFA").show()
            self.controller.set_alphabet(selection)
        print(selection)
        pass

    def add_state_click(self):
        if self.controller:
            new_state = CustomDialog(root, "Enter node label").show()
            self.controller.add_state(new_state)
        
    def set_inital_click(self):
        if self.controller:
            states = self.Q_post["text"]
            intal_state = CustomDialogDrop(root, "Pick an inital state", states).show()
            self.controller.set_inital(intal_state)
        pass
    def set_final_click(self):
        print("set final")
        pass
    def build_click(self):
        if self.controller:
            self.controller.build()
        
    def update_display(self, widget:str ,value):
        self.widgets[widget]["text"] = value

    def show_error(self, message):
        messagebox.showerror(title="error",message=message)

class OutputView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #create a Display
        self.display = DisplayView(parent)

        self.regex = ttk.Label(self.display, text="{}",relief=SUNKEN)
        self.regex.grid(row=2, column=0, sticky=EW,pady=3)
        
        #create a control
        self.control = ControlView(parent)

        #add buttons
        self.save_machine = ttk.Button(self.control, text="save machine", command=self.save_machine_click)
        self.save_machine.grid(row=0, column=0, sticky=EW)

        self.copy_regex = ttk.Button(self.control, text="copy RegEx", command=self.copy_regex_click)
        self.copy_regex.grid(row = 1, column=0, sticky=EW)

        #pack the display and control
        self.pack(side= TOP, padx=20, pady=20)

        # set the controller
        self.controller = None
    def save_machine_click(self):
        print("save machine")
        pass
    def copy_regex_click(self):
        print("copy RegEx")
        pass
    def update_diagram(self, image):
        if self.control:
            #add widgets
            self.img = ImageTk.PhotoImage(Image.open(image))
            self.graph_diagram = Label(self.display,image=self.img)#.pack(side=LEFT, fill=BOTH, expand=True)
            self.graph_diagram.grid(row=1,column=0, sticky=EW)


    def show_error(self, message):
        messagebox.showerror(title="error",message=message)

class DisplayView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent
        self.pack(side = LEFT)

class ControlView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.master = parent
        self.pack(side = RIGHT)
