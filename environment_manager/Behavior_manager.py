from environment_manager.Interaction import Interaction
from environment_manager.config import ConfEnvManager
import os
import json
import datetime

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
        # First we create two interaction objects, one for the input the other for the output
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
        # We obtain the absolute path to this file
        this_abs_path = os.path.abspath(os.path.dirname(__file__))
        # First we prepare de output file
        output_rel_path = interaction_output_obj.get_path()
        output_file_name = interaction_output_obj.get_intname()
        output_file_ext = interaction_input_obj.get_commext()
        output_file_name_plusext = output_file_name + '.' + output_file_ext
        this_path = os.path.join(output_rel_path, output_file_name_plusext) # Relative path
        this_path = os.path.join(this_abs_path, this_path) # Absolute path
        output_file = open(this_path,"w") # Destroy old file, create new one
        output_file.close()
        output_file = open(this_path, "a")  # Reopen to append
        # We ask for the relative path
        input_rel_path = interaction_input_obj.get_path() # Relative path
        abs_input_rel_path = os.path.join(this_abs_path, input_rel_path) # Absolute path
        # Obtain list of files in input directory
        file_list = os.listdir(abs_input_rel_path)
        # We search for the files configured
        file_ext = interaction_input_obj.get_commext()
        for file in file_list: # We search the files in the directory
            if file_ext in file: # We read the file if the extension matches
                this_path = os.path.join(input_rel_path,file) # Relative path
                this_path = os.path.join(this_abs_path, this_path) # Absolute path
                input_file = open(this_path) # Open the file
                for line in input_file.readlines(): # Read line by line
                    ########################################################
                    ## We retrieve the object in the form of a dictionary ##
                    ########################################################
                    line_dict = json.loads(line) # Transform the string into a dictionary
                    this_obj_name = interaction_input_obj.get_objname() # Name of the object
                    this_obj_source = interaction_input_obj.get_objsource()  # Name of the object
                    obj_id_dict = line_dict[this_obj_name] # Obtain the id of the object
                    obj_doc = self.bbdd.recover_one_doc(this_obj_source, obj_id_dict) # Recover object from source
                    #########################################################
                    ## We recovered the action in the form of a dictionary ##
                    #########################################################
                    this_act_name = interaction_input_obj.get_actname()  # Name of the action
                    act_name_dict = line_dict[this_act_name]  # Obtain the dictionary of the action
                    #print(obj_doc, act_name_dict)
                    ###########################################################################
                    ## We call the function that evaluate the behaviour and prepare response ##
                    ###########################################################################
                    response = self.behavior(obj_doc,act_name_dict)
                    if response == 2: # Good
                        good_dic = {ConfEnvManager.response_id:10}
                        obj_id_dict.update(good_dic)
                    else: # Bad
                        bad_dic = {ConfEnvManager.response_id: 0}
                        obj_id_dict.update(bad_dic)
                    str_response = str(obj_id_dict) + '\n'
                    output_file.write(str_response)
                input_file.close()
        output_file.close()


    def behavior(self, object_dict, action_dict):
        """ This function will model the response for one action done to one object
        :param object_dict: Dictionary containing de object caracteristics
        :param action_dict: Dictionary containing the action to apply to the object
        :return: 0 if none of de actions (platform, product) match the customer's tastes
                 1 if the platform or the product match the customer's tastes
                 2 if the platform and the product match the customer's tastes
        """
        # First thing is separate the action into his elements (harcode for now)
        this_product = action_dict[ConfEnvManager.action_elemen_1]
        this_platform = action_dict[ConfEnvManager.action_elemen_2]
        # Test the first action element
        response1 = self.product_behavior(object_dict, this_product)
        # Test the second action element
        response2 = self.platform_behavior(object_dict, this_platform)
        # Return
        return response1 + response2


    def product_behavior(self, object_dict, action_elemnt_dict):
        """ This function will model the response for one action done to one object
        :param object_dict: Dictionary containing de object caracteristics
        :param action_elemnt_dict: Dictionary containing the action element to apply to the object
        :return: 0 if the product doesn't match the customer's tastes
                 1 if the product matches the customer's tastes
        """
        # print(object_dict,action_elemnt_dict)
        # Now we obtain the product selected in the action
        action_product = action_elemnt_dict[ConfEnvManager.prod_name]
        # Depending on the product we search the customer atributtes that matches
        # PARAGUAS
        if (action_product == ConfEnvManager.prod_par):
            # We obtain the city where the person is living
            this_city = object_dict[ConfEnvManager.person_city]
            # List of allowed cities
            this_cities = [ConfEnvManager.per_city_san,ConfEnvManager.per_city_ovi,ConfEnvManager.per_city_der]
            # Validate if we match the taste
            if this_city in this_cities:
                return 1
            else:
                return 0
        # BANADOR
        elif (action_product == ConfEnvManager.prod_ban):
            # We obtain the city and the gender
            this_city = object_dict[ConfEnvManager.person_city]
            this_gender = object_dict[ConfEnvManager.person_gender]
            # List of allowed cities
            this_cities = [ConfEnvManager.per_city_cad, ConfEnvManager.per_city_mar, ConfEnvManager.per_city_mal]
            # Validate if we match the taste
            if this_city in this_cities and this_gender == ConfEnvManager.per_male:
                return 1
            else:
                return 0
        # BIKINI
        elif (action_product == ConfEnvManager.prod_bik):
            # We obtain the city and the gender
            this_city = object_dict[ConfEnvManager.person_city]
            this_gender = object_dict[ConfEnvManager.person_gender]
            # List of allowed cities
            this_cities = [ConfEnvManager.per_city_cad, ConfEnvManager.per_city_mar, ConfEnvManager.per_city_mal]
            # Validate if we match the taste
            if this_city in this_cities and this_gender == ConfEnvManager.per_female:
                return 1
            else:
                return 0
        # GIMNASIO
        elif (action_product == ConfEnvManager.prod_gim):
            # We obtain the city and the gender
            this_city = object_dict[ConfEnvManager.person_city]
            this_weight = object_dict[ConfEnvManager.person_weight]
            # List of allowed cities
            this_cities = [ConfEnvManager.per_city_sal, ConfEnvManager.per_city_seg]
            # Validate if we match the taste
            if this_city in this_cities and this_weight < 90:
                return 1
            else:
                return 0
        # DIETISTA
        elif (action_product == ConfEnvManager.prod_die):
            # We obtain the city and the gender
            this_city = object_dict[ConfEnvManager.person_city]
            this_weight = object_dict[ConfEnvManager.person_weight]
            # List of allowed cities
            this_cities = [ConfEnvManager.per_city_sal, ConfEnvManager.per_city_seg]
            # Validate if we match the taste
            if this_city in this_cities and this_weight >= 90:
                return 1
            else:
                return 0
        # BALON_BALONCESTO
        elif (action_product == ConfEnvManager.prod_bal):
            # We obtain the city and the gender
            this_city = object_dict[ConfEnvManager.person_city]
            this_height = object_dict[ConfEnvManager.person_height]
            this_acc_bal = object_dict[ConfEnvManager.person_acc_bal]
            # List of allowed cities
            this_cities = [ConfEnvManager.per_city_mad]
            # Validate if we match the taste
            if this_city in this_cities and this_height >= 190 and this_acc_bal < 90000:
                return 1
            else:
                return 0
        # DESCAPOTABLE
        elif (action_product == ConfEnvManager.prod_des):
            # We obtain the city and the gender
            this_city = object_dict[ConfEnvManager.person_city]
            this_height = object_dict[ConfEnvManager.person_height]
            this_acc_bal = object_dict[ConfEnvManager.person_acc_bal]
            # List of allowed cities
            this_cities = [ConfEnvManager.per_city_mad]
            # Validate if we match the taste
            if this_city in this_cities and this_height >= 190 and this_acc_bal >= 90000:
                return 1
            else:
                return 0
        # BALON_FUTBOL
        elif (action_product == ConfEnvManager.prod_fut):
            # We obtain the city and the gender
            this_city = object_dict[ConfEnvManager.person_city]
            this_height = object_dict[ConfEnvManager.person_height]
            this_acc_bal = object_dict[ConfEnvManager.person_acc_bal]
            # List of allowed cities
            this_cities = [ConfEnvManager.per_city_mad]
            # Validate if we match the taste
            if this_city in this_cities and this_height < 190 and this_acc_bal < 90000:
                return 1
            else:
                return 0
        # PORSCHE
        elif (action_product == ConfEnvManager.prod_por):
            # We obtain the city and the gender
            this_city = object_dict[ConfEnvManager.person_city]
            this_height = object_dict[ConfEnvManager.person_height]
            this_acc_bal = object_dict[ConfEnvManager.person_acc_bal]
            # List of allowed cities
            this_cities = [ConfEnvManager.per_city_mad]
            # Validate if we match the taste
            if this_city in this_cities and this_height < 190 and this_acc_bal >= 90000:
                return 1
            else:
                return 0
        else:
            print("Product not recogniced")


    def platform_behavior(self, object_dict, action_elemnt_dict):
        """ This function will model the response for one action done to one object
        :param object_dict: Dictionary containing de object caracteristics
        :param action_elemnt_dict: Dictionary containing the action element to apply to the object
        :return: 0 if the platform doesn't match the customer's tastes
                 1 if the platform matches the customer's tastes
        """
        # First we obtain the born date of the person
        this_born_date = object_dict[ConfEnvManager.person_born_date]
        # Now we obtain the platform taste for the person
        # RADIO
        if datetime.datetime(1960, 1, 1, 0, 0) <= this_born_date < datetime.datetime(1970, 1, 1, 0, 0):
            this_person_platform_taste = ConfEnvManager.plat_radio
        # TV
        elif datetime.datetime(1970, 1, 1, 0, 0) <= this_born_date < datetime.datetime(1980, 1, 1, 0, 0):
            this_person_platform_taste = ConfEnvManager.plat_tv
        # NEWS PAPER
        elif datetime.datetime(1980, 1, 1, 0, 0) <= this_born_date < datetime.datetime(1990, 1, 1, 0, 0):
            this_person_platform_taste = ConfEnvManager.plat_newspaper
        # SOCIAL NETWORKS
        elif datetime.datetime(1990, 1, 1, 0, 0) <= this_born_date <= datetime.datetime(2000, 12, 31, 0, 0):
            this_person_platform_taste = ConfEnvManager.plat_social_networks
        else:
            print("Error")
        # Now we obtain the platform selected in the action
        action_platform = action_elemnt_dict[ConfEnvManager.plat_name]
        # Only if the platform selected in the action matches the taste of the person we return 1
        if action_platform == this_person_platform_taste:
            return 1
        else:
            return 0
