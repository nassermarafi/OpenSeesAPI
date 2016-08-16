"""
This class is used to create the following OpenSees TCL Commands:
This command is used to build a Solution Method object that determines how the program executes the step evaluation and
handles non-convergence (i.e. ok not 0)
"""

__author__ = 'Stephens/Thonstad'

from OpenSeesAPI.OpenSees import OpenSees
from OpenSeesAPI import Test
from OpenSeesAPI import Algorithm

class BasicTimeHistory(OpenSees):
        """

        """
        def __init__(self, Dt, Tol, Steps, **kwargs):
            self._Dt = Dt
            self._Tol = Tol
            self._Steps = Steps
            self.__dict__.update(kwargs)
            self._CommandLine = (   'set ok 0 \n' +
                                    'set Nsteps %d \n'%Steps +
                                    'set step 0 \n'
                                    'while {$ok == 0 & $step < [expr $Nsteps +1]} {\n' +
                                    '\t set ok [analyze 1 %f]\n'%Dt +
                                    '\t puts "Running Time History Step: $step out of %d"\n'%Steps +
                                    '\t set step [expr $step+1]\n' +
                                    '}\n')

class GravityAnalysis(OpenSees):
        """

        """
        def __init__(self, Steps, **kwargs):
            self._Steps = Steps
            self.__dict__.update(kwargs)
            self._CommandLine = (   'analyze %d \n'%Steps +
                                    'loadConst - time 0.0 \n')

class ChangeAlgorithm(OpenSees):
        """

        """
        def __init__(self, Dt, Steps, **kwargs):
            self._Dt = Dt
            self._Steps = Steps
            self.__dict__.update(kwargs)
            self._CommandLine = (   'set ok 0 \n' +
                                    'while{$ok == 0} { \n' +
                                    '\t set ok [analyze %d %f ]\n'%(Steps,Dt) +
                                    '\t if {$ok != 0} {\n' +
                                    '\t puts "Trying Newton Line Search ... "\n' +
                                    '\t' + Algorithm.NewtonLineSearch(Tolerance=0.8).CommandLine + '\n' +
                                    '\t set ok [analyze %d %f ]\n'%(Steps,Dt) +
                                    '\t }\n\n' +
                                    '\t if {$ok != 0} {\n' +
                                    '\t puts "Trying Newton with Initial Tangent ... "\n' +
                                    '\t' + Algorithm.Newton(Initial=True).CommandLine + '\n' +
                                    '\t set ok [analyze %d %f ]\n'%(Steps,Dt) +
                                    '\t }\n\n' +
                                    '\t if {$ok != 0} {\n' +
                                    '\t puts "Trying Broyden ... "\n' +
                                    '\t' + Algorithm.Broyden(8).CommandLine + '\n' +
                                    '\t set ok [analyze %d %f ]\n'%(Steps,Dt) +
                                    '\t }\n\n' +
                                    '\t if {$ok != 0} {\n' +
                                    '\t puts "Trying KrylovNewton ... "\n' +
                                    '\t' + Algorithm.KrylovNewton().CommandLine + '\n' +
                                    '\t set ok [analyze %d %f ]\n'%(Steps,Dt) +
                                    '\t }\n' +
                                    '}\n')

class DisplacementTestStep(OpenSees):
        """

        """
        def __init__(self, Dt, Tol, Steps, **kwargs):
            self._Dt = Dt
            self._Tol = Tol
            self._Steps = Steps
            self.__dict__.update(kwargs)
            self._CommandLine = (   'set ok 0 \n' +
                                    'while{$ok == 0} { \n' +
                                    '\t if {$ok != 0} {\n' +
                                    '\t puts "Trying Lower Dt: %f and Tol: %f ... "\n'%(Dt,Tol) +
                                    '\t' + Test.NormDispIncr(Tol,1000,0).CommandLine + '\n' +
                                    '\t set ok [analyze %d %f ]\n'%(Steps,Dt) +
                                    '\t }\n\n' +
                                    '\t if {$ok != 0} {\n' +
                                    '\t puts "Trying Lower Dt: %f and Tol: %f ... "\n'%(Dt*0.1,Tol) +
                                    '\t' + Test.NormDispIncr(Tol,1000,0).CommandLine + '\n' +
                                    '\t set ok [analyze %d %f ]\n'%(Steps,0.1*Dt) +
                                    '\t }\n\n' +
                                    '\t if {$ok != 0} {\n' +
                                    '\t puts "Trying Lower Dt: %f and Tol: %f ... "\n'%(Dt*0.01,Tol) +
                                    '\t' + Test.NormDispIncr(Tol,1000,0).CommandLine + '\n' +
                                    '\t set ok [analyze %d %f ]\n'%(Steps,0.01*Dt) +
                                    '\t }\n\n' +
                                    '\t if {$ok != 0} {\n' +
                                    '\t puts "Trying Lower Dt: %f and Tol: %f ... "\n'%(Dt*0.001,Tol) +
                                    '\t' + Test.NormDispIncr(Tol,1000,0).CommandLine + '\n' +
                                    '\t set ok [analyze %d %f ]\n'%(Steps,0.001*Dt) +
                                    '\t }\n' +
                                    '\t if {$ok != 0} {\n' +
                                    '\t puts "Trying Lower Dt: %f and Tol: %f ... "\n'%(Dt*0.0001,Tol) +
                                    '\t' + Test.NormDispIncr(Tol,1000,0).CommandLine + '\n' +
                                    '\t set ok [analyze %d %f ]\n'%(Steps,0.0001*Dt) +
                                    '\t }\n' +
                                    '\t if {$ok != 0} {\n' +
                                    '\t puts "Trying Lower Dt: %f and Tol: %f ... "\n'%(Dt*0.0000001,Tol) +
                                    '\t' + Test.NormDispIncr(Tol,1000,0).CommandLine + '\n' +
                                    '\t set ok [analyze %d %f ]\n'%(Steps,0.0000001*Dt) +
                                    '\t }\n' +
                                    '}\n')

class TestComparison(OpenSees):
        """
        TestComparison(Dt,Tol,DisplacementFileName,controlNodeID,DOF)
            Finds the solution of the system at specific diplacement steps defined in DisplacementFileName (.txt file) at
            the control node (controlNodeID) in the specified degree of freedom.
        """
        def __init__(self, DisplacmentFileName, controlNodeID, DOF, **kwargs):

            self._controlNodeID = controlNodeID
            self._DOF = DOF
            self.__dict__.update(kwargs)
            self._CommandLine = (   'set fid [open %s r]\n'%DisplacmentFileName +
                                    'set def [read $fid]\n' +
                                    'set numSteps [llength $def]\n\n' +
                                    'set ok 0 \n' +
                                    'set stepNum 0\n' +
                                    'while {$ok == 0 && $stepNum < [expr $numSteps-1]} { \n' +
                                    '\t set U1 [lindex $def $stepNum]\n' +
                                    '\t puts $U1\n'
                                    '\t set U2 [lindex $def $stepNum+1]\n' +
                                    '\t set dU [expr $U2-$U1]\n'
                                    '\t integrator DisplacementControl %s %d $dU 1 $dU $dU\n'%(controlNodeID,DOF) +
                                    '\t set ok [analyze 1]\n' +
                                    '\t incr stepNum\n'
                                    '}\n')


