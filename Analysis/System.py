__author__ = 'Nasser'

from OpenSeesAPI.OpenSees import OpenSees

class BandGeneral(OpenSees):
    def __init__(self):
        self._CommandLine = 'system BandGeneral'

class BandSPD(OpenSees):
    def __init__(self):
        self._CommandLine = 'system BandSPD'

class ProfileSPD(OpenSees):
    def __init__(self):
        self._CommandLine = 'system ProfileSPD'

class SuperLU(OpenSees):
    def __init__(self):
        self._CommandLine = 'system SparseGEN'

class UmfPack(OpenSees):
    def __init__(self, LValue = None):
        self._CommandLine = 'system UmfPack' #Add L Value

class FullGeneral(OpenSees):
    def __init__(self):
        self._CommandLine = 'system FullGeneral'

class SparseSYM(OpenSees):
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
