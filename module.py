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


def choose_exercise(area_df: pd.DataFrame, area_df_list: list):
  '''
  This function chooses random exercises from the arms dataframe.
  
  Args:
    area_df (pd.DataFrame): The dataframe for the area.
    arms_df_list (list): A list of dataframes for the arms area.

  Returns:
    exercises (list): A list of exercises for the area (each has "Index", "Name", "Area", "Weight", "Rep_num", "RIR", and "Instructions").
  '''
  exercises = []

  for i in range(len(area_df_list)):
    exercise = area_df.loc[area_df['Area'] == area_df_list[i]['Area'].values[0]].sample(n=1)
    exercises.append(exercise)

  return exercises


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
    upper_split (list): A list of ordered upper body exercises in this order: [Biceps, Shoulders, Triceps, Back, Compound].
  '''

  upper_split = []

  arms_dataframe_list = create_unique_dataframes(df=area_1_dataframe)
  push_pull_dataframe_list = create_unique_dataframes(df=area_2_dataframe)

  arm_exercises = choose_exercise(area_df=area_1_dataframe,
                                        area_df_list=arms_dataframe_list)

  push_pull_exercises = choose_exercise(area_df=area_2_dataframe,
                                              area_df_list=push_pull_dataframe_list)

  compound_exercise = compound_dataframe.loc[compound_dataframe['Area'] == 'Upper'].sample(n=1)

  for arm, push_pull in zip(arm_exercises, push_pull_exercises):
      upper_split.extend([arm, push_pull])

  upper_split.append(compound_exercise)

  return upper_split


def generate_lower_split(area_3_dataframe: pd.DataFrame, compound_dataframe: pd.DataFrame):
  '''
  This function generates the lower split section of the workout.

  Args:
    area_3_dataframe (pd.DataFrame): A dataframe for the third area.
    compound_dataframe (pd.DataFrame): A dataframe for the compound exercises.

  Returns:
    lower_split (list): A list of ordered lower body exercises in this order: [Quands, Calves, Glutes, Hamstrings, Compound].
  '''

  lower_split = []

  leg_dataframe_list = create_unique_dataframes(df=area_3_dataframe)
  leg_exercises = choose_exercise(area_df=area_3_dataframe,
                                  area_df_list=leg_dataframe_list)

  compound_exercise = compound_dataframe.loc[compound_dataframe['Area'] == 'Lower'].sample(n=1)

  lower_split = leg_exercises.copy()
  lower_split.append(compound_exercise)

  return lower_split


def generate_core_split(core_dataframe: pd.DataFrame):
  '''
  This function generates the core split section of the workout.

  Args:
    core_dataframe (pd.Dataframe): A dataframe for core.

  Returns:
    core_split (list): A list of ordered core exercises in this order: [Abs, Obliques, Abs, LB & Balance], intensity alternates between exercises.
  '''
  core_split = []

  intensity_values = list(core_dataframe['Intensity'].unique())
  area_values = list(core_dataframe['Area'].unique())

  exercise_1 = core_dataframe.loc[core_dataframe['Area'] == area_values[0]].sample(n=1)
  core_split.append(exercise_1)

  if exercise_1['Intensity'].item() == 1:
    exercise_2 = core_dataframe.loc[(core_dataframe['Area'] == area_values[1]) & (core_dataframe['Intensity'] == 2)].sample(n=1)
    core_split.append(exercise_2)
    exercise_3 = core_dataframe.loc[(core_dataframe['Area'] == area_values[0]) & (core_dataframe['Intensity'] == 1)].sample(n=1)
    core_split.append(exercise_3)
    exercise_4 = core_dataframe.loc[(core_dataframe['Area'] == area_values[2]) & (core_dataframe['Intensity'] == 2)].sample(n=1)
    core_split.append(exercise_4)

  else:
    exercise_2 = core_dataframe.loc[(core_dataframe['Area'] == area_values[1]) & (core_dataframe['Intensity'] == 1)].sample(n=1)
    core_split.append(exercise_2)
    exercise_3 = core_dataframe.loc[(core_dataframe['Area'] == area_values[0]) & (core_dataframe['Intensity'] == 2)].sample(n=1)
    core_split.append(exercise_3)
    exercise_4 = core_dataframe.loc[(core_dataframe['Area'] == area_values[2]) & (core_dataframe['Intensity'] == 1)].sample(n=1)
    core_split.append(exercise_4)
  
  return core_split