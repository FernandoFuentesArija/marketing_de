from environment_manager.config import ConfEnvManager
from common_tools.logger import log
from common_tools.config import ConfigCommonVariables
from common_tools.config import ConfigErrorMessages

class Interaction:
    """ Base class to define different ways to interact with the environment

    On first place we are only going to define a FILE type of interaction

    ATTRIBUTES
    ---------
    It's composed:
    - self.bbdd: Object that represents the connection to the bbdd
    - self.int_type:
    - self.int_name:
    - self.int_comm_type:
    - self.int_comm_format:
    - self.int_comm_ext
    - self.int_comm_loc
    - self.input_int_obj_name
    - self.input_int_obj_id
    - self.input_int_act_name
    - self.input_int_inter_capacity

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

    def __str__(self):
        """ ToString
        """
        toString01 = "Interaction type: " + str(self.int_type) + "\n"
        toString02 = "Interaction name: " + str(self.int_name) + "\n"
        toString03 = "Interaction communication type: " + str(self.int_comm_type) + "\n"
        toString04 = "Interaction communication format: " + str(self.int_comm_format) + "\n"
        toString05 = "Interaction communication extension: " + str(self.int_comm_ext) + "\n"
        toString06 = "Interaction communication location: : " + str(self.int_comm_loc) + "\n"
        if hasattr(self, 'input_int_obj_name'):
            toString07 = "Interaction input object name: " + str(self.input_int_obj_name) + "\n"
        else:
            toString07 = ''
        if hasattr(self, 'input_int_obj_id'):
            toString08 = "Interaction input object id: " + str(self.input_int_obj_id) + "\n"
        else:
            toString08 = ''
        if hasattr(self, 'input_int_act_name'):
            toString09 = "Interaction input action name: " + str(self.input_int_act_name) + "\n"
        else:
            toString09 = ''
        if hasattr(self, 'input_int_inter_capacity'):
            toString10 = "Interaction capacity: " + str(self.input_int_inter_capacity) + "\n"
        else:
            toString10 = ''
        return (toString01 + toString02 + toString03 + toString04 + toString05 + toString06 + toString07 + toString08 +
        toString09 + toString10)

    def set_interaction(self, interaction_name):
        """ This function will inform the attributes of the object, based on the interaction name that is passed as
        a parameter. The configuration with the data is on the collection <interaction_coll>.
        :param interaction_name: Name of the interaction to load as this object.
        :return: None.
        """
        collection = ConfEnvManager.interaction_coll
        condition = {ConfEnvManager.int_name:interaction_name}
        int_doc = self.bbdd.recover_one_doc(collection, condition)
        if isinstance(int_doc,dict):
            for key in int_doc:
                if key == ConfEnvManager.int_type:
                    self.int_type = int_doc[ConfEnvManager.int_type]
                elif key == ConfEnvManager.int_name:
                    self.int_name = int_doc[ConfEnvManager.int_name]
                elif key == ConfEnvManager.int_comm_type:
                    self.int_comm_type = int_doc[ConfEnvManager.int_comm_type]
                elif key == ConfEnvManager.int_comm_format:
                    self.int_comm_format = int_doc[ConfEnvManager.int_comm_format]
                elif key == ConfEnvManager.int_comm_ext:
                    self.int_comm_ext = int_doc[ConfEnvManager.int_comm_ext]
                elif key == ConfEnvManager.int_comm_loc:
                    self.int_comm_loc = int_doc[ConfEnvManager.int_comm_loc]
                elif key == ConfEnvManager.input_int_obj_name:
                    self.input_int_obj_name = int_doc[ConfEnvManager.input_int_obj_name]
                elif key == ConfEnvManager.input_int_obj_id:
                    self.input_int_obj_id = int_doc[ConfEnvManager.input_int_obj_id]
                elif key == ConfEnvManager.input_int_act_name:
                    self.input_int_act_name = int_doc[ConfEnvManager.input_int_act_name]
                elif key == ConfEnvManager.input_int_inter_capacity:
                    self.input_int_inter_capacity = int_doc[ConfEnvManager.input_int_inter_capacity]
                else:
                    pass # Error
        else:
            list_var_message = [ConfigErrorMessages.ErrorCode006, interaction_name, ConfEnvManager.interaction_coll]
            log_object = 'Iteration.set_interaction()'
            log(ConfigCommonVariables.level_error, list_var_message, log_object)

    def get_type(self):
        """ This function return the interaction type.
        :return: self.int_type
        """
        return self.int_type

    def get_commtype(self):
        """ This function return the interaction communication type.
        :return: self.int_comm_type
        """
        return self.int_comm_type

    def get_path(self):
        """ This function return the path were the input/output is expected.
        :return: self.int_comm_loc
        """
        return self.int_comm_loc

    def get_commform(self):
        """ This function return the interaction communication format.
        :return: self.int_comm_format
        """
        return self.int_comm_format

    def get_commext(self):
        """ This function return the interaction communication file extension.
        :return: self.int_comm_ext
        """
        return self.int_comm_ext