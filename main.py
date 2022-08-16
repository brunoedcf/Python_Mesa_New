# from visualization import server

# server.launch()


from model import ColorModel
import mesa
import pandas as pd

import matplotlib.pyplot as plt

params = {"width": 20, "height": 20, "N": 200}

results = mesa.batch_run(
    ColorModel,
    parameters=params,
    iterations=5,
    max_steps=100,
    number_processes=1,
    data_collection_period=1,
    display_progress=True,
)

results_df = pd.DataFrame(results)

print(results_df)