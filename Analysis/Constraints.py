__author__ = 'Nasser'

from OpenSeesAPI.OpenSees import OpenSees

class Plain(OpenSees):
    def __init__(self):
        self._CommandLine = 'constaints Plain'

class Lagrange(OpenSees):
    def __init__(self, AlphaS=1.0, AlphaM=1.0):
        self._AlphaS = AlphaS
        self._AlphaM = AlphaM

    @property
    def CommandLine(self):
        self._CommandLine = 'constraints Lagrange %f %f'%(self._AlphaS, self._AlphaM)
        return self._CommandLine

class Penalty(OpenSees):
    def __init__(self, AlphaS, AlphaM):
        self._AlphasS = AlphaS
        self._AlphaM = AlphaM

    @property
    def CommandLine(self):
        self._CommandLine = 'constraints Penalty %f %f'%(self._AlphasS, self._AlphaM)
        return self._CommandLine

class Transformation(OpenSees):
    def __init__(self):
        self._CommandLine = 'constraints Transformation'