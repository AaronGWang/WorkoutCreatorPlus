import pandas as pd
import random

def create_unique_dataframes(df: pd.DataFrame, dataframes: list):
  '''
  This function creates unique dataframes based on the unique values of the "Area" column in a dataframe.

  Args:
    df (pd.DataFrame): The dataframe to be used.
    dataframes (empty list): A list to store the unique dataframes.

  Returns:
    list: A list of dataframes based on the unique values of the "Area" column.
  '''
  unique_values = df['Area'].unique()

  for value in unique_values:
    new_df = df.loc[df['Area'] == value]
    dataframes.append(new_df)

  return dataframes

