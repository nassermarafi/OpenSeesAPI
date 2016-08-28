"""
This helper is used to create the following OpenSees TCL Commands:
This command is used to build a Solution Method object that determines how the program executes the step evaluation and
handles non-convergence (i.e. ok not 0)
"""

__author__ = 'Stephens/Thonstad, Modified by Marafi'

import OpenSeesAPI

def BasicTimeHistory(OData, Dt, Steps):
    """

    :param OData: osapi database object
    :param Dt: time step
    :param Steps: number of steps
    :return: adds the solution algorithm to the database file
    """
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('set ok 0'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('set Nsteps %d'%Steps))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('set step 0'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('while {$ok == 0 & $step < [expr $Nsteps +1]} {'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t set ok [analyze 1 %f]'%Dt))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t puts "Running Time History Step: $step out of %d"'%Steps))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t set step [expr $step+1]'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('}'))

def GravityAnalysis(OData, Steps):
    """

    :param OData: osapi database object
    :param Steps: number of steps
    :return: adds the solution algorithm to the database file
    """
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('analyze %d'%Steps))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('loadConst - time 0.0'))

def ChangeAlgorithm(OData, Dt, Steps):
    """

    :param OData: osapi database object
    :param Dt: time steps
    :param Steps: number of steps
    :return: adds the solution algorithm to the database file
    """
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('set ok 0'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('while{$ok == 0} {'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t set ok [analyze %d %f ]'%(Steps,Dt)))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t if {$ok != 0} {'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t puts "Trying Newton Line Search ... "'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t' + OpenSeesAPI.Analysis.Algorithm.NewtonLineSearch(Tolerance=0.8).CommandLine + ''))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t set ok [analyze %d %f ]'%(Steps,Dt)))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t }\n'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t if {$ok != 0} {'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t puts "Trying Newton with Initial Tangent ... "'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t' + OpenSeesAPI.Analysis.Newton(Initial=True).CommandLine + ''))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t set ok [analyze %d %f ]'%(Steps,Dt)))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t }\n'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t if {$ok != 0} {'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t puts "Trying Broyden ... "'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t' + OpenSeesAPI.Analysis.Broyden(8).CommandLine + ''))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t set ok [analyze %d %f ]\n'%(Steps,Dt)))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t }\n'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t if {$ok != 0} {'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t puts "Trying KrylovNewton ... "'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t' + OpenSeesAPI.Analysis.KrylovNewton().CommandLine + ''))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t set ok [analyze %d %f ]'%(Steps,Dt)))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t }\n'))

def DisplacementTestStep(OData, Dt, Tol, Steps,):
    """

    :param OData: osapi database object
    :param Dt: time step
    :param Tol: tolerance
    :param Steps: number of steps
    :return: adds the solution algorithm to the database file
    """
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('set ok 0'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('while{$ok == 0} {'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t if {$ok != 0} {'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t puts "Trying Lower Dt: %f and Tol: %f ... "'%(Dt,Tol)))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t' + OpenSeesAPI.Analysis.Test.NormDispIncr(Tol,1000,0).CommandLine + ''))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t set ok [analyze %d %f ]'%(Steps,Dt)))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t }\n'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t if {$ok != 0} {'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t puts "Trying Lower Dt: %f and Tol: %f ... "'%(Dt*0.1,Tol)))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t' + OpenSeesAPI.Analysis.Test.NormDispIncr(Tol,1000,0).CommandLine + ''))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t set ok [analyze %d %f ]'%(Steps,0.1*Dt)))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t }\n'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t if {$ok != 0} {'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t puts "Trying Lower Dt: %f and Tol: %f ... "'%(Dt*0.01,Tol)))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t' + OpenSeesAPI.Analysis.Test.NormDispIncr(Tol,1000,0).CommandLine + ''))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t set ok [analyze %d %f ]'%(Steps,0.01*Dt)))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t }\n'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t if {$ok != 0} {\n'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t puts "Trying Lower Dt: %f and Tol: %f ... "'%(Dt*0.001,Tol)))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t' + OpenSeesAPI.Analysis.Test.NormDispIncr(Tol,1000,0).CommandLine + ''))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t set ok [analyze %d %f ]'%(Steps,0.001*Dt)))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t }\n'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t if {$ok != 0} {'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t puts "Trying Lower Dt: %f and Tol: %f ... "'%(Dt*0.0001,Tol)))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t' + OpenSeesAPI.Analysis.Test.NormDispIncr(Tol,1000,0).CommandLine + ''))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t set ok [analyze %d %f ]'%(Steps,0.0001*Dt)))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t }\n'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t if {$ok != 0} {'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t puts "Trying Lower Dt: %f and Tol: %f ... "'%(Dt*0.0000001,Tol)))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t' + OpenSeesAPI.Analysis.Test.NormDispIncr(Tol,1000,0).CommandLine + ''))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t set ok [analyze %d %f ]\n'%(Steps,0.0000001*Dt)))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t }'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('}'))

def TestComparison(OData, DisplacmentFileName, controlNodeID, DOF,):
    """
    TestComparison(Dt,Tol,DisplacementFileName,controlNodeID,DOF)
    Finds the solution of the system at specific diplacement steps defined in DisplacementFileName (.txt file) at
    the control node (controlNodeID) in the specified degree of freedom.
    :param OData: osapi database object
    :param DisplacmentFileName: displacement file name
    :param controlNodeID: control node id
    :param DOF: degree of freedom to push
    :return: adds the solution algorithm to the database file
    """
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('set fid [open %s r]'%DisplacmentFileName))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('set def [read $fid]'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('set numSteps [llength $def]'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('set ok 0 '))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('set stepNum 0'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('while {$ok == 0 && $stepNum < [expr $numSteps-1]} { '))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t set U1 [lindex $def $stepNum]'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t puts $U1'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t set U2 [lindex $def $stepNum+1]'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t set dU [expr $U2-$U1]'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t integrator DisplacementControl %s %d $dU 1 $dU $dU'%(controlNodeID,DOF)))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t set ok [analyze 1]'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('\t incr stepNum'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('}'))