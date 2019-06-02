import pandas as pd
import random
import os
import subprocess
from environment_manager import main_env_manager

action_list = ["action1","action2","action3","action4","action5"]
cont = 1
Qk_list = []
k_list = []
alpha_list = []
id_list = []

for i in range(len(action_list)):
    Qk_list.append(random.randint(0,10))
    k_list.append(1)
    alpha_list.append(0)
    id_list.append(cont)
    cont = cont + 1

action_df = pd.DataFrame({"action":action_list,
                          "Qk":Qk_list,
                          "k":k_list,
                          "alpha":alpha_list},
                         index=id_list)

print(action_df)

my_list1 = ['primero','segundo','tercero']
my_list2 = []
for elemnt in my_list1:
    a = elemnt
    my_list2.append(a)
print(my_list2)

#dir_actual = os.getcwd()
#ruta_rel = "../environment_manager/main_env_manager.py"
#ruta_good = os.path.join(dir_actual,ruta_rel)
#os.system(ruta_good)
#process1 = subprocess.Popen(['python', "../environment_manager/main_env_manager.py"])
#retcode = subprocess.call(["../environment_manager/main_env_manager.py"])
main_env_manager.run()


