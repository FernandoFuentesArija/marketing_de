from environment_creator.Attribute import Attribute
from bbdd_manager.Mongo_manager import Mongo_manager
from bbdd_manager import ConfigVariablesBbdd

# Creamos una conexion a la BBDD
bbdd_connec = Mongo_manager(ConfigVariablesBbdd.env_database)

# Variables
att_desc1 = {
    'OBJ_NAME':'person',
    'ATT_NAME':'weight',
    'ATT_CONSTR':'NON_UNIQUE',
    'ATT_TYPE':'NUMBER',
    'PRECISION':'2',
    'RANGE':'10-100',
    'GENERATION':'RANDOM'
}
att_num1 = 10

#Creacion de la clase y uso
att_1 = Attribute(bbdd_connec)

# Case 1 - numeros aleatorios
result_list1 = att_1.create_attribute(att_desc1,att_num1)
print("Imprimimos lista de numeros aleatorios")
print(result_list1)

att_desc2 = {
    'OBJ_NAME':'person',
    'ATT_NAME':'weight',
    'ATT_CONSTR':'NON_UNIQUE',
    'ATT_TYPE':'NUMBER',
    'PRECISION':'0',
    'RANGE':'2-10',
    'GENERATION':'SEQUENTIAL',
    'HOP':'2'
}
att_num2 = 4

# Case 2 - numeros secuenciales
result_list2 = att_1.create_attribute(att_desc2,att_num2)
print("Imprimimos lista de numeros secuenciales")
print(result_list2)




