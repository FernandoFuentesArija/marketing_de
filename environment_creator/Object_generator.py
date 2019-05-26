from environment_creator.config import ConfigVariablesEnv
from environment_creator.Attribute import Attribute

class Object_generator:
    """ Base class to generate objects that are previously configured in the DDBB

    The environment is composed of objects. These objects have characteristics that define them. Those characteristics
    we are going to call them attributes. This instance will create a json with all the objects to load into the bbdd.

    ATTRIBUTES
    ---------
    It's composed:
    - self.bbdd: Object that represents the connection to the bbdd


    PUBLIC METHODS
    ---------------
    -

    PRIVATE METHODS
    ---------------
    -

    PERSISTENCE
    ------------
    - The initialization of this class accepts an object that represents the connection to a database.

    RELATIONS WITH OTHER ELEMENTS
    ------------------------------
    -[element name]: La
    """

    # We pass a connection to each instance (can be the same)
    def __init__(self, ddbb_conn):
        """ For every instance we need 1 parameter
        :param ddbb_conn: Object that represents the connection to the bbdd
        """
        self.bbdd = ddbb_conn

    def create_json_with_objects(self, object_name, how_many_objects):
        """ This function will create and return a list objects
        :param object_name: Name of the object to create
        :param how_many_objects: Number of objects to create
        :return: list of objects generated in a json file
        """
        # We open the file
        file_name = object_name + '.json'
        output_file = open(file_name,'w')
        # Variables
        list_of_attributes_conf = []
        list_of_attributes = []
        attribute_solver = Attribute(self.bbdd)
        # We prepare the query
        collection = ConfigVariablesEnv.ojb_conf_coll
        condition = {ConfigVariablesEnv.object_name:object_name}
        # We search the object name in the source where the object configuration is loaded to obtain all attributes
        obj_att_cur = self.bbdd.recover_docs(collection, condition)
        # We save in a list the attribute descriptions
        for doc in obj_att_cur:
            list_of_attributes_conf.append(doc)
        num_of_att = len(list_of_attributes_conf)
        # For each attribute descriptor, we call the attribute class to generate them
        for att_desc in list_of_attributes_conf:
            list_solved_att = attribute_solver.create_attribute(att_desc, how_many_objects)
            list_of_attributes.append(list_solved_att)
        # For each object, we generate the json record
        for obj_num in range(how_many_objects):
            json_str_record = '{'
            for att_num in range(num_of_att):
                # Take the name and the type of the attribute
                doc_att_conf = list_of_attributes_conf[att_num]
                att_name = doc_att_conf[ConfigVariablesEnv.attribute_name]
                att_type = doc_att_conf[ConfigVariablesEnv.attribute_type]
                # We prepare the key
                json_str_record = json_str_record + '"' + att_name + '":'
                # Take the attribute
                this_att = list_of_attributes[att_num][obj_num]
                # Special treatment if its a date
                if att_type == ConfigVariablesEnv.att_type_date:
                    json_str_record = json_str_record + '{ "$date":"' + str(this_att) + ConfigVariablesEnv.date_adjustment +'"},'
                elif att_type == ConfigVariablesEnv.att_type_text:
                    json_str_record = json_str_record + '"' + str(this_att) + '"' + ','
                else:
                    json_str_record = json_str_record + str(this_att) + ','
            json_len = len(json_str_record)
            json_str_record = json_str_record[:json_len-1] + '}\n'
            output_file.write(json_str_record)
        output_file.close()


