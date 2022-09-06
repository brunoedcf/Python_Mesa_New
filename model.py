from turtle import color
import mesa
import mesa.time
import mesa.space
from mesa.datacollection import DataCollector
from agents import ColorAgent

def compute_diff(model):
    colors = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0
    }

    for agent in model.schedule.agents:
        colors[agent.color] += 1

    c = list(colors.values())
    diff = max(c) - min(c)

    return diff

class ColorModel(mesa.Model):

    def __init__(self, N, width, height, probability):

        self.num_agents = N 
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.probability = probability
        self.count_steps = 0

        self.datacollector = DataCollector(
            {
                "1": lambda m: self.count_type(m, "1"),
                "2": lambda m: self.count_type(m, "2"),
                "3": lambda m: self.count_type(m, "3"),
                "4": lambda m: self.count_type(m, "4"),
                "5": lambda m: self.count_type(m, "5"),
                "diff": lambda m: compute_diff(self)
            }
        )

        # Create agents
        for i in range(self.num_agents):

            if i % 5 == 0:
                a = ColorAgent(i, self, '1')
            elif i % 5 == 1:
                a = ColorAgent(i, self, '2')
            elif i % 5 == 2:
                a = ColorAgent(i, self, '3')
            elif i % 5 == 3:
                a = ColorAgent(i, self, '4')
            elif i % 5 == 4:
                a = ColorAgent(i, self, '5')

            self.schedule.add(a)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)

            self.grid.place_agent(a, (x, y))

        self.running = True
        self.datacollector.collect(self)

    def step(self):

        self.schedule.step()
        self.datacollector.collect(self)
        self.count_steps += 1

        # if self.count_steps >= 100:
        #     self.running = False
        #     diff = self.datacollector.get_model_vars_dataframe()
        #     diff.to_csv("data.csv")
        #     return


    @staticmethod
    def count_type(model, agent_color):

        count = 0

        for agent in model.schedule.agents:
            if agent.color == agent_color:
                count += 1

        return count