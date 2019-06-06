import pandas as pd
import random
import os
import subprocess
from environment_manager import main_env_manager
import datetime


print("Tiempo: " + str(datetime.datetime.now()))
action_list = ["action1","action2","action3","action4","action5"]
cont = 1
Qk_list = [5,8,8,3,6]
k_list = [1,1,1,1,1]
alpha_list = [0,0,0,0,0]
id_list = [1,2,3,4,5]


action_df = pd.DataFrame({"action":action_list,
                          "Qk":Qk_list,
                          "k":k_list,
                          "alpha":alpha_list},
                         index=id_list)
print(action_df )
print('----------------')

# We obtain the max prediction of reward Qk
Qk_max = action_df['Qk'].max()
# We search in the df if we have more than one max
filter_action_df = action_df[action_df.Qk == Qk_max]
print(filter_action_df)
print('----------------')
original_index = filter_action_df.index
print(original_index)
print('----------------')
# We reset the index of the new df
filter_action_df_res = filter_action_df.reset_index(drop=True)
print(filter_action_df_res)
print('----------------')
new_index = filter_action_df_res.index
print(new_index)
print('----------------')
# We generate a random index to select only one row
new_sel_id = random.randint(0, len(filter_action_df_res) - 1)
print('Sel new index: ' + str(new_sel_id))
old_sel_id = original_index[new_sel_id]
print('Sel orig index: ' + str(old_sel_id))
# We select the row
#max_row = filter_action_df_res.loc[sel_id, :]

#action_df.at[4,'Qk']=20
#print(action_df)
print(datetime.datetime.now())

print(random.random())







