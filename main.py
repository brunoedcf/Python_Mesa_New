from model_agents import MoneyModel
import matplotlib.pyplot as plt
import numpy as np

agent_wealth = []

for j in range(5):
    Model = MoneyModel(100, 10, 10)

    for i in range(100):
        Model.step()

    agent_wealth += ([{a.wealth, a.unique_id} for a in Model.schedule.agents])


print(agent_wealth)
plt.hist(agent_wealth)
plt.title("Histogram")
plt.show()
plt.show()