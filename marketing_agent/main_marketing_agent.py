from bbdd_manager.Mongo_manager import Mongo_manager
from bbdd_manager import ConfigVariablesBbdd
from marketing_agent.N_bandit_agent import N_bandit_agent
from marketing_agent.Agent_orchestrator import Agent_orchestrator

# Creamos una conexion a la BBDD
bbdd_connec = Mongo_manager(ConfigVariablesBbdd.env_database)

# Creamos una accion
test_orch = Agent_orchestrator(bbdd_connec)
test_orch.run(100)

