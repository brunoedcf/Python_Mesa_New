import mesa
import mesa.time
import mesa.space
import random

colors = {
    '1':'1',
    '2':'2',
    '3':'3',
    '4':'4',
    '5':'5',
}

class ColorAgent(mesa.Agent):

    def __init__(self, unique_id, model, clr):

        super().__init__(unique_id, model)

        self.color = colors[clr];

    def move(self):

        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )

        new_position = self.random.choice(possible_steps)

        self.model.grid.move_agent(self, new_position)

    def change_color(self):

        chance_of_change = random.randint(1, 100)

        if chance_of_change <= self.model.probability:

            cellmates = self.model.grid.get_cell_list_contents([self.pos])

            if len(cellmates) > 1:
                
                other_agent = self.random.choice(cellmates)

                while(other_agent == self):
                    other_agent = self.random.choice(cellmates)
                
                other_agent.color = self.color

        else:

            self.color = colors[str(random.randint(1, 5))]

        
    def step(self):

        self.move()

        self.change_color()