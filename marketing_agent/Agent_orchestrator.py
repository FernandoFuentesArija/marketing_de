from marketing_agent.config import ConfigEnvMarkAgent
from marketing_agent.N_bandit_agent import N_bandit_agent
from environment_manager import main_env_manager
import json


class Agent_orchestrator:
    """ Base class that represents the orchestrator who will manage comnunications between the agents and
    the environment.

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
    def __init__(self, ddbb_conn, agent_error = 0.05):
        """ For every instance we need at least 1 parameter the conection
        :param ddbb_conn: Object that represents the connection to the bbdd
        :param agent_error: Number that represents the error (random action)
        """
        self.bbdd = ddbb_conn
        self.error_for_agents = agent_error
        self.total_reguard_list = []
        self.list_of_actions = self.get_list_of_actions()

    def set_agent_error(self, new_error):
        """ We set the error variable
        :param new_error: Number that represents the error (random action)
        """
        self.error_for_agents = new_error

    def get_list_of_actions(self):
        """ We recover the list of actions from a config file
        :return: list of actions
        """
        list_of_act = []
        act_conf_file = open("config/actions.conf")
        for line in act_conf_file:
            list_of_act.append(line)
        act_conf_file.close()
        return list_of_act

    def run(self, iterations):
        """ This method will prepare as many agents as objects in the environment and manage all the comunications
        between them.
        :param iterations: Number of actions done for each agent to the environment
        :return total_reguard_list: Returns a list with the total reward by iteraction
        """
        # list with the sum of rewards of each iteration
        list_iter_rewards = []
        # sum of rewards of each iteration
        sum_iter_rewards = 0
        # List to contain al agents created
        list_obj_agents = []
        list_id_obj_agents = []
        # We recover all objects in the environment
        all_env_objs = self.bbdd.recover_all_doc(ConfigEnvMarkAgent.env_source)
        # We prepare a list of agents for each object in the environment
        for obj in all_env_objs:
            # We created the agent and put him on the list
            agent = N_bandit_agent(self.bbdd,obj,self.list_of_actions,self.error_for_agents)
            # We put him on the list of agents
            list_obj_agents.append(agent)
            # We get the id of the agent's environment
            agent_id_env = agent.return_id_obj()
            # We put him in the list of ids
            list_id_obj_agents.append(agent_id_env)
        for iteration in range(iterations):
            # At the begining of each iteration we initialize the counter
            sum_iter_rewards = 0
            # We ask to every agent to select an action and save it in the input environment manager
            f = open(ConfigEnvMarkAgent.in_path_file_name, "w") # Open input file (delete content)
            for one_agent in list_obj_agents:
                # We write in the input file the actions choosed by the agents
                #f.write(one_agent.select_action())
                reg_escribir = one_agent.select_action()
                f.write(reg_escribir)
            f.close() # Close input file
            # We ask the environment manager to process the input actions
            main_env_manager.run()
            # Once the environment has react to the actions we have to comunicate the answers to the agents
            response_file = open(ConfigEnvMarkAgent.out_path_file_name) # Apertura fichero de respuestas
            for response_str in response_file:
                # We transform the string into a dictionary
                response_str = response_str.replace("'","\"")
                response_dict = json.loads(response_str)  # Transform the string into a dictionary
                this_id = response_dict[ConfigEnvMarkAgent.obj_id] # Obtain the person id
                this_reguard = response_dict[ConfigEnvMarkAgent.reward_id] # Obtain the reward of last action
                # Save the sum of reguards for this iteration
                sum_iter_rewards = sum_iter_rewards + this_reguard
                # We search the agent
                this_index = list_id_obj_agents.index(this_id)
                # We give it the reward
                list_obj_agents[this_index].receive_feedback(this_reguard)
            response_file.close() # Cierre fichero de respuestas
            # Before new iteration save total sum
            list_iter_rewards.append(sum_iter_rewards)
        return list_iter_rewards








