import pandas as pd
import random

def create_unique_dataframes(df: pd.DataFrame):
  '''
  This function creates unique dataframes based on the unique values of the "Area" column in a dataframe.

  Args:
    df (pd.DataFrame): The dataframe to be used (the broad area dataframe, e.g. Arms.csv).

  Returns:
    list: A list of dataframes based on the unique values of the "Area" column.
  '''
  dataframes = []

  unique_values = df['Area'].unique()

  for value in unique_values:
    new_df = df.loc[df['Area'] == value]
    dataframes.append(new_df)

  return dataframes


def choose_arms_exercises(area_1_dataframe: pd.DataFrame, arms_dataframe_list: list):
  '''
  This function chooses random exercises from the arms dataframe.
  
  Args:
    area_1_dataframe (pd.DataFrame): The dataframe for the first area.
    arms_dataframe_list (list): A list of dataframes for the arms area.

  Returns:
    list: A list of exercises for the arms (each has "Index", "Name", "Area", "Weight", "Rep_num", "RIR", and "Instructions").
  '''
  arm_exercises = []

  for i in range(len(arms_dataframe_list)):
    exercise = area_1_dataframe.loc[random.choice(list(arms_dataframe_list[i]['Index'])) - 1]
    arm_exercises.append(exercise)

  return arm_exercises


def choose_push_pull_exercises(area_2_dataframe: pd.DataFrame, push_pull_dataframe_list: list):
  '''
  This function chooses random exercises from the push/pull dataframe.

  Args:
    area_2_dataframe (pd.DataFrame): The dataframe for the second area.
    push_pull_dataframe_list (list): A list of dataframes for the push/pull area.

  Returns:
    list: A list of exercises for the push/pull (each has "Index", "Name", "Area", "Weight", "Rep_num", "RIR", and "Instructions").
  '''
  push_pull_exercises = []

  for i in range(len(push_pull_dataframe_list)):
    exercise = area_2_dataframe.loc[random.choice(list(push_pull_dataframe_list[i]['Index'])) - 1]
    push_pull_exercises.append(exercise)

  return push_pull_exercises


def generate_upper_split(area_1_dataframe: pd.DataFrame,
                         area_2_dataframe: pd.DataFrame,
                         compound_dataframe: pd.DataFrame):
  '''
  This function generates the upper split section of the workout.

  Args:
    area_1_dataframe (pd.DataFrame): A dataframe for the first area.
    area_2_dataframe (pd.DataFrame): A dataframe for the second area.
    compound_dataframe (pd.DataFrame): A dataframe for the compound exercises.

  Returns:
    list: A list of exercises for the upper split workout.
  '''

  upper_split = []

  arms_dataframe_list = create_unique_dataframes(df=area_1_dataframe)
  push_pull_dataframe_list = create_unique_dataframes(df=area_2_dataframe)

  arm_exercises = choose_arms_exercises(area_1_dataframe=area_1_dataframe, arms_dataframe_list=arms_dataframe_list)

  push_pull_exercises = choose_push_pull_exercises(area_2_dataframe=area_2_dataframe, push_pull_dataframe_list=push_pull_dataframe_list)

  compound_upper_exercises = compound_dataframe.loc[compound_dataframe['Area'] == 'Upper']
  compound_exercise = compound_dataframe.loc[random.choice(list(compound_upper_exercises['Index'])) - 1]

  for arm, push_pull in zip(arm_exercises, push_pull_exercises):
      upper_split.extend([arm, push_pull])

  upper_split.append(compound_exercise)

  return upper_split
  


  