import datetime
from common_tools.config import ConfigCommonVariables
from common_tools.config import ConfigErrorMessages
from common_tools import error_management
""" Modulo que encapsula el logger
"""


def log(log_level, log_message, log_object):
    # First we validate the message
    if isinstance(log_message, list):
        log_message = formatErrorMessage(log_message)
    # Build the rest of the output print
    dateHour = datetime.datetime.now()
    print(dateHour, "[", log_level, "]: Error in ", log_object)
    print(dateHour, "[", log_level, "]: ", log_message)
    # Raise error if the level is error
    if log_level == ConfigCommonVariables.level_error:
        error_management.raiseError(log_object + ' -> ' + log_message)

def formatErrorMessage(list_args):
    # We take the variable the thas has the error message
    error_code = list_args[0]
    # We recover from configuration this error message
    exec('raw_str = ConfigErrorMessages.' + error_code, globals())
    wrk_str = raw_str
    # We fill all the variables
    for elem in range(1,len(list_args)):
        wrk_str = wrk_str.replace('$'+ str(elem), list_args[elem])
    return wrk_str
