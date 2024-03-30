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
  random_seed = random.randint(1, 1000)

  exercises = []

  for i in range(len(area_df_list)):
    exercise = area_df.loc[area_df['Area'] == area_df_list[i]['Area'].values[0]].sample(n=1, random_state=random_seed)
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
    upper_split (list): A list of ordered upper body exercises in this order: [Biceps, Triceps, Shoulders, Back, Chest, Compound].
  '''

  upper_split = []

  arms_dataframe_list = create_unique_dataframes(df=area_1_dataframe)
  push_pull_dataframe_list = create_unique_dataframes(df=area_2_dataframe)

  arm_exercises = choose_exercise(area_df=area_1_dataframe,
                                        area_df_list=arms_dataframe_list)

  push_pull_exercises = choose_exercise(area_df=area_2_dataframe,
                                              area_df_list=push_pull_dataframe_list)

  compound_exercise = compound_dataframe.loc[compound_dataframe['Area'] == 'Upper'].sample(n=1)
  compound_exercise['Area'] = 'Compound'

  upper_split = arm_exercises + push_pull_exercises

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

  compound_exercise['Area'] = 'Compound'

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

    filtered_df = core_dataframe[core_dataframe['Name'] != exercise_1['Name'].item()]

    exercise_3 = filtered_df.loc[(core_dataframe['Area'] == area_values[0]) & (core_dataframe['Intensity'] == 1)].sample(n=1)
    core_split.append(exercise_3)

    exercise_4 = core_dataframe.loc[(core_dataframe['Area'] == area_values[2]) & (core_dataframe['Intensity'] == 2)].sample(n=1)
    core_split.append(exercise_4)

  else:
    exercise_2 = core_dataframe.loc[(core_dataframe['Area'] == area_values[1]) & (core_dataframe['Intensity'] == 1)].sample(n=1)
    core_split.append(exercise_2)

    filtered_df = core_dataframe[core_dataframe['Name'] != exercise_1['Name'].item()]

    exercise_3 = filtered_df.loc[(core_dataframe['Area'] == area_values[0]) & (core_dataframe['Intensity'] == 2)].sample(n=1)
    core_split.append(exercise_3)

    exercise_4 = core_dataframe.loc[(core_dataframe['Area'] == area_values[2]) & (core_dataframe['Intensity'] == 1)].sample(n=1)
    core_split.append(exercise_4)
  
  return core_split


def generate_main_set_focus(upper_data: pd.DataFrame):
  '''
  This function generates the focus of the workout based on the upper body data.

  Args:
    upper_data (pd.DataFrame): The upper body data, including weight, rep_num & RIR

  Returns:
    focus (str): The focus of the workout.
  '''
  if upper_data['Weight'].item() == 0:
    weight = 'low weight'
  elif upper_data['Weight'].item() == 1:
    weight = 'medium weight'
  else:
    weight = 'heavy weight'

  if upper_data['Rep_num'].item() == 0:
    rep_num = 'low reps'
  elif upper_data['Rep_num'].item() == 1:
    rep_num = 'medium reps'
  else:
    rep_num = 'high reps'

  if upper_data['RIR'].item() == 0:
    RIR = 'with no reps in reserve'
  else:
    RIR = 'with reps in reserve'

  return f"Focus on {weight} for {rep_num}, {RIR}"


def print_main_set(data: list):
  '''
  This function prints the set based on the data.

  Args:
    data (list): The data to be printed.

  Returns:
    workout (str): organized lines of text about every exercise.
  '''
  string = str('---------\n\n')

  for i in range(len(data)):
    line = str(f"Exercise: {data[i]['Name'].to_string(index=False)} | Area: {data[i]['Area'].to_string(index=False)} | {generate_main_set_focus(data[i])}")
    string += line + '\n' + '\n'

  string += str('---------')

  return string


def generate_core_focus(core_data: pd.DataFrame):
  '''
  This function generates the focus of the workout based on the core data.

  Args:
    core_data (pd.DataFrame): The core data, including weight, rep_num & RIR

  Returns:
    focus (str): The focus of the workout.
  '''
  if core_data['Weight'].item() == 0:
    weight = 'low weight'
  elif core_data['Weight'].item() == 1:
    weight = 'medium weight'
  else:
    weight = 'heavy weight'

  if core_data['Intensity'].item() == 1:
    intensity = 'low-intensity'
  else:
    intensity = 'high-intensity'

  return f"This is a {intensity} exercise. Focus on {weight}"


def print_core_set(data: list):
  '''
  This function prints the core set based on the data.

  Args:
    data (list): The data to be printed.

  Returns:
    workout (str): organized lines of text about every exercise.
  '''
  string = ''

  for i in range(len(data)):
    line = str(f"Exercise: {data[i]['Name'].to_string(index=False)} | Area: {data[i]['Area'].to_string(index=False)} | {generate_core_focus(data[i])} for {data[i]['Rep_num'].to_string(index=False)} {data[i]['Unit'].to_string(index=False)}")
    string += line + '\n' + '\n'
  
  string += str('---------')

  return string