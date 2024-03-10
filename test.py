import pandas as pd

df = pd.read_csv('Legs.csv')

grouped = df.groupby('Area')

dataframes = {}
for area, group in grouped:
    dataframes['Area'] = group.copy()

for area, dataframe in dataframes.items():
    print(f"Dataframe for area '{area}':")
    print(dataframe)
    print()