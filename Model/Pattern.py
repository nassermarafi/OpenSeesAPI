__author__ = 'marafi'

# Plain Pattern
# Uniform Excitation Pattern
# Multi-Support Excitation Pattern
# DRM Load Pattern

from OpenSeesAPI.OpenSees import OpenSees

class UniformExcitation(OpenSees):
    """
    pattern UniformExcitation $patternTag $dir -accel $tsTag <-vel0 $vel0> <-fact $cFactor>
    $patternTag	unique tag among load patterns
    $dir	direction in which ground motion acts
    1 - corresponds to global X axis
    2 - corresponds to global Y axis
    3 - corresponds to global Z axis
    $tsTag	tag of the TimeSeries series defining the acceleration history.
    $vel0	the initial velocity (optional, default=0.0)
    $cFactor	constant factor (optional, default=1.0)
    """
    def __init__(self, id, Dof, TimeSeries, **kwargs):
        self._id = id
        self._Dof = Dof
        self._TimeSeries = TimeSeries
        self._CommandLine = 'pattern UniformExcitation %d %d -accel %d'%(self._id, self._Dof, self._TimeSeries.id)
        self.__dict__.update(kwargs)

class Plain(OpenSees):
    """
    This commnand allows the user to construct a LoadPattern object. Each plain load pattern is associated with a TimeSeries object and can contain multiple NodalLoads, ElementalLoads and SP_Constraint objects. The command to generate LoadPattern object contains in { } the commands to generate all the loads and the single-point constraints in the pattern. To construct a load pattern and populate it, the following command is used:
    pattern Plain $patternTag $tsTag <-fact $cFactor> {
    load...
    eleLoad...
    sp...
    ...
    }

    NOTES:
    The command to generate a LoadPattern contains in { } the commands to generate all the loads and single-point constraints..
    $patternTag	unique tag among load patterns
    $tsTag	the tag of the time series to be used in the load pattern
    $cFactor	constant factor (optional, default=1.0)
    load...	command to nodal load
    eleLoad ...	command to generate elemental load
    sp ...	command to generate single-point constraint
    """
    def __init__(self, id, TimeSeriesTag, Objects, Optional='', **kwargs):
        self._id = id
        self._TimeSeriesTag = TimeSeriesTag
        self._Optional = Optional
        self._Objects = Objects
        self.__dict__.update(kwargs)

        self._CommandLine = 'pattern Plain %d %s %s { \n%s\n }'%(self._id, self._TimeSeriesTag, self._Optional, ''.join(map(lambda x: '\n'+x._CommandLine, self._Objects)))

class Load(OpenSees):
    """
    load $nodeTag (ndf $LoadValues)
    $nodeTag	tag of node to which load is applied.
    $loadvalues	ndf reference load values.
    """
    def __init__(self, Node, LoadList, **kwargs):
        self._Node = Node
        self._LoadList = LoadList
        self.__dict__.update(kwargs)

        self._CommandLine = 'load %d %s'%(self._Node.id, ''.join([' %f'%x for x in self._LoadList]))

class EleLoad(OpenSees):
    """
    The eleLoad command is used to construct an ElementalLoad object and add it to the enclosing LoadPattern.
    load $eleLoad $arg1 $arg2 $arg3 ....

    The element loads are only applied to line elements. Continuum elements do not accept element loads. When NDM=2, the beam column elements all accept eleLoad commands of the following form:
    eleLoad -ele $eleTag1 <$eleTag2 ....> -type -beamUniform $Wy <$Wx>

    eleLoad -range $eleTag1 $eleTag2 -type -beamPoint $Py $xL <$Px>

    When NDM=3, the beam column elements all accept eleLoad commands of the following form:
    eleLoad -ele $eleTag1 <$eleTag2 ....> -type -beamUniform $Wy $Wz <$Wx>

    eleLoad -range $eleTag1 $eleTag2 -type -beamPoint $Py $Pz $xL <$Px>

    $eleTag1 $eleTag2 ...	tag of PREVIOUSLY DEFINED element
    $Wx	mag of uniformily distributed ref load acting in direction along member length
    $Wy	mag of uniformily distributed ref load acting in local y direction of element
    $Wz	mag of uniformily distributed ref load acting in local z direction of element
    $Py	mag of ref point load acting in direction along member length
    $Py	mag of ref point load acting in local y direction of element
    $Pz	mag of ref point load acting in local z direction of element
    $xL	location of point load relative to node I, prescribed as fraction of element length
    """
    def __init__(self, EleArg, ElementList, TypeArg, LoadList, **kwargs):
        self._EleArg = EleArg
        self._ElementList = ElementList
        self._TypeArg = TypeArg
        self._LoadList = LoadList
        self.__dict__.update(kwargs)

        self._CommandLine = 'eleLoad %s %s %s %s'%(self._EleArg, ''.join([' %d'%x.id for x in self._ElementList]), self._TypeArg, ''.join([' %f'%x for x in self._LoadList]))

class sp(OpenSees):
    """
    sp $nodeTag $dofTag $dofValue

    $nodeTag	tag of node to which constraint is applied.
    $dofTag	the degree-of-freedom at the node to which constraint is applied (1 through ndf)
    $dofValue	reference constraint value.
    """
    def __init__(self, Node, DOF, DOFValue, **kwargs):
        self._Node = Node
        self._DOF = DOF
        self._DOFValue = DOFValue
        self.__dict__.update(kwargs)

        self._CommandLine = 'sp %d %d %f'%(self._Node.id, self._DOF, self._DOFValue)