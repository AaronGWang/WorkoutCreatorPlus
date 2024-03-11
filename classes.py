import pandas as pd
import random
class main_set_split():
  '''
  This class creates the main set based on a type of split. 

  Parameters:
  split_type (dict): The type of split to be used.
  set_num (int): The number of sets of each workout.
  num_per_set (int): The number of exercises per set.
  area_1 (str): The first area of the first split.
  area_2 (str): The second area of the first split.
  area_3 (str): The area of the second split.
  '''
  def __init__(self, split_type, set_num, num_per_set):
    self.split_type = split_type
    self.set_num = set_num
    self.num_per_set = num_per_set
    self.split_1 = list(split_type.keys())[0]
    self.split_2 = list(split_type.keys())[1]
    self.area_1 = list(split_type.values())[0][0]
    self.area_2 = list(split_type.values())[0][1]
    self.area_3 = list(split_type.values())[1]

  def create_first_set(self):
    '''
    This method creates the first set of the workout. 
    '''
    area_1_df = pd.read_csv(f'Exercises/{self.area_1}.csv')
    area_2_df = pd.read_csv(f'Exercises/{self.area_2}.csv')

    ridx_1 = random.sample(len(area_1_df), k=3)
    print(area_1_df[ridx_1])

    
