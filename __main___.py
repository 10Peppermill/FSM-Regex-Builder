import tkinter as tk
from model.automata import NondeterministicFiniteAutomata as NFA
from view.view import MainView
from controller.controller import Controller

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('FSM Regex Builder')

        #create a model
        model = NFA()

        # create a view and place it on the root window
        view = MainView(self)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
