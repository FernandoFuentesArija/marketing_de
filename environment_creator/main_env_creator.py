from bbdd_manager.Mongo_manager import Mongo_manager
from bbdd_manager import ConfigVariablesBbdd
from environment_creator.Object_generator import Object_generator

# Creamos una conexion a la BBDD
bbdd_connec = Mongo_manager(ConfigVariablesBbdd.env_database)
# Creamos el objeto
og1 = Object_generator(bbdd_connec)
og1.create_json_with_objects("PERSON",10000)