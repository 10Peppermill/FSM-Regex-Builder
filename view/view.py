import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
#!/usr/bin/env python3
import graphviz

class MainView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        #create LabelFram
        labelframeinput = LabelFrame(master=parent, text="InputView")
        labelframeinput.pack(fill=BOTH, expand=True)

        #create LabelFram
        labelframeoutput = LabelFrame(master=parent, text="OutputView")
        labelframeoutput.pack(fill="both", expand="yes")

        input = InputView(labelframeinput)
        output = OutputView(labelframeoutput)
        self.pack(padx=20, pady=20)

class InputView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #create a Display
        self.display = DisplayView(parent)

        #add widgets
        self.Epsilon = ttk.Label(master=self.display, text="E:", justify=LEFT)
        self.Epsilon_var = tk.StringVar()
        self.Epsilon_post = ttk.Entry(master=self.display, textvariable=self.Epsilon_var)
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

        #create a control
        self.control = ControlView(parent)

        #add buttons
        self.enter_alphabet = ttk.Button(self.control, text="set alphabet", command=self.enter_alphabet_click)
        self.enter_alphabet.grid(row=0, column=0)

        self.add_state = ttk.Button(self.control, text="add state", command=self.add_state_click)
        self.add_state.grid(row=0, column=1)

        self.set_start = ttk.Button(self.control, text="set start", command=self.set_start_click)
        self.set_start.grid(row = 1, column = 0)

        self.set_Final = ttk.Button(self.control, text="set final", command=self.set_final_click)
        self.set_Final.grid(row = 1, column = 1)

        self.build = ttk.Button(self.control, text="build", command=self.build_click)
        self.build.grid(row = 2, columnspan=2, sticky=EW)

        #pack the display and control
        self.pack(side= TOP, padx=20, pady=20)

        # set the controller
        self.controller = None

    def enter_alphabet_click(self):
        print(self.Epsilon_var.get())
        pass
    def add_state_click(self):
        print("add state")
        pass
    def set_start_click(self):
        print("set start")
        pass
    def set_final_click(self):
        print("set final")
        pass

    def build_click(self):
        print("build")
        #graphiz test
        f = graphviz.Digraph('finite_state_machine', filename='fsm')
        f.attr(rankdir='LR', size='8,5')

        f.attr('node', shape='doublecircle')
        f.node('LR_2')
        

        f.attr('node', shape='circle')
        f.edge('LR_0', 'LR_0', label='0,1')
        f.edge('LR_0', 'LR_1', label='1')
        f.edge('LR_1', 'LR_2', label='0,1')


        #f.view(filename="fsm.gv.png")
        f.render(format='png')
    def show_error(self, message):
        messagebox.showerror(title="error",message=message)



class OutputView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #create a Display
        self.display = DisplayView(parent)

        #grahphiz

        #add widgets
        self.img = ImageTk.PhotoImage(Image.open('fsm.png'))
        self.graph_diagram = Label(self.display,image=self.img)#.pack(side=LEFT, fill=BOTH, expand=True)
        self.graph_diagram.grid(row=1,column=0, sticky=EW)

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