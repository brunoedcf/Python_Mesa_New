import mesa
import mesa.time
import mesa.space


class MoneyAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 50
        self.broke = False
        self.step_counter = 0

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def give_money(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = self.random.choice(cellmates)
            other.wealth += 1
            self.wealth -= 1

    def step(self):
        # The agent's step will go here.
        # For demonstration purposes we will print the agent's unique_id

        self.move()

        if self.broke != True:

            if self.step_counter % 5 != 0:
                self.give_money()
                self.step_counter += 1

            else:
                print(f"I, agent {self.unique_id} am in PAYDAY {int(self.step_counter / 5)} and have {self.wealth} money.")
                self.wealth -= 2
                if self.wealth < 0:
                    self.broke = True
                    print(f"    Agent {self.unique_id} is now broke")

                self.step_counter += 1

        else: 
             print(f"    Agent {self.unique_id} is broke")
             self.step_counter += 1


class MoneyModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, N, width, height):
        self.num_agents = N ### NUMBER OF AGENTS
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))


    def step(self):

        """Advance the model by one step."""
        self.schedule.step()
