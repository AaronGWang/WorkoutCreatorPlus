import pandas as pd
import random
import clipboard
from module import generate_upper_split, generate_core_split, print_main_set, print_core_set

df_1 = pd.read_csv('Exercises/Arms.csv')
df_2 = pd.read_csv('Exercises/Push_Pull.csv')
df_3 = pd.read_csv('Exercises/Compound.csv')
df_5 = pd.read_csv('Exercises/Core.csv')

upper_data = generate_upper_split(area_1_dataframe=df_1, 
                                  area_2_dataframe=df_2, 
                                  compound_dataframe=df_3)
core_data = generate_core_split(core_dataframe=df_5)
random.shuffle(upper_data)

upper = print_main_set(upper_data)
core = print_core_set(core_data)

full = f'{upper}\n\n{core}'
clipboard.copy(full)