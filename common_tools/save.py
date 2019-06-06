# Imports

def from_list_to_file(this_list,this_file):
    """

    :param this_list:
    :param this_file:
    :return:
    """
    f = open(this_file,'w') # Abrimos el fichero
    txt = ','.join(str(x) for x in this_list)
    f.write(txt)
    f.close()

