"""
This class is used to create the following OpenSees TCL Commands:

The type of ConstraintHandler created and the additional arguments required depends on the constraintType? provided in the command.

The following contain information about numbererType? and the args required for each of the available constraint handler types:
Plain Constraints
Lagrange Multipliers
Penalty Method
Transformation Method

"""

__author__ = 'Nasser'

from OpenSeesAPI.OpenSees import OpenSees

class Plain(OpenSees):
    """
    This command is used to construct a Plain constraint handler. A plain constraint handler can only enforce homogeneous single point constraints (fix command) and multi-point constraints constructed where the constraint matrix is equal to the identity (equalDOF command). The following is the command to construct a plain constraint handler:
    """
    ""
    def __init__(self):
        self._CommandLine = 'constraints Plain'

class Lagrange(OpenSees):
    """
    This command is used to construct a LagrangeMultiplier constraint handler, which enforces the constraints by introducing lagrange multiplies to the system of equation. The following is the command to construct a plain constraint handler:

    constraints Lagrange <$alphaS $alphaM >

    $alphaS	αS factor on singe points. optional, default = 1.0
    $alphaM	αM factor on multi-points, optional default = 1.0;
    """
    def __init__(self, AlphaS=1.0, AlphaM=1.0):
        self._AlphaS = AlphaS
        self._AlphaM = AlphaM

    @property
    def CommandLine(self):
        self._CommandLine = 'constraints Lagrange %f %f'%(self._AlphaS, self._AlphaM)
        return self._CommandLine

class Penalty(OpenSees):
    """
    This command is used to construct a Penalty constraint handler, which enforces the constraints using the penalty method. The following is the command to construct a penalty constraint handler:

    constraints Penalty $alphaS $alphaM

    $alphaS	penalty αS factor on single point constraints
    $alphaM	penalty αM factor on multi-point constraints
    """
    def __init__(self, AlphaS, AlphaM):
        self._AlphasS = AlphaS
        self._AlphaM = AlphaM

    @property
    def CommandLine(self):
        self._CommandLine = 'constraints Penalty %f %f'%(self._AlphasS, self._AlphaM)
        return self._CommandLine

class Transformation(OpenSees):
    """
    This command is used to construct a transformation constraint handler, which enforces the constraints using the transformation method. The following is the command to construct a transformation constraint handler:

    constraints Transformation

    NOTES:
    The single-point constraints when using the transformation method are done directly. The matrix equation is not manipulated to enforce them, rather the trial displacements are set directly at the nodes at the start of each analysis step.
    Great care must be taken when multiple constraints are being enforced as the transformation method does not follow constraints:
    1) If a node is fixed, constrain it with the fix command and not equalDOF or other type of constraint.
    2) If multiple nodes are constrained, make sure that the retained node is not constrained in any other constraint.
    And remember if a node is constrained to multiple nodes in your model it probably means you have messed up.
    """
    def __init__(self):
        self._CommandLine = 'constraints Transformation'