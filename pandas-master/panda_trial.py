import pandas as pd

df = pd.read_csv("pokemon_data.csv")

df["Ovr. Atk"] = df["Attack"] + df["Sp. Atk"]

print(df.sort_values(["Ovr. Atk"], ascending = False))