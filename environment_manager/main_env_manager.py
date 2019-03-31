from bbdd_manager.Mongo_manager import Mongo_manager
from bbdd_manager import ConfigVariablesBbdd
from environment_manager.Interaction import Interaction
from environment_manager.Behavior_manager import Behavior_manager

# Creamos una conexion a la BBDD
bbdd_connec = Mongo_manager(ConfigVariablesBbdd.env_database)
# Creamos el objeto
int1 = Interaction(bbdd_connec)
int1.set_interaction("SEND_CAMPAIGN")
#print(int1)
bm1 = Behavior_manager(bbdd_connec)
bm1.action_behavior_manager("SEND_CAMPAIGN","RECEIVE_EXPENSES")
