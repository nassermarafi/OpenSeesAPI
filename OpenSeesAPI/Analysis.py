"""
This class is used to create the following OpenSees TCL Commands:
analysis analysisType?
$analysisType	char string identifying type of analysis object to be constructed. Currently 3 valid options:
Static - for static analysis
Transient - for transient analysis with constant time step
VariableTransient - for transient analysis with variable time step
NOTE:
If the component objects are not defined before hand, the command automatically creates default component objects and issues warning messages to this effect. The number of warning messages depends on the number of component objects that are undefined.
"""

__author__ = 'Nasser'

from OpenSeesAPI.OpenSees import OpenSees

class Static(OpenSees):
        def __init__(self):
            self._CommandLine = 'analysis Static'

class Transient(OpenSees):
        def __init__(self):
            self._CommandLine = 'analysis Transient'

class VariableTransient(OpenSees):
        def __init__(self):
            self._CommandLine = 'analysis variableTransient'



