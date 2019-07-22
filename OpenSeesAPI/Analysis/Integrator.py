"""
This class is used to create the following OpenSees TCL Commands:
This command is used to construct the Integrator object. The Integrator object determines the meaning of the terms in the system of equation object Ax=B.
The Integrator object is used for the following:
   * determine the predictive step for time t+dt
   * specify the tangent matrix and residual vector at any iteration
   * determine the corrective step based on the displacement increment dU

The type of integrator used in the analysis is dependent on whether it is a static analysis or transient analysis.

Static Integrators:
Load Control
Displacement Control
Minimum Unbalanced Displacement Norm
Arc-Length Control

Transient Integrators:
Central Difference
Newmark Method
Hilber-Hughes-Taylor Method
Generalized Alpha Method
TRBDF2
"""

__author__ = 'Nasser'

from OpenSeesAPI.OpenSees import OpenSees

class Static:
    class LoadControl(OpenSees):
        """
        integrator LoadControl $lambda <$numIter $minLambda $maxLambda>
        $lambda	the load factor increment ?
        $numIter	the number of iterations the user would like to occur in the solution algorithm. Optional, default = 1.0.
        $minLambda	the min stepsize the user will allow. optional, defualt = ?min = ?
        $maxLambda	the max stepsize the user will allow. optional, default = ?max = ?
        """
        def __init__(self, Lambda, NumIter=None, minLambda=None, maxLambda=None):
            self._Lambda = Lambda
            self._NumIter = None
            self._minLambda = minLambda
            self._maxLambda = maxLambda
            if self._NumIter == None:
                self._CommandLine = 'integrator LoadControl %f'%(self._Lambda)
            else:
                self._CommandLine = 'integrator LoadControl %f %d %f %f'%(self._Lambda, self._NumIter, self._minLambda, self._maxLambda)

    class DisplacementControl(OpenSees):
        """
        integrator DisplacementControl $node $dof $incr <$numIter $?Umin $?Umax>
        $node	node whose response controls solution
        $dof	degree of freedom at the node, valid options: 1 through ndf at node.
        $incr	first displacement increment Udof
        $numIter	the number of iterations the user would like to occur in the solution algorithm. Optional, default = 1.0.
        $Umin	the min stepsize the user will allow. optional, defualt = Umin = U0
        $Umax	the max stepsize the user will allow. optional, default = Umax = U0
        """
        def __init__(self, Node, DOF, Increment, Optional=''):
            self._Node = Node
            self._DOF = DOF
            self._Increment = Increment
            self._Optional = Optional
            self._CommandLine = 'integrator DisplacementControl %d %d %e %s'%(self._Node.id, self._DOF, self._Increment, self._Optional)

    class ArcLength(OpenSees):
        """
        This command is used to construct an ArcLength integrator object. In an analysis step with ArcLength we seek to determine the time step that will result in our constraint equation being satisfied.
        integrator ArcLength $s $alpha
        $s	the  arcLength.
        $alpha a scaling factor on the reference loads.
        """
        def __init__(self):
            self._CommandLine = 'integrator ArcLength'

class Transient:
    class Newmark(OpenSees):
        """
        This command is used to construct a Newmark integrator object.
        integrator Newmark $gamma $beta
        $gamma	gamma factor
        $beta	beta factor

        EXAMPLE:

        integrator Newmark 0.5 0.25
        """
        def __init__(self, Gamma, Beta):
            self._Gamma = Gamma
            self._Beta = Beta
            self._CommandLine = 'integrator Newmark %f %f'%(self._Gamma, self._Beta)

    class HHT(OpenSees):
        """
        This command is used to construct a Hilber-Hughes-Taylor (HHT) integration object. This is an implicit method that allows for energy dissipation and second order accuracy (which is not possible with the regular Newmark method). Depending on choices of input parameters, the method can be unconditionally stable.
        integrator HHT $alpha <$gamma $beta>
        $alpha	alpha factor
        $gamma	gamma factor
        $beta	beta factor
        EXAMPLE:

        integrator HHT 0.9
        """
        def __init__(self, Alpha, Gamma=None, Beta=None):
            self._Alpha = Alpha
            self._Gamma = Gamma
            self._Beta = Beta
            if Gamma == None and Beta == None:
                self._CommandLine = 'integrator HHT %.3f'%(self._Alpha)
            else:
                self._CommandLine = 'integrator HHT %.3f %.3f %.3f' % (self._Alpha, self._Gamma, self._Beta)

    class CentralDifference(OpenSees):
        """
        This command is used to construct a Central Difference integrator object.
integrator CentralDifference

        EXAMPLE:

        integrator CentralDifference
        """
        def __init__(self):
            self._CommandLine = 'integrator CentralDifference'

