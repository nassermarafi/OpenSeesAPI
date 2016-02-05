__author__ = 'Nasser'

from OpenSeesAPI.OpenSees import OpenSees

class Plain(OpenSees):
    def __init__(self):
        self._CommandLine = 'numberer Plain'

class RCM(OpenSees):
    def __init__(self):
        self._CommandLine = 'numberer RCM'

class AMD(OpenSees):
    def __init__(self):
        self._CommandLine = 'numberer AMD'