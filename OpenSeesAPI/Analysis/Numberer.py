"""
This class is used to create the following OpenSees TCL Commands:
This command is used to construct the DOF_Numberer object. The DOF_Numberer object determines the mapping between equation numbers and degrees-of-freedom -- how degrees-of-freedom are numbered.
numberer numbererType? arg1? ...
The type of DOF_Numberer created and the additional arguments required depends on the numbererType? provided in the command.

The following contain information about numbererType? and the args required for each of the available dof numberer types:

Plain Numberer
Reverse Cuthill-McKee Numberer
Alternative_Minimum_Degree Numberer
"""

__author__ = 'Nasser'

from OpenSeesAPI.OpenSees import OpenSees

class Plain(OpenSees):
    """
    This command is used to construct a Plain degree-of-freedom numbering object to provide the mapping between the degrees-of-freedom at the nodes and the equation numbers. A Plain numberer just takes whatever order the domain gives it nodes and numbers them, this ordering is both dependent on node numbering and size of the model. The command to construct a Plain numberer is a follows:

    numberer Plain
    """
    def __init__(self):
        self._CommandLine = 'numberer Plain'

class RCM(OpenSees):
    """
    This command is used to construct an RCM degree-of-freedom numbering object to provide the mapping between the degrees-of-freedom at the nodes and the equation numbers. An RCM numberer uses the reverse Cuthill-McKee scheme to order the matrix equations. The command to construct an RCM numberer is a follows:

    numberer RCM
    """
    def __init__(self):
        self._CommandLine = 'numberer RCM'

class AMD(OpenSees):
    """
    This command is used to construct an AMD degree-of-freedom numbering object to provide the mapping between the degrees-of-freedom at the nodes and the equation numbers. An AMD numberer uses the approximate minimum degree scheme to order the matrix equations. The command to construct an AMD numberer is a follows:

    numberer AMD
    """
    def __init__(self):
        self._CommandLine = 'numberer AMD'