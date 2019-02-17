from environment_creator.Attribute import Attribute
from bbdd_manager.Mongo_manager import Mongo_manager
from bbdd_manager import ConfigVariablesBbdd
import random

# Creamos una conexion a la BBDD
bbdd_connec = Mongo_manager(ConfigVariablesBbdd.env_database)

#Creacion de la clase y uso
att_1 = Attribute(bbdd_connec)

# Case 1 - numeros aleatorios
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
result_list1 = att_1.create_attribute(att_desc1,att_num1)
print("Imprimimos lista de numeros aleatorios")
print(result_list1)



# Case 2 - numeros secuenciales
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
result_list2 = att_1.create_attribute(att_desc2,att_num2)
print("Imprimimos lista de numeros secuenciales")
print(result_list2)


# Case 3 - numeros unique
def gen_list(num):
    ret_gen_list = []
    this_num = 0
    for i in range(num):
        this_num = random.randint(0,9)
        ret_gen_list.append(this_num)
    ret_gen_list.append(this_num)
    ret_gen_list.pop(0)
    #print(ret_gen_list)
    return ret_gen_list

att_1.att_num = 5
result_list3 = att_1.create_unique_list(gen_list)
print("Imprimimos lista de numeros sin repeticiones")
print(result_list3)

# Case 4 - fallo del create_numbers por generacion no reconocida
att_desc4 = {
    'OBJ_NAME':'person',
    'ATT_NAME':'weight',
    'ATT_CONSTR':'NON_UNIQUE',
    'ATT_TYPE':'NUMBER',
    'PRECISION':'0',
    'RANGE':'2-10',
    'GENERATION':'SEQUENTI',
    'HOP':'2'
}
att_num4 = 4
#print("fallo del create_numbers por generacion no reconocida")
#result_list2 = att_1.create_attribute(att_desc4,att_num4)

# Case 5 - numeros secuenciales
att_desc5 = {
    'OBJ_NAME':'person',
    'ATT_NAME':'weight',
    'ATT_CONSTR':'NON_UNIQUE',
    'ATT_TYPE':'NUMBER',
    'PRECISION':'0',
    'RANGE':'2-10',
    'GENERATION':'SEQUENTIAL',
    'HOP':'2'
}
att_num5 = 5
#print("fallo del create_numbers por generacion secuencial incorrecta")
#result_list2 = att_1.create_attribute(att_desc5,att_num5)


# Case 6 - Tipo de atributo que no existe
att_desc6 = {
    'OBJ_NAME':'person',
    'ATT_NAME':'weight',
    'ATT_CONSTR':'NON_UNIQUE',
    'ATT_TYPE':'NUMBERS',
    'PRECISION':'0',
    'RANGE':'2-10',
    'GENERATION':'SEQUENTIAL',
    'HOP':'2'
}
att_num6 = 5
#print("fallo del create_numbers por generacion secuencial incorrecta")
#result_list2 = att_1.create_attribute(att_desc6,att_num6)

# Case 7 - texto aleatorio
att_desc7 = {
    'OBJ_NAME':'person',
    'ATT_NAME':'text_code',
    'ATT_CONSTR':'NON_UNIQUE',
    'ATT_TYPE':'TEXT',
    'GENERATION':'RANDOM',
    'LENGTH':'5'
}
att_num7 = 4
result_list7 = att_1.create_attribute(att_desc7,att_num7)
print("Imprimimos lista de texto aleatorio")
print(result_list7)

# Case 8 - texto cte
att_desc8 = {
    'OBJ_NAME':'person',
    'ATT_NAME':'text_code',
    'ATT_CONSTR':'NON_UNIQUE',
    'ATT_TYPE':'TEXT',
    'GENERATION':'CTE',
    'CTE_STR':'Hola Mundo'
}
att_num8 = 5
result_list8 = att_1.create_attribute(att_desc8,att_num8)
print("Imprimimos lista de texto constante")
print(result_list8)

# Case 9 - texto de bbdd
att_desc9 = {
    'OBJ_NAME':'person',
    'ATT_NAME':'text_code',
    'ATT_CONSTR':'NON_UNIQUE',
    'ATT_TYPE':'TEXT',
    'GENERATION':'BBDD',
    'BBDD_SOURCE':'data_person_names_sample',
    'BBDD_FIELD':'name'
}
att_num9 = 6
result_list9 = att_1.create_attribute(att_desc9,att_num9)
print("Imprimimos lista de texto desde una bbdd")
print(result_list9)