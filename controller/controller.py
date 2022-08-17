from model.automata import NondeterministicFiniteAutomata as NFA
from view.view import MainView
import graphviz
class Controller:
    def __init__(self, model:NFA, view:MainView) -> None:
        self.model = model
        self.view = view
    
    def add_state(self, label:str):
        self.model.add_state(label = label)
        self.view.input.update_display(self.model.get_states())
        print(self.model.get_states())
        


    def build(self):        
        #graphiz test
        f = graphviz.Digraph('finite_state_machine', filename='fsm')
        f.attr(rankdir='LR', size='8,5')

        f.attr('node', shape='doublecircle')
        f.node('LR_2')
        

        f.attr('node', shape='circle')
        f.edge('LR_0', 'LR_0', label='0,1')
        f.edge('LR_0', 'LR_1', label='1')
        f.edge('LR_1', 'LR_2', label='0,1')

        self.view.output.update_diagram(image = f.render(format='png'))

    