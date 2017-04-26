"""
This class is used to create the following OpenSees TCL Commands:

This command is used to construct a SolutionAlgorithm object, which determines the sequence of steps taken to solve the non-linear equation.
algorithm algorithmType? arg1? ...
The type of solution algorithm created and the additional arguments required depends on the algorithmType? provided in the command.

The following contain information about algorithmType? and the args required for each of the available algorithm types:
Linear Algorithm
Newton Algorithm
Newton with Line Search Algorithm
Modified Newton Algorithm
Krylov-Newton Algorithm
Secant Newton Algorithm
BFGS Algorithm
Broyden Algorithm
"""

__author__ = 'Nasser'

from OpenSeesAPI.OpenSees import OpenSees

class Linear(OpenSees):
    """
        This command is used to construct a Linear algorithm object which takes one iteration to solve the system of equations.
     \Delta U = - K^{-1}R(U),\!

    algorithm Linear <-initial> <-factorOnce>

    -secant	optional flag to indicate to use secant stiffness
    -initial	optional flag to indicate to use initial stiffness
    -factorOnce	optional flag to indicate to only set up and factor matrix once
    """
    def __init__(self):
        self._CommandLine = 'algorithm Linear'

class Newton(OpenSees):
    """
    This command is used to construct a NewtonRaphson algorithm object which is uses the Newton-Raphson algorithm to solve the nonlinear residual equation. The Newton-Raphson method is the most widely used and most robust method for solving nonlinear algebraic equations. The command is of the following form:
    algorithm Newton <-initial> <-initialThenCurrent>

    -initial	optional flag to indicate to use initial stiffness iterations
    -initialThenCurrent	optional flag to indicate to use initial stiffness on first step, then use current stiffness for subsequent steps
    """
    def __init__(self, Initial=False,InitialThenCurrent=False):
        self._Initial = Initial
        self._InitialThenCurrent = InitialThenCurrent
        if self._Initial:
            self._CommandLine = 'algorithm Newton -initial'
        elif self._InitialThenCurrent:
            self._CommandLine = 'algorithm Newton -initialThenCurrent'
        else:
            self._CommandLine = 'algorithm Newton'

class ModifiedNewton(OpenSees):
    """
    This command is used to construct a ModifiedNewton algorithm object, which uses the modified newton-raphson algorithm to solve the nonlinear residual equation. The command is of the following form:
algorithm ModifiedNewton <-initial>

    -initial	optional flag to indicate to use initial stiffness iterations.

    """
    def __init__(self, Initial=False):
        self._Initial = Initial
        if self._Initial:
            self._CommandLine = 'algorithm ModifiedNewton -initial'
        else:
            self._CommandLine = 'algorithm ModifiedNewton'

class NewtonLineSearch(OpenSees):
    """
    This command is used to construct a NewtonLineSearch algorithm object which introduces line search to the Newton-Raphson algorithm to solve the nonlinear residual equation. Line search increases the effectiveness of the Newton method when convergence is slow due to roughness of the residual. The command is of the following form:
    algorithm NewtonLineSearch <-type $typeSearch> <-tol $tol> <-maxIter $maxIter> <-minEta $minEta> <-maxEta $maxEta>

    $typeSearch	line search algorithm. optional default is InitialInterpoled. valid types are:
    Bisection, Secant, RegulaFalsi, InitialInterpolated
    $tol	tolerance for search. optional, defeulat = 0.8
    $maxIter	max num of iterations to try. optional, default = 10
    $minEta	a min \eta\! value. optional, default = 0.1
    $maxEta	a max \eta\! value. optional, default = 10.0
    """
    def __init__(self, typeSearch='InitialInterpoled', Tolerance=0.8, MaxIteration=10, MinEta=0.1, MaxEta=10.):
        self._typeSearch = typeSearch
        self._Tolerance = Tolerance
        self._MaxIteration = MaxIteration
        self._MinEta = MinEta
        self._MaxEta = MaxEta
        self._CommandLine = 'algorithm NewtonLineSearch -type %s -tol %e -maxIter %d -minEta %f -maxEta %f'%(self._typeSearch,self._Tolerance,self._MaxIteration,self._MinEta,self._MaxEta)

class KrylovNewton(OpenSees):
    """
    This command is used to construct a KrylovNewton algorithm object which uses a Krylov subspace accelerator to accelerate the convergence of the modified newton method. The command is of the following form:
algorithm KrylovNewton <-iterate $tangIter> <-increment $tangIncr> <-maxDim $maxDim>

    $tangIter	tangent to iterate on, options are current, initial, noTangent. default is current.
    $tangIncr	tangent to increment on, options are current, initial, noTangent. default is current
    $maxDim	max number of iterations until the tangent is reformed and the acceleration restarts (default = 3).
    """
    def __init__(self, TangIter=None, TangIncr=None, MaxDim=None):
        self._TangIter = TangIter
        self._TangIncr = TangIncr
        self._MaxDim = MaxDim
        if self._TangIncr == None:
            self._CommandLine = 'algorithm KrylovNewton'
        else:
            self._CommandLine = 'algorithm KrylovNewton %f %f %d'%(self._TangIncr, self._TangIncr, self._MaxDim)

class BFGS(OpenSees):
    """
    This command is used to construct a(BFGS) algorithm object. The BFGS method is one of the most effective matrix-update or quasi Newton methods for iteration on a nonlinear system of equations. The method computes new search directions at each iteration step based on the initial jacobian, and subsequent trial solutions. The unlike regular Newton-Raphson does not require the tangent matrix be reformulated and refactored at every iteration, however unlike ModifiedNewton it does not rely on the tangent matrix from a previous iteration.

    algorithm BFGS
    """
    def __init__(self):
        self._CommandLine = 'algorithm BFGS'

class Broyden(OpenSees):
    """
    This command is used to construct a Broyden algorithm object for general unsymmetric systems which performs successive rank-one updates of the tangent at the first iteration of the current time step.

    algorithm Broyden <$count>

    $count	number of iterations within a time step until a new tangent is formed
    """
    def __init__(self, Count):
        self._Count = Count
        self._CommandLine = 'algorithm Broyden %d'%self._Count
