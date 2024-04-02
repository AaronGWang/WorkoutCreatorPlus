def main(split_type: str, shuffle: str='yes', main_instructions: str='no', core_instructions: str='no'):
  '''
  This function generates a workout split based on the user's input and copies it to the clipboard.

  Args:
    split_type (str): The type of workout split to generate. Must be either "upper" or "lower".
    shuffle (str): Whether or not to shuffle the exercises. Defaults to "yes".
    main_instructions (str): Whether or not to include instructions for the main exercises. Defaults to "no".
    core_instructions (str): Whether or not to include instructions for the core exercises. Defaults to "no".

  Returns:
    str: A message indicating that the workout split has been copied to the clipboard.
    (The workout split is also copied to the clipboard.)
  '''

  # Imports
  import pandas as pd
  import random
  import clipboard
  from module import generate_lower_split, generate_upper_split, generate_core_split, print_main_set, print_core_set, check_status
  
  # Load csv files
  df_1 = pd.read_csv('Exercises/Arms.csv')
  df_2 = pd.read_csv('Exercises/Push_Pull.csv')
  df_3 = pd.read_csv('Exercises/Compound.csv')
  df_4 = pd.read_csv('Exercises/Legs.csv')
  df_5 = pd.read_csv('Exercises/Core.csv')

  # Upper split generator
  if split_type.upper() == 'UPPER':
    # Check status from inputs
    string = check_status(split_type.lower(), shuffle, main_instructions, core_instructions)

    # Generate Exercises
    upper_data = generate_upper_split(area_1_dataframe=df_1, 
                                      area_2_dataframe=df_2, 
                                      compound_dataframe=df_3)
    core_data = generate_core_split(core_dataframe=df_5)

    # Shuffle / no shuffle
    if shuffle == 'yes':
      random.shuffle(upper_data)
    else:
      None

    # Organize exercises into rows
    upper = print_main_set(upper_data, split='upper', instructions=main_instructions)
    core = print_core_set(core_data, instructions=core_instructions)
  
    # Combine and copy to clipboard
    full = f'{upper}\n\n{core}'
    clipboard.copy(full)

    # Print confirmation message
    print(string)


  # Lower split generator
  elif split_type.upper() == 'LOWER':
    # Check status from inputs
    string = check_status(split_type.lower(), shuffle, main_instructions, core_instructions)

    # Generate Exercises
    lower_data = generate_lower_split(area_3_dataframe=df_4, 
                                        compound_dataframe=df_3)
    core_data = generate_core_split(core_dataframe=df_5)

    # Shuffle / no shuffle
    if shuffle == 'yes':
      random.shuffle(lower_data)
    else:
      None

    # Organize exercises into rows
    lower = print_main_set(lower_data, split='lower', instructions=main_instructions)
    core = print_core_set(core_data, instructions=core_instructions)

    # Combine and copy to clipboard
    full = f"{lower}\n\n{core}"
    clipboard.copy(full)

    # Print confirmation message
    print(string)

  # Invalid split type
  else:
    print('Invalid split type. Please enter either "upper" or "lower".')


# Command line arguments
import sys
if __name__ == '__main__':
    if len(sys.argv) > 1:
        split_type = sys.argv[1]
        shuffle = sys.argv[2] if len(sys.argv) > 2 else 'yes'
        main_instructions = sys.argv[3] if len(sys.argv) > 3 else 'no'
        core_instructions = sys.argv[4] if len(sys.argv) > 4 else 'no'
        main(split_type, shuffle, main_instructions, core_instructions)
    else:
        print('Invalid number of arguments. Please provide a correct split type.')