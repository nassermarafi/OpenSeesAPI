"""
This class is used to create the following OpenSees TCL Commands:

SP_Constraint (single-point constraint), which prescribe the movement (typically 0) of a single dof at a node. There are a number of commands for creating single-point coonstraints:
fix
fixX
fixY
fixZ

MP_Constraint (multi-point constraint), which prescribe that the movement of certain dof at one node are defined by the movement of certain dof at another node. There again are a number of commands for defining multi-point constraints.
equalDOF
rigidDiaphragm
rigidLink
"""

__author__ = 'Nasser Marafi'

from OpenSeesAPI.OpenSees import OpenSees

class Fix(OpenSees):
    """
    fix $nodeTag (ndf $constrValues)
    $nodeTag	integer tag identifying the node to be constrained
    $constrValues	ndf constraint values (0 or 1) corresponding to the ndf degrees-of-freedom.
    0 unconstrained (or free)
    1 constrained (or fixed)
    """
    def __init__(self, Node, DOFList, **kwargs):
        self._Node = Node
        self._DOFList = DOFList
        self._CommandLine = 'fix %d %s'%(Node.id, ''.join([' %d'%x for x in DOFList]))
        self.__dict__.update(kwargs)

class EqualDOF(OpenSees):
    """
    equalDOF $rNodeTag $cNodeTag $dof1 $dof2 ...
    $rNodeTag	integer tag identifying the retained, or master node (rNode)
    $cNodeTag	integer tag identifying the constrained, or slave node (cNode)
    $dof1 $dof2 ...	nodal degrees-of-freedom that are constrained at the cNode to be the same as those at the rNode
    Valid range is from 1 through ndf, the number of nodal degrees-of-freedom.
    """
    def __init__(self, MasterNode, SlaveNodes, DOFList, **kwargs):
        self._MasterNode = MasterNode
        self._SlaveNode = SlaveNodes
        self._DOFList = DOFList
        self.__dict__.update(kwargs)

        self._CommandLine = 'equalDOF %d %d %s'%(self._MasterNode.id, self._SlaveNode.id, ''.join([' %d'%x for x in self._DOFList]))

class RigidDiaphragm(OpenSees):
    """
    rigidDiaphragm $perpDirn $masterNodeTag $slaveNodeTag1 $slaveNodeTag2 ...
    $perpDirn	direction perpendicular to the rigid plane (i.e. direction 3 corresponds to the 1-2 plane)
    $masterNodeTag	integer tag identifying the master node
    $slaveNodeTag1 $slaveNodeTag2 ...	integar tags identifying the slave nodes
    """
    def __init__(self, perpDOF, MasterNode, SlaveNodeList, **kwargs):
        self._perpDOF = perpDOF
        self._MasterNode = MasterNode
        self._SlaveNodeList = SlaveNodeList
        self.__dict__.update(kwargs)

        self._CommandLine = 'rigidDiaphragm %d %d %s'%(self._perpDOF, self._MasterNode.id, ''.join([' %d'%x.id for x in self._SlaveNodeList]))

class RigidLink(OpenSees):
    """
    rigidLink $type $masterNodeTag $slaveNodeTag
    $type	string-based argument for rigid-link type:
    bar only the translational degree-of-freedom will be constrained to be exactly the same as those at the master node
    beam both the translational and rotational degrees of freedom are constrained.
    $masterNodeTag	integer tag identifying the master node
    $slaveNodeTag	integer tag identifying the slave node
    """
    def __init__(self, Type, MasterNode, SlaveNode, **kwargs):
        self._Type = Type
        self._MasterNode = MasterNode
        self._SlaveNode = SlaveNode
        self.__dict__.update(kwargs)

        self._CommandLine = 'rigidLink %s %d %d'%(self._Type, self._MasterNode.id, self._SlaveNode.id)
