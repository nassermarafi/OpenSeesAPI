############################################################################
##### This is a sample script that runs moment curvature analysis for a concrete columns
##### Coded by Nasser Marafi (marafi@uw.edu)
##### Last Updated: 12/15/2015
##### Make sure to have a subfolder called /tcl/ with the OpenSees Executable File
############################################################################
__author__ = 'marafi'

import os
import numpy as np

########################## Input Parameters ##########################

# OpenSeesCommand = os.getcwd()+'/tcl/OpenSees' # Path to the OpenSees Executable File
OpenSeesCommand = 'OpenSees' # Make sure Opensees is in your path if you use this

########################## Pre-Initialization ##########################
import OpenSeesAPI
import os
import numpy as np

########################## Initializing ##########################

### Create OpenSees Database

import time
import uuid
randomnumber = str(uuid.uuid4().get_hex().upper()[0:12])
timestamp = time.strftime("%y%m%d-%H%M%S")+randomnumber
ModelName = 'ExampleScript'
FileName = '%s-%s.tcl'%(ModelName,timestamp)

Directory = os.getcwd().replace('OpenSeesAPI','')
OData = OpenSeesAPI.Database.Collector(OpenSeesCommand, Directory+'/tcl/', FileName)

########################## Setup and Source Definition ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Initialization'))
OData.AddObject(OpenSeesAPI.Model.BasicBuilder(2,3))

########################## Define Building Geometry, Nodes and Constraints ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Geometry Setup'))

SupportNode = OData.CreateNode(0,0)
MassNode = OData.CreateNode(0,0)

########################## Define Geometric Transformations ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Define Geometric Transformations'))

#Define Geometry Transformations for Beams and Column
GeoTransfLinear = OpenSeesAPI.Model.Element.GeomTransf.Linear(1)
OData.AddObject(GeoTransfLinear)

##############################################################################
### All OpenSEES Objects are adding directly to the Database Beyond This Point
##############################################################################

########################## Define Materials and Sections ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Define Materials and Sections'))

########################## Define Rotational Springs for Plastic Hinge ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Define Rotational Springs for Plastic Hinge'))

#Define Rotational Spring
#### Collector Should Give ID

SteelMat = OpenSeesAPI.Model.Element.Material.UniaxialMaterial.Steel01(OData.GetFreeMaterialId(3,1), 78.3, 30000, 0.031)
ConcreteMat = OpenSeesAPI.Model.Element.Material.UniaxialMaterial.Concrete01(OData.GetFreeMaterialId(3,1), -4.35, -0.004, -2.0, -0.014)

OData.AddMaterial(SteelMat)
OData.AddMaterial(ConcreteMat)

FiberObjects = []
FiberObjects.append(OpenSeesAPI.Model.Element.Material.Section.FiberSection.Patch.Rect(ConcreteMat,100,100,0,0,20,40))
FiberObjects.append(OpenSeesAPI.Model.Element.Material.Section.FiberSection.Layer.Straight(SteelMat,8,1,2,2,18,2))
FiberObjects.append(OpenSeesAPI.Model.Element.Material.Section.FiberSection.Layer.Straight(SteelMat,8,1,2,38,18,38))

FiberSection = OpenSeesAPI.Model.Element.Material.Section.FiberSection(OData.GetFreeElementId(2,1),FiberObjects)

OData.AddMaterial(FiberSection)

########################## Define Elements ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Define Elements'))
# OData.AddElement(OpenSeesAPI.Model.Element.Element.ZeroLength(OData.GetFreeElementId(9,1),SupportNode, MassNode, [Spring],[1]))
OData.AddElement(OpenSeesAPI.Model.Element.Element.ZeroLengthSection(OData.GetFreeElementId(9,1),SupportNode, MassNode, FiberSection))

##############################################################################
### Start Writing Elements to the Executible File
##############################################################################

# Setting Nodes as Used
for object in set(OData._Elements):
    object._NodeI.__setattr__('Used',True)
    object._NodeJ.__setattr__('Used',True)

#Writing Nodes to File
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Defining Nodes'))
for obj in OData._Nodes:
    try:
        if obj.Used:
            OData.Executable.AddCommand(obj.CommandLine)
    except:
        continue

#Defining Fixity
OData.AddConstraint(OpenSeesAPI.Model.Constraint.Fix(SupportNode,[1,1,1]))
OData.AddConstraint(OpenSeesAPI.Model.Constraint.Fix(MassNode,[0,1,0]))

#Defining Masses

#Write Element from OpenSees Collector
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Writing Materials'))
for obj in OData._Materials:
    OData.Executable.AddCommand(obj.CommandLine)

#Write Sections from OpenSees Collector
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Writing Sections'))
for obj in OData._Sections:
    OData.Executable.AddCommand(obj.CommandLine)

#Write Elements from OpenSees Collector
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Writing Elements'))
for obj in OData._Elements:
    OData.Executable.AddCommand(obj.CommandLine)

#Write Shells from OpenSees Collector
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Writing Shells'))
for obj in OData._Quadrilaterals:
    OData.Executable.AddCommand(obj.CommandLine)

#Write Constraints from OpenSees Collector
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Writing Constraints'))
for obj in OData._Constraints:
    OData.Executable.AddCommand(obj.CommandLine)

########################## Eigenvalue Analysis ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Eigenvalue Analysis'))

########################## Rayleigh Damping ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Rayleigh Damping'))

########################## Loads ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Loads'))

########################## Time Series ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Time Series'))


########################## Recorders ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Recorder Setup'))

OutputFolder = 'Results'

Displacement_File_Name = '%s-NodeD-%s.dat'%(ModelName,timestamp)
OData.AddObject(OpenSeesAPI.Output.Recorder.Node(OutputFolder+'/'+Displacement_File_Name, [MassNode], [3], 'disp'))

Reaction_File_Name = '%s-NodeReact-%s.dat'%(ModelName,timestamp)
OData.AddObject(OpenSeesAPI.Output.Recorder.Node(OutputFolder+'/'+Reaction_File_Name, [SupportNode], [3], 'reaction'))

########################## Display Results ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Display Results'))

########################## Gravity Analysis ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Gravity Analysis'))

#Load Pattern
GravityLoads = [OpenSeesAPI.Model.Pattern.Load(MassNode,[-200.,0,0])]
OData.AddObject(OpenSeesAPI.Model.Pattern.Plain(100,'Linear', GravityLoads)) #Noticed that  my loading and his are different

#Run Analysis
OData.AddObject(OpenSeesAPI.TCL.TCLScript('set ok 0;'))
OData.AddObject(OpenSeesAPI.Analysis.Integrator.Static.LoadControl(1,1))
OData.AddObject(OpenSeesAPI.Analysis.Analysis.Static())
OData.AddObject(OpenSeesAPI.TCL.TCLScript('set ok [analyze 1]'))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('if {$ok == 0} {puts "Gravity Analysis Success"} else { puts "Grsvity Analysis Failed" }'))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('loadConst -time 0.0'))

########################## Pushover Analysis ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Pushover Analysis'))

#Load Pattern
PushOverLoads = [OpenSeesAPI.Model.Pattern.Load(MassNode,[0,0,1])]
OData.AddObject(OpenSeesAPI.Model.Pattern.Plain(200,'Linear', PushOverLoads)) #Noticed that  my loading and his are different

#Define Analysis
OData.AddObject(OpenSeesAPI.Analysis.Constraints.Transformation())
OData.AddObject(OpenSeesAPI.Analysis.Numberer.RCM())
# OData.AddObject(OpenSeesAPI.Analysis.System.Mumps(Optional='-ICNTL 50'))
OData.AddObject(OpenSeesAPI.Analysis.System.BandGeneral())
OData.AddObject(OpenSeesAPI.Analysis.Test.EnergyIncr(1e-4, 10000))
# OData.AddObject(OpenSeesAPI.Analysis.Test.RelativeNormDispIncr(1e-6,1000))
OData.AddObject(OpenSeesAPI.Analysis.Algorithm.NewtonLineSearch())
ControlNode = MassNode
# OData.AddObject(OpenSeesAPI.Analysis.Integrator.Static.DisplacementControl(ControlNode, 1, 0.01))
# OData.AddObject(OpenSeesAPI.Analysis.Analysis.Static())

TargetDrifts = [0,0.01,-0.01,0.01,-0.01,0.02,-0.02,0.02,-0.02,0.04,-0.04,0.04,-0.04, 0.08, -0.08, 0.08, -0.08]
StepSize = 0.0001
LoadingSequence = []
for i in range(1,len(TargetDrifts),1):
    LoadingSequence.extend(list(np.linspace(TargetDrifts[i-1],TargetDrifts[i],int(abs(TargetDrifts[i]-TargetDrifts[i-1])/StepSize)+1)))
LoadingSequence = np.array(LoadingSequence)/100.

#Run Analysis
OData.AddObject(OpenSeesAPI.TCL.TCLScript('set ok 0;'))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('set step 0;'))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('set prevDisp 0'))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('set Drifts [list %s]'%(''.join(map(lambda x: '%f \t'%(x), LoadingSequence)))))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('foreach targetDisp $Drifts {'))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('integrator DisplacementControl %d 3 [expr $targetDisp-$prevDisp]'%ControlNode._id))
OData.AddObject(OpenSeesAPI.Analysis.Analysis.Static())
OData.AddObject(OpenSeesAPI.TCL.TCLScript('set ok [analyze 1]'))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('puts "Running Push Over Step: $step"'))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('incr step'))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('set prevDisp $targetDisp'))
# OData.AddObject(OpenSeesAPI.TCL.TCLScript('puts "Not Ok Doing Other Stuff'))

OData.AddObject(OpenSeesAPI.TCL.TCLScript('}'))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('if {$ok == 0} {puts "Analysis Success"} else { puts "Analysis Failed" }'))

########################## Time History Analysis ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Time History Analysis'))

########################## Close File ##########################
OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Close File'))

OData.AddObject(OpenSeesAPI.TCL.TCLScript('wipe al b l;'))
OData.AddObject(OpenSeesAPI.TCL.TCLScript('puts "Models Run Complete";'))

##############################################################################
### Start Running OpenSees File
##############################################################################

########################## Plot Geometry ##########################

########################## Run OpenSees Script ##########################
OData.Executable.StartAnalysis(SuppressOutput=False)

########################## Load Result Files ##########################
Displ = np.loadtxt(Directory+'/tcl/'+OutputFolder+'/'+Displacement_File_Name)
Reac = np.loadtxt(Directory+'/tcl/'+OutputFolder+'/'+Reaction_File_Name)

########################## Removing Files ##########################

try:
    os.remove(Directory+'/tcl/%s-%s.out'%(ModelName,timestamp))
except:
    pass

os.remove(Directory+'/tcl/%s-%s.tcl'%(ModelName,timestamp))
os.remove(Directory+'/tcl/'+OutputFolder+'/'+Displacement_File_Name)
os.remove(Directory+'/tcl/'+OutputFolder+'/'+Reaction_File_Name)

########################## Plot Push Over ##########################

import matplotlib.pylab as plt
plt.figure(figsize=(4,4))
plt.plot(Displ[1:,1], Reac[1:, 1])
plt.xlabel('Curvature'); plt.ylabel('Moment, k-in')
plt.grid()
plt.show()