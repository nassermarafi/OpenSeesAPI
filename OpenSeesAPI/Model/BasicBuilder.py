"""
This class is used to create the following OpenSees TCL Commands:
model BasicBuilder
"""

__author__ = 'Nasser Marafi'

from OpenSeesAPI.OpenSees import OpenSees

class BasicBuilder(OpenSees):
    """
    This command is used to define spatial dimension of model and number of degrees-of-freedom at nodes. Once issued additional commands are added to interpreter.
    model BasicBuilder -ndm $ndm <-ndf $ndf>
    $ndm	spatial dimension of problem (1,2, or 3)
    $ndf	number of degrees of freedom at node (optional)
    default value depends on value of ndm:
    ndm=1 -> ndf=1
    ndm=2 -> ndf=3
    ndm=3 -> ndf=6
    """
    def __init__(self, NoDim, NoDOF):
        self._NoDim = NoDim
        self._NoDOF = NoDOF
        self._CommandLine = 'model BasicBuilder -ndm %d -ndf %d;'%(self._NoDim, self._NoDOF)