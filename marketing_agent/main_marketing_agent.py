from bbdd_manager.Mongo_manager import Mongo_manager
from bbdd_manager import ConfigVariablesBbdd
from marketing_agent.Agent_orchestrator import Agent_orchestrator
import matplotlib.pyplot as plt
from pylab import *
import common_tools.save as save

# Creamos una conexion a la BBDD
bbdd_connec = Mongo_manager(ConfigVariablesBbdd.env_database)

# Creamos una accion
test_orch = Agent_orchestrator(bbdd_connec)
# CASE 1 - 180 Iterations, 120 number of agents, 0.05 error, 0 initial_estimate
list_of_results = test_orch.run(180,120,0.01,2)
save.from_list_to_file(list_of_results,'save_results/test_180_120_001_2.csv')
x_axis = range(len(list_of_results))
plt.plot(list_of_results)
# CASE 2 - 180 Iterations, 120 number of agents, 0.01 error, 0 initial_estimate
list_of_results1 = test_orch.run(180,120,0.05,2)
save.from_list_to_file(list_of_results1,'save_results/test_180_120_005_2.csv')
x_axis1 = range(len(list_of_results1))
plt.plot(list_of_results1)
# CASE 3 - 180 Iterations, 120 number of agents, 0.05 error, 2 initial_estimate
list_of_results2 = test_orch.run(180,120,0.10,2)
save.from_list_to_file(list_of_results2,'save_results/test_180_120_010_2.csv')
x_axis2 = range(len(list_of_results2))
plt.plot(list_of_results2)

show()


