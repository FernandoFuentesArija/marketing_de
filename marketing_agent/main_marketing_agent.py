from bbdd_manager.Mongo_manager import Mongo_manager
from bbdd_manager import ConfigVariablesBbdd
from marketing_agent.Agent_orchestrator import Agent_orchestrator
import matplotlib.pyplot as plt
from pylab import *

# Creamos una conexion a la BBDD
bbdd_connec = Mongo_manager(ConfigVariablesBbdd.env_database)

# Creamos una accion
test_orch = Agent_orchestrator(bbdd_connec)
# Iterations, number of agents, error
list_of_results = test_orch.run(180,120,0.05)
x_axis = range(len(list_of_results))
plt.plot(list_of_results)
list_of_results1 = test_orch.run(180,120,0.01)
x_axis1 = range(len(list_of_results1))
plt.plot(list_of_results1)
list_of_results2 = test_orch.run(180,120,0.01,2)
x_axis2 = range(len(list_of_results2))
plt.plot(list_of_results2)

show()


