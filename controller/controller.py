from model.automata import NondeterministicFiniteAutomata as NFA
from view.view import MainView
import graphviz
class Controller:
    def __init__(self, model:NFA, view:MainView) -> None:
        self.model = model
        self.view = view
    
    def add_state(self, label:str):
        self.model.add_state(label = label)
        self.view.input.update_display("states", self.model.get_states())
    
    def del_state(self, label:str):
        self.model.del_state(label = label)
        self.view.input.update_display("states", self.model.get_states())

    def set_alphabet(self, alphabet:str):
        self.model.set_alphabet(alphabet)
        self.view.input.update_display("alphabet",self.model.get_alphabet())

    def set_inital(self, label:str):
        self.model.set_inital(label)
        state = self.model.get_inital().label
        self.view.input.update_display("inital", state)

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

    