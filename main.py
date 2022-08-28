# To see the simulation interface

from visualization import server

server.launch()

# Batch run experiments

from model import ColorModel
import mesa
import pandas as pd


params = {"width": 20, "height": 20, "N": 200}

results = mesa.batch_run(
    ColorModel,
    parameters=params,
    iterations=50,
    max_steps=500,
    number_processes=1,
    data_collection_period=1,
    display_progress=True,
)

results_df = pd.DataFrame(results)

results_df.to_csv("data.csv")

print(results_df)