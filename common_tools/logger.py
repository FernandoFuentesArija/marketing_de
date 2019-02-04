import datetime
from common_tools.config import ConfigCommonVariables
from common_tools import error_management
""" Modulo que encapsula el logger
"""


def log(log_level, log_message, log_object):
    dateHour = datetime.datetime.now()
    print(dateHour, "[", log_level, "]: Error in ", log_object)
    print(dateHour, "[", log_level, "]: ", log_message)
    if log_level == ConfigCommonVariables.level_error:
        error_management.raiseError(log_object + ' -> ' + log_message)