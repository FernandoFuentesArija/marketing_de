from bbdd_manager.Mongo_manager import Mongo_manager
from bbdd_manager import ConfigVariablesBbdd
from marketing_agent.Agent_orchestrator import Agent_orchestrator
import matplotlib.pyplot as plt
from pylab import *

# Creamos una conexion a la BBDD
bbdd_connec = Mongo_manager(ConfigVariablesBbdd.env_database)

# Creamos una accion
test_orch = Agent_orchestrator(bbdd_connec)
list_of_results = test_orch.run(100)
x_axis = range(len(list_of_results))
plt.plot(list_of_results)
show()


