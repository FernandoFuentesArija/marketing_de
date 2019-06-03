from bbdd_manager.Mongo_manager import Mongo_manager
from bbdd_manager import ConfigVariablesBbdd
from environment_manager.Interaction import Interaction
from environment_manager.Behavior_manager import Behavior_manager

# Creamos una conexion a la BBDD
bbdd_connec = Mongo_manager(ConfigVariablesBbdd.env_database)
bm1 = Behavior_manager(bbdd_connec)
# Ejemplo de uso behaviour
def run():
    bm1.action_behavior_manager("SEND_CAMPAIGN","RECEIVE_EXPENSES")
#run() # For local test
