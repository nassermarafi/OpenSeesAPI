"""
This class is used to create the following OpenSees TCL Commands:
This command is used to construct the LinearSOE and LinearSolver objects to store and solve the system of equations in the analysis.
system systemType? arg1? ...
The type of LinearSOE created and the additional arguments required depends on the systemType? provided in the command.
The following contain information about systemType? and the args required for each of the available system types:
BandGeneral SOE
BandSPD SOE
ProfileSPD SOE
SuperLU SOE
UmfPack SOE
FullGeneral
SparseSYM SOE
Mumps
Cusp
"""

__author__ = 'Nasser'

from OpenSeesAPI.OpenSees import OpenSees

class BandGeneral(OpenSees):
    """
    This command is used to construct a BandGeneralSOE linear system of equation object. As the name implies, this class is used for matrix systems which have a banded profile. The matrix is stored as shown below in a 1dimensional array of size equal to the bandwidth times the number of unknowns. When a solution is required, the Lapack routines DGBSV and SGBTRS are used. The following command is used to construct such a system:
    system BandGeneral
    """
    def __init__(self):
        self._CommandLine = 'system BandGeneral'

class BandSPD(OpenSees):
    """
    This command is used to construct a BandSPDSOE linear system of equation object. As the name implies, this class is used for symmetric positive definite matrix systems which have a banded profile. The matrix is stored as shown below in a 1 dimensional array of size equal to the (bandwidth/2) times the number of unknowns. When a solution is required, the Lapack routines DPBSV and DPBTRS are used. To following command is used to construct such a system:
    system BandSPD
    """
    def __init__(self):
        self._CommandLine = 'system BandSPD'

class ProfileSPD(OpenSees):
    """
    This command is used to construct a profileSPDSOE linear system of equation object. As the name implies, this class is used for symmetric positive definite matrix systems. The matrix is stored as shown below in a 1 dimensional array with only those values below the first non-zero row in any column being stored. This is sometimes also referred to as a skyline storage scheme. To following command is used to construct such a system:
    system ProfileSPD
    """
    def __init__(self):
        self._CommandLine = 'system ProfileSPD'

class SuperLU(OpenSees):
    """
    This command is used to construct a SparseGEN linear system of equation object. As the name implies, this class is used for sparse matrix systems. The solution of the sparse matrix is carried out using SuperLU. To following command is used to construct such a system:
    system SparseGEN
    """
    def __init__(self):
        self._CommandLine = 'system SparseGEN'

class UmfPack(OpenSees):
    """
    This command is used to construct a sparse system of equations which uses the UmfPack solver. To following command is used to construct such a system:
    system UmfPack <-lvalueFact $LVALUE

    (LVALUE*the number of nonzero entries) is the amount of additional memory set aside for fill in during the matrix solution, by default the LVALUE factor is 10. You only need to experiment with this if you get error messages back about LVALUE being too small.
    """
    def __init__(self, LValue = None):
        self._CommandLine = 'system UmfPack' #Add L Value

class FullGeneral(OpenSees):
    """
    This command is used to construct a Full General linear system of equation object. As the name implies, the class utilizes NO space saving techniques to cut down on the amount of memory used. If the matrix is of size, nxn, then storage for an nxn array is sought from memory when the program runs. When a solution is required, the Lapack routines DGESV and DGETRS are used. The following command is used to construct such a system:
    system FullGeneral
    """
    def __init__(self):
        self._CommandLine = 'system FullGeneral'

class SparseSYM(OpenSees):
    """
    This command is used to construct a sparse symmetric system of equations which uses a row-oriented solution method in the solution phase. To following command is used to construct such a system:
    system SparseSYM
    """
    def __init__(self):
        self._CommandLine = 'system SparseSYM'

class Mumps(OpenSees):
    def __init__(self,Optional=''):
        self._Optional = Optional
        self._CommandLine = 'system Mumps %s'%self._Optional

class Cusp(OpenSees):
    """
    system CuSP -rTol $RTOL -mInt $MINT -pre $PRE -solver $SOLVER
    $RTOL	Set the relative tolerance.
    $MINT	Set the maximum number of iterations.
    $PRE	Set the preconditioner. can be none, diagonal, and ainv
    $SOLVER	Set the iterative solver. can be bicg, bicgstab, cg, and gmres.
    """
    def __init__(self):
        self._CommandLine = 'system CuSP '
