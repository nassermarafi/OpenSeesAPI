"""
This class is used to create the following OpenSees TCL Commands:
eigen
"""

__author__ = 'Nasser'

from OpenSeesAPI.OpenSees import OpenSees

class Eigen(OpenSees):
    """
    This command is used to perform the analysis.
    eigen <$solver> $numEigenvalues
    $numEigenvalues	number of eigenvalues required
    $solver	optional string detailing type of solver: -genBandArpack, -symmBandLapack, -fullGenLapack (default: -genBandArpack)

    RETURNS:
    a tcl string containg eigenvalues.
    """
    def __init__(self, NoOfModes, symmBandLapack=False, fullGenLapack=False):
        self._NoOfModes = NoOfModes
        self._Optional = ''
        if symmBandLapack == True:
            self._Optional = '-symmBandLapack'
        elif fullGenLapack==True:
            self._Optional = '-fullGenLapack'
        self._CommandLine =  'set pi [expr 2.0*asin(1.0)]; \n'
        self._CommandLine += 'set nModes %d; \n'%(self._NoOfModes)
        self._CommandLine += 'set lambdaN [eigen %s %d]; \n'%(self._Optional,self._NoOfModes)
        for i in range(0,self._NoOfModes):
                self._CommandLine += 'set lambdaN%d [lindex $lambdaN [expr %d]]; \n'%(i+1,i)
        for i in range(0,self._NoOfModes):
            self._CommandLine += 'set w%d [expr pow($lambdaN%d,0.5)]; \n'%(i+1,i+1)
        for i in range(0,self._NoOfModes):
            self._CommandLine += 'set T%d [expr 2.0*$pi/$w%d]; \n'%(i+1,i+1)
        for i in range(0,self._NoOfModes):
            self._CommandLine += 'puts "T%d = $T%d s" \n'%(i+1,i+1)
