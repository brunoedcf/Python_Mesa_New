from mesa.visualization.modules import CanvasGrid, ChartModule, PieChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

from model import ColorModel

COLORS = {'1': '#8700ff', '2': '#ffad00', '3': '#ff3377', '4': '#bdff00', '5': '#aa2585'}

def color_influence_portrayal(agent):
    if agent is None:
        return
    portrayal = {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Layer": 0}
    (x, y) = agent.pos
    portrayal["x"] = x
    portrayal["y"] = y
    portrayal["Color"] = COLORS[agent.color]
    return portrayal


canvas_element = CanvasGrid(color_influence_portrayal, 20, 20, 500, 500)
agent_chart = ChartModule(
    [{"Label": label, "Color": color} for (label, color) in COLORS.items()]
)
pie_chart = PieChartModule(
    [{"Label": label, "Color": color} for (label, color) in COLORS.items()]
)

model_params = {
    "N": 200,
    "height": 20,
    "width": 20,
    "probability": UserSettableParameter("slider", "Probability", 95, 0, 100, 1),
}
server = ModularServer(
    ColorModel, [canvas_element, agent_chart, pie_chart], "Color Influence", model_params
)