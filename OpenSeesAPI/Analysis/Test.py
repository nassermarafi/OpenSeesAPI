"""
This class is used to create the following OpenSees TCL Commands:
This command is used to construct a ConvergenceTest object. Certain SolutionAlgorithm objects require a ConvergenceTest object to determine if convergence has been achieved at the end of an iteration step. The convergence test is applied to the matrix equation, AX=B stored in the LinearSOE.
test testType? arg1? ...
The type of convergence test created and the additional arguments required depends on the testType? provided in the command.
The following contain information about testType? and the args required for each of the available test types:
test Command Equation
Norm Unbalance Test
Norm Displacement Increment Test
Energy Increment Test
Relative Norm Unbalance Test
Relative Norm Displacement Increment Test
Total Relative Norm Displacement Increment Test
Relative Energy Increment Test
Fixed Number of Iterations
"""

__author__ = 'Nasser'



from OpenSeesAPI.OpenSees import OpenSees

class NormUnbalance(OpenSees):
    """
    test NormUnbalance $tol $iter <$pFlag> <$nType>
    $tol	the tolerance criteria used to check for convergence
    $iter	the max number of iterations to check before returning failure condition
    $pFlag	optional print flag, default is 0. valid options:
    0 print nothing
    1 print information on norms each time test() is invoked
    2 print information on norms and number of iterations at end of successfull test
    4 at each step it will print the norms and also the ?U and R(U) vectors.
    5 if it fails to converge at end of $numIter it will print an error message BUT RETURN A SUCEESSFULL test
    $nType	optional type of norm, default is 2. (0 = max-norm, 1 = 1-norm, 2 = 2-norm, ...)
    """
    def __init__(self, Tolerance, MaxIterations, PrintFlag=None, nType=None):
        self._Tolerance = Tolerance
        self._MaxIterations = MaxIterations
        self._PrintFlag = PrintFlag
        self._nType =nType
        if self._PrintFlag != None:
            self._Optional = '%d'%(PrintFlag)
        elif self._nType != None:
            self._Optional = '%d %d'%(PrintFlag,nType)
        else:
            self._Optional = ''
        self._CommandLine = 'test NormUnbalance %e %d %s'%(Tolerance,MaxIterations,self._Optional)

class NormDispIncr(OpenSees):
    """
    This command is used to construct a convergence test which uses the norm of the left hand side solution vector of the matrix equation to determine if convergence has been reached. What the solution vector of the matrix equation is depends on integrator and constraint handler chosen. Usually, though not always, it is equal to the displacement increments that are to be applied to the model. The command to create a NormDispIncr test is the following:
    test NormDispIncr $tol $iter <$pFlag> <$nType>

    $tol	the tolerance criteria used to check for convergence
    $iter	the max number of iterations to check before returning failure condition
    $pFlag	optional print flag, default is 0. valid options:
    0 print nothing
    1 print information on norms each time test() is invoked
    2 print information on norms and number of iterations at end of successfull test
    4 at each step it will print the norms and also the ?U and R(U) vectors.
    5 if it fails to converge at end of $numIter it will print an error message BUT RETURN A SUCEESSFULL test
    $nType	optional type of norm, default is 2. (0 = max-norm, 1 = 1-norm, 2 = 2-norm, ...)
    """
    def __init__(self, Tolerance, MaxIterations, pFlag=0, nType=2):
        self._Tolerance = Tolerance
        self._MaxIterations = MaxIterations
        self._pFlag = pFlag
        self._nType = nType
        self._CommandLine = 'test NormDispIncr %e %d %d %d'%(self._Tolerance,self._MaxIterations, self._pFlag, self._nType)

class EnergyIncr(OpenSees):
    """
    test EnergyIncr $tol $iter <$pFlag> <$nType>

    $tol	the tolerance criteria used to check for convergence
    $iter	the max number of iterations to check before returning failure condition
    $pFlag	optional print flag, default is 0. valid options:
    0 print nothing
    1 print information on norms each time test() is invoked
    2 print information on norms and number of iterations at end of successfull test
    4 at each step it will print the norms and also the ?U and R(U) vectors.
    5 if it fails to converge at end of $numIter it will print an error message BUT RETURN A SUCEESSFULL test
    $nType	optional type of norm, default is 2. (0 = max-norm, 1 = 1-norm, 2 = 2-norm, ...)
    """
    def __init__(self, Tolerance, MaxIterations, pFlag = 0 , nType=2):
        self._Tolerance = Tolerance
        self._MaxIterations = MaxIterations
        self._CommandLine = 'test EnergyIncr %e %d %d %d'%(Tolerance,MaxIterations,pFlag,nType)

class RelativeNormUnbalance(OpenSees):
    def __init__(self, Tolerance, MaxIterations):
        self._Tolerance = Tolerance
        self._MaxIterations = MaxIterations
        self._CommandLine = 'test RelativeNormUnbalance %e %d'%(Tolerance,MaxIterations)

class RelativeNormDispIncr(OpenSees):
    def __init__(self, Tolerance, MaxIterations):
        self._Tolerance = Tolerance
        self._MaxIterations = MaxIterations
        self._CommandLine = 'test RelativeNormDispIncr %e %d'%(Tolerance,MaxIterations)

class RelativeEnergyIncr(OpenSees):
    def __init__(self, Tolerance, MaxIterations):
        self._Tolerance = Tolerance
        self._MaxIterations = MaxIterations
        self._CommandLine = 'test RelativeEnergyIncr %e d'%(Tolerance,MaxIterations)