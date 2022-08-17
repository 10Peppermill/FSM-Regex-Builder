import tkinter as tk
from model.automata import NondeterministicFiniteAutomata as NFA
from view.view import MainView
from controller.controller import Controller

from model.state import State
from model.transition import Transition 
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('FSM Regex Builder')

        #create a model
        model = NFA(symbol_Epsilon=set(), symbol_Q=set(),symbol_q_0=None,symbol_F=set())

        # create a view and place it on the root window
        view = MainView(self)
        #view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
