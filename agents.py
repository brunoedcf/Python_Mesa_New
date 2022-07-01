import mesa
import mesa.time
import mesa.space
import random

colors = ['1', '2', '3', '4', '5']

class ColorAgent(mesa.Agent):

    def __init__(self, unique_id, model):

        super().__init__(unique_id, model)

        self.color = random.choice(colors)

        print(f"Minha cor é {self.color}: Agente {self.unique_id}")

    def move(self):

        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )

        new_position = self.random.choice(possible_steps)

        self.model.grid.move_agent(self, new_position)

    def change_color(self):

        cellmates = self.model.grid.get_cell_list_contents([self.pos])

        if len(cellmates) > 1:
            
            other_agent = self.random.choice(cellmates)

            while(other_agent == self):
                other_agent = self.random.choice(cellmates)
            
            other_agent.color = self.color

        
    def step(self):

        self.move()

        self.change_color()