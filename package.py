"""
Demo Python Module

This is a template for Python modules that can
be re-used as required. This section is intended
to document the module as a whole.
"""

###########
# Imports #
###########

import sys

#############
# Constants #
#############

CONST = "I am a constant"

#####################
# Exception Classes #
#####################

class DemoException(Exception):
    pass

#######################
# Interface Functions #
#######################

def api(call):
    result = "You have called the API for a template class!"
    return result

###########
# Classes #
###########

class Demonstration(object):

    def __init__(self):
        self.purpose = "demonstration"

    def demonstrate(self):
        return "My purpose is " + self.purpose

################################
# Internal Functions & Classes #
################################

def helper_function(params):
    return params

#################
# Main Function #
#################

def main():
    return None

if __name__ == '__main__':
    status = main()
    sys.exit(status)
