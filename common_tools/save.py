# Imports

def from_list_to_file(this_list,this_file):
    """

    :param this_list:
    :param this_file:
    :return:
    """
    f = open(this_file,'w') # Abrimos el fichero
    # For each elemnt
    cont = 1
    for x in this_list:
        linea = this_file + ',' + str(cont) + ',' + str(x) + '\n'
        f.write(linea)
        cont = cont + 1
    f.close()

