from marketing_agent.config import ConfigEnvMarkAgent
import pandas as pd
import random

class N_bandit_agent:
    """ Base class that represent an agent

    The agent is the element that takes actions on the environment, and receive the reguard.

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
    def __init__(self, ddbb_conn, environment, n_actions, error):
        """ For every instance we need 1 parameter
        :param ddbb_conn: Object that represents the connection to the bbdd
        """
        # We save arguments as object variables (not class variables)
        self.bbdd = ddbb_conn
        self.this_env = environment
        self.this_n_actions = n_actions
        self.this_error = error
        self.error_sum = 0 # Acumulated error
        # Create dataframe with the actions and her information
        # - Variables used
        cont = 1
        Qk_list = []
        k_list = []
        alpha_list = []
        id_list = []
        # - Create rest of columns
        for i in range(len(n_actions)):
            Qk_list.append(0)
            k_list.append(1)
            alpha_list.append(0)
            id_list.append(cont)
            cont = cont + 1
        # - Create the dataframe
        self.action_df = pd.DataFrame({"action": n_actions,
                                       "Qk": Qk_list,
                                       "k": k_list,
                                       "alpha": alpha_list},
                                       index=id_list)

    def __str__(self):
        """ We override the print method

        :return:
        """
        str1 = "Environment: " + str(self.this_env) + "\n"
        str2 = "N_actions: " + str(self.this_n_actions) + "\n"
        str3 = "Error: " + str(self.this_error) + "\n"
        str4 = "Action_Matrix" + "\n" + str(self.action_df)
        return str1 + str2 + str3 + str4

    def return_id_obj(self):
        """ Function that returns the identificator of the environment passed (person ID = ID_DOC)
        :return:
        """
        # We obtain de id
        self.obj_id = self.this_env[ConfigEnvMarkAgent.obj_id]
        # We create the firt half of the action message
        self.action_id_part = ConfigEnvMarkAgent.pre_id_str + self.obj_id + ConfigEnvMarkAgent.post_id_str
        return self.obj_id

    def select_action(self):
        """ This function selects an action to be send to the environment
        :return:
        """
        # For each iteraction we add the allowed error
        self.error_sum = self.error_sum + self.this_error
        # If the error is more than one we do a random selection
        if self.error_sum >= 1:
            # We reset the accumulated error
            self.error_sum = 0
            # We select a random action id
            sel_id = random.randint(1, len(self.this_n_actions))
            # We save the selected ID
            self.selected_id = sel_id
            # Now we select a random action
            random_row = self.action_df.loc[sel_id, :]
            self.action_str, self.Qk, self.k, self.alpha = random_row
        # Else we do greedy selection
        else:
            # We obtain the max prediction of reward Qk
            Qk_max = self.action_df['Qk'].max()
            # We search in the df if we have more than one max
            filter_action_df = self.action_df[self.action_df.Qk == Qk_max]
            original_index = filter_action_df.index
            # We reset the index of the new df
            filter_action_df_res = filter_action_df.reset_index(drop=True)
            new_index = filter_action_df_res.index
            # We generate a random index to select only one row
            sel_id = random.randint(0, len(filter_action_df_res) - 1)
            # We save a reference of the index selected
            self.selected_id = original_index[sel_id]
            # We select the row
            max_row = filter_action_df_res.loc[sel_id, :]
            # We obtain the values for the action
            self.action_str, self.Qk, self.k, self.alpha = max_row
        return self.action_id_part + self.action_str

    def receive_feedback(self, reward):
        """ Method for communicating to the agent the reward received for his last action

        :param reward:
        :return:
        """
        # We calculate the mean reward for the action and upgrade de step
        self.k_next = self.k + 1
        self.Qk_next = self.Qk + (1/self.k_next)*(reward-self.Qk)
        # We update the action matrix
        self.action_df.at[self.selected_id, 'Qk'] = self.Qk_next
        self.action_df.at[self.selected_id, 'k'] = self.k_next





