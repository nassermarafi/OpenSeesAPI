__author__ = 'marafi'



# This command is used to construct a Node object. It assigns coordinates and masses to the Node object.
#
# node $nodeTag (ndm $coords) <-mass (ndf $massValues)>
# $nodeTag	integer tag identifying node
# $coords	nodal coordinates (ndm arguments)
# $massValues	nodal mass corresponding to each DOF (ndf arguments) (optional))
# The optional -mass string allows analyst the option of associating nodal mass with the node
#
# EXAMPLE:
# node 1 0.0 0.0 0.0; # x,y,z coordinates (0,0,0) of node 1
# node 2 0.0 120. 0.0; # x,y,z coordinates (0,120,0) of node 2

from OpenSeesAPI.OpenSees import OpenSees

class Node(OpenSees):
    def __init__(self, id, X, Y, Z=None, MassX = None, MassY = None, MassZ = None, **kwargs):
        self._X = X
        self._Y = Y
        self._Z = Z
        self._id = id
        self._MassX = MassX
        self._MassY = MassY
        self._MassZ = MassZ

        self._Optional = None
        if self._MassX != None:
            self._Optional = '-mass'
            for x in [self._MassX, self._MassY, self._MassZ]:
                if x != None:
                    self._Optional += ' %f'%x

        self.__dict__.update(kwargs)

        if Z == None:
            self._CommandLine = 'node %d %f %f'%(self._id, self._X, self._Y)
        else:
            self._CommandLine = 'node %d %f %f %f'%(self._id, self._X, self._Y, self._Z)

    @property
    def X(self):
        return self._X
    @property
    def Y(self):
        return self._Y
    @property
    def Z(self):
        return self._Z

class Mass(OpenSees):
    def __init__(self, Node, MassList, **kwargs):
        self._Node = Node
        self._MassList = MassList
        self._CommandLine = 'mass %d %s'%(self._Node.id, ''.join([' %f'%x for x in self._MassList]))

        self.__dict__.update(kwargs)

class Raleigh(OpenSees):
    def __init__(self, AlphaM, BetaK, BetaKInitial, BetaKCommitted):
        self._AlphaM = AlphaM
        self._BetaK = BetaK
        self._BetaKInitial = BetaKInitial
        self._BetaKCommitted = BetaKCommitted
        self._CommandLine = 'rayleigh %f %f %f %f'%(self._AlphaM, self._BetaK, self._BetaKInitial, self._BetaKCommitted)