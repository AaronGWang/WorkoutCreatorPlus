import pandas as pd
import random
import clipboard
from module import generate_lower_split, generate_core_split, print_main_set, print_core_set

df_3 = pd.read_csv('Exercises/Compound.csv')
df_4 = pd.read_csv('Exercises/Legs.csv')
df_5 = pd.read_csv('Exercises/Core.csv')

lower_data = generate_lower_split(area_3_dataframe=df_4, 
                                  compound_dataframe=df_3)
core_data = generate_core_split(core_dataframe=df_5)
random.shuffle(lower_data)

lower = print_main_set(lower_data)
core = print_core_set(core_data)
full = f"{lower}\n\n{core}"
clipboard.copy(full)