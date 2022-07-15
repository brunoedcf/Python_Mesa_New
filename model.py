import mesa
import mesa.time
import mesa.space
from mesa.datacollection import DataCollector
from agents import ColorAgent


class ColorModel(mesa.Model):

    def __init__(self, N, width, height, probability = 95):

        self.num_agents = N 
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.probability = probability

        self.datacollector = DataCollector(
            {
                "1": lambda m: self.count_type(m, "1"),
                "2": lambda m: self.count_type(m, "2"),
                "3": lambda m: self.count_type(m, "3"),
                "4": lambda m: self.count_type(m, "4"),
                "5": lambda m: self.count_type(m, "5"),
            }
        )

        # Create agents
        for i in range(self.num_agents):

            a = ColorAgent(i, self)

            self.schedule.add(a)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)

            self.grid.place_agent(a, (x, y))

        self.running = True
        self.datacollector.collect(self)

    def step(self):

        self.schedule.step()
        self.datacollector.collect(self)


    @staticmethod
    def count_type(model, agent_color):

        count = 0

        for agent in model.schedule.agents:
            if agent.color == agent_color:
                count += 1

        return count