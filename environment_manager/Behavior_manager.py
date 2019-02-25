from environment_manager.Interaction import Interaction
from environment_manager.config import ConfEnvManager
import os

class Behavior_manager:
    """ Base class to manage the behavior of the objects loaded in the environment

    First we use the package environment_creator to fill a DDBB with the derised objects(give birth to the environment).
    Now we want to give that environment the ability to react against the reception of actions.

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

    def action_behavior_manager(self, interaction_input_name, interaction_output_name):
        """ This function will model the response of the environment to actions
        :param interaction_input_name: Name of the interaction that is use to receive the action.
        :param interaction_output_name: Name of the interaction that is use to send the response to the action.
        :return: None
        """
        # First we create to interaction objects, one for the input the other for the output
        interaction_input_obj = Interaction(self.bbdd)
        interaction_input_obj.set_interaction(interaction_input_name)
        interaction_output_obj = Interaction(self.bbdd)
        interaction_output_obj.set_interaction(interaction_output_name)
        # Now we are going to see the type of interaction selected (only file right now)
        type_of_inter = interaction_input_obj.get_commtype()
        if type_of_inter == ConfEnvManager.file_comm:
            self.file_action_behavior_manager(interaction_input_obj, interaction_output_obj)
        else: # Configure more types in the future
            pass

    def file_action_behavior_manager(self, interaction_input_obj, interaction_output_obj):
        """ This function will model the response of the environment to actions
        :param interaction_input_obj: Object of the interaction that is use to receive the action.
        :param interaction_output_obj: Object of the interaction that is use to send the response to the action.
        :return: None
        """
        # We ask for the relative path
        input_rel_path = interaction_input_obj.get_path()
        # Obtain list of files in input directory
        file_list = os.listdir(input_rel_path)
        print("lista dir: ", file_list)