"""
This class is used to create the following OpenSees TCL Commands:

"""

__author__ = 'Nasser'

# This Stores All The OpenSees Instances

from OpenSeesAPI import OpenSees
from OpenSeesAPI import Node
from OpenSeesAPI import TCL


class Collector(object):
    ''' This Declares Tcl File Headers
    Naming Convention for Element ID:
                        Nodes: 1ZZXXXX
                        SubNodes: 2ZZXXXX
                        OtherNodes: 3ZZXXXX
                        Reserved: 4ZZXXXX
                        Columns: 5ZZXXXX
                        Beams: 6ZZXXXX
                        Braces: 7ZZXXXX
                        Planes: 8ZZXXXX
                        ZeroLength/Other: 9ZZXXXX

                        GroupID is Story Number
    '''

    def __init__(self, OpenSeesCommand, FileLocation, TCLFileName):
        """

        :param OpenSeesCommand: Name of OpenSees Exeutable File
        :param FileLocation: Folder location of where you would like the analysis to be
        :param TCLFileName: Analysis File Name
        :return: OpenSeesAPI Collector Object. This is Where all the OSAPI objects are stored prior to running analysis

        """

        self._Executable = OpenSees.Executable(OpenSeesCommand, FileLocation, TCLFileName)
        self._Object = []
        self._Nodes = []
        self._Elements = []
        self._Materials = []
        self._Sections = []
        self._Restraint = []
        self._Quadrilaterals = []
        self._ElementIds = {}
        self._NodeIds = {}
        self._MaterialIds = {}
        self._SectionIds = {}

        #Analysis attributes
        self._Types = ''
        self._Constraints = []
        self._Numberers = []
        self._Systems = []
        self._Tests = []
        self._Algorithms = []
        self._Integrators = []
        self._Analyses = []
        self._Loads = []
        self._SolutionMethods = []

    @property
    def Executable(self):
        return self._Executable

    def AddObject(self, Obj):
        self._Object.append(Obj)
        self._Executable.AddCommand(Obj.CommandLine)
        return Obj

    def AddNode(self, Node):
        self._Nodes.append(Node)
        return Node

    def AddElement(self, Element):
        self._Elements.append(Element)
        return Element

    def AddMaterial(self, Material):
        self._Materials.append(Material)
        return Material

    def AddSection(self, Section):
        self._Sections.append(Section)
        return Section

    def AddRestraint(self, Constraint):
        self._Restraint.append(Constraint)
        return Constraint

    def AddQuadrilateral(self, Quarilateral):
        self._Quadrilaterals.append(Quarilateral)
        return Quarilateral

    def GetFreeNodeId(self, NodeType, GroupId):
        temp = '%d%d'%(NodeType, GroupId)
        if temp in self._NodeIds:
            self._NodeIds[temp] += 1
        else:
            self._NodeIds[temp] = 1
        id =  '%4.0f'%self._NodeIds[temp]
        id = id.replace(' ','0')
        return int('%s%s'%(temp,id))

    def GetFreeSectionId(self, SectionType, GroupId):
        temp = '%d%d'%(SectionType, GroupId)
        if temp in self._SectionIds:
            self._SectionIds[temp] += 1
        else:
            self._SectionIds[temp] = 1
        id =  '%4.0f'%self._SectionIds[temp]
        id = id.replace(' ','0')
        return int('%s%s'%(temp,id))

    def GetFreeElementId(self, ElementType, GroupId):
        temp = '%d%d'%(ElementType, GroupId)
        if temp in self._ElementIds:
            self._ElementIds[temp] += 1
        else:
            self._ElementIds[temp] = 1
        id =  '%4.0f'%self._ElementIds[temp]
        id = id.replace(' ','0')
        return int('%s%s'%(temp,id))

    def GetFreeMaterialId(self, MaterialType, GroupId):
        temp = '%d%d'%(MaterialType, GroupId)
        if temp in self._MaterialIds:
            self._MaterialIds[temp] += 1
        else:
            self._MaterialIds[temp] = 1
        id =  '%4.0f'%self._MaterialIds[temp]
        id = id.replace(' ','0')
        return int('%s%s'%(temp,id))

    def CreateNode(self, X, Y, Z=None, NodeType=1, GridX=None, GridY=None, GridZ=None, GroupId=1,_Notes=None):
        id = self.GetFreeNodeId(NodeType, GroupId)
        NodeI = Node.Node(id, X, Y, Z, GridX=GridX, GridY=GridY, GridZ=GridZ, NodeType=NodeType,_Notes=_Notes)
        self._Nodes.append(NodeI)
        return NodeI

    #Methods
    def GetNodesByYCoordinate(self, YCoordinate, NodeType=1):
        return list(filter(lambda x: x.Y==YCoordinate and x.NodeType==NodeType, self._Nodes))

    def GetNodesByZCoordinate(self, ZCoordinate, NodeType=1):
        return list(filter(lambda x: x.Z==ZCoordinate and x.NodeType==NodeType, self._Nodes))

    def GetNodesByGrid(self, GridX, GridY, GridZ=None, NodeType=1):
        if GridZ == None:
            return list(filter(lambda x: x.GridX==GridX and x.GridY==GridY and x.NodeType==NodeType, self._Nodes))
        else:
            return list(filter(lambda x: x.GridX==GridX and x.GridY==GridY and x.GridZ==GridZ and x.NodeType==NodeType, self._Nodes))

    def GetNodesByYGrid(self, GridY, NodeType=1):
        return list(filter(lambda x: x.GridY==GridY and x.NodeType==NodeType, self._Nodes))

    def GetNodesByZGrid(self, GridZ, NodeType=1):
        return list(filter(lambda x: x.GridZ==GridZ and x.NodeType==NodeType, self._Nodes))

    def GetNode(self, id):
        return list(filter(lambda x: x.id == id, self._Nodes))[0]

    def WriteModel(self):

        #Writing Nodes to File
        self._Executable.AddCommand(TCL.CodeTitle('Defining Nodes').CommandLine)
        for obj in self._Nodes:
            try:
                if obj.Used:
                    self._Executable.AddCommand(obj.CommandLine)
            except:
                continue

        #Write Materials from OpenSees Collector
        self._Executable.AddCommand(TCL.CodeTitle('Writing Materials').CommandLine)
        try:
            for obj in self._Materials:
                self._Executable.AddCommand(obj.CommandLine)
        except:
            print('Warning: No Materials added to Collector')

        #Write Sections from OpenSees Collector
        self._Executable.AddCommand(TCL.CodeTitle('Writing Sections').CommandLine)
        try:
            for obj in self._Sections:
                self._Executable.AddCommand(obj.CommandLine)
        except:
            print('Warning: No Sections added to Collector')

        #Write Elements from OpenSees Collector
        self._Executable.AddCommand(TCL.CodeTitle('Writing Elements').CommandLine)
        try:
            for obj in self._Elements:
                self._Executable.AddCommand(obj.CommandLine)
        except:
            print('Warning: No Elements added to Collector')

        #Write Shells from OpenSees Collector
        self._Executable.AddCommand(TCL.CodeTitle('Writing Shells').CommandLine)
        try:
            for obj in self._Quadrilaterals:
                self._Executable.AddCommand(obj.CommandLine)
        except:
            print('Warning: No Shells added to Collector')

        #Write Restraints from OpenSees Collector
        self._Executable.AddCommand(TCL.CodeTitle('Writing Constraints').CommandLine)
        try:
            for obj in self._Restraint:
                self._Executable.AddCommand(obj.CommandLine)
        except:
            print('Warning: No Constraints added to Collector')

    def AddType(self,Type):
        self._Types = Type
        return Type

    def AddConstraint(self, Constraint):
        self._Constraints = Constraint
        return Constraint

    def AddNumberer(self, Numberer):
        self._Numberers = Numberer
        return Numberer

    def AddSystem(self, System):
        self._Systems = System
        return System

    def AddTest(self, Test):
        self._Tests = Test
        return Test

    def AddAlgorithm(self, Algorithm):
        self._Algorithms = Algorithm
        return Algorithm

    def AddIntegrator(self, Integrator):
        self._Integrators = Integrator
        return Integrator

    def AddAnalysis(self, Analysis):
        self._Analyses = Analysis
        return Analysis

    def AddLoad(self, Load,option = 'append'):
        if option == 'append':
            self._Loads.append(Load)
        elif option == 'overwrite':
            self._Loads = []
            self._Loads.append(Load)
        return Load

    def AddSolutionMethod(self, SolutionMethod):
        self._SolutionMethods = SolutionMethod
        return SolutionMethod

    def WriteAnalysis(self):

        try:
            self._Executable.AddCommand(TCL.CodeTitle(self._Types).CommandLine)

            #Write Analysis Options from OpenSees Collector
            self._Executable.AddCommand(self._Constraints.CommandLine)
            self._Executable.AddCommand(self._Numberers.CommandLine)
            self._Executable.AddCommand(self._Systems.CommandLine)
            self._Executable.AddCommand(self._Tests.CommandLine)
            self._Executable.AddCommand(self._Algorithms.CommandLine)
            self._Executable.AddCommand(self._Integrators.CommandLine)
            self._Executable.AddCommand(self._Analyses.CommandLine)

            #Write Loads from OpenSees Collector
            for obj in self._Loads:
                self._Executable.AddCommand(obj.CommandLine)

            #Write Solution Method from OpenSees Collector
            self._Executable.AddCommand(self._SolutionMethods.CommandLine)

        except:
            print("%s Analysis object incomplete - cannot perform analysis"%self._Types)



# class AnalysisCollector(object):
#     '''
#     '''
#
#     def __init__(self, OpenSeesCommand, FileLocation, TCLFileName,Type):
#         """
#
#         :param OpenSeesCommand: Name of OpenSees Exeutable File
#         :param FileLocation: Folder location of where you would like the analysis to be
#         :param TCLFileName: Analysis File Name
#         :return: OpenSeesAPI Collector Object. This is Where all the OSAPI objects are stored prior to running analysis
#
#         """
#
#         self._Executable = OpenSees.Executable(OpenSeesCommand, FileLocation, TCLFileName)
#         self._Type = Type
#         self._Constraint = None
#         self._Numberer = None
#         self._System = None
#         self._Test = None
#         self._Algorithm = None
#         self._Integrator = None
#         self._Analysis = None
#         self._Loads = []
#         self._SolutionMethod = None
#
#     def AddConstraint(self, Constraint):
#         self._Constraint = Constraint
#         return Constraint
#
#     def AddNumberer(self, Numberer):
#         self._Numberer = Numberer
#         return Numberer
#
#     def AddSystem(self, System):
#         self._System = System
#         return System
#
#     def AddTest(self, Test):
#         self._Test = Test
#         return Test
#
#     def AddAlgorithm(self, Algorithm):
#         self._Algorithm = Algorithm
#         return Algorithm
#
#     def AddIntegrator(self, Integrator):
#         self._Integrator = Integrator
#         return Integrator
#
#     def AddAnalysis(self, Analysis):
#         self._Analysis = Analysis
#         return Analysis
#
#     def AddLoad(self, Load):
#         self._Loads.append(Load)
#         return Load
#
#     def AddSolutionMethod(self, SolutionMethod):
#         self._SolutionMethod = SolutionMethod
#         return SolutionMethod
#
#     def WriteAnalysis(self):
#
#         try:
#             self._Executable.AddCommand(TCL.CodeTitle(self._Type).CommandLine)
#
#             #Write Analysis Options from OpenSees Collector
#             self._Executable.AddCommand(TCL.CodeTitle('Analysis Options').CommandLine)
#             self._Executable.AddCommand(self._Constraint.CommmandLine)
#             self._Executable.AddCommand(self._Numberer.CommmandLine)
#             self._Executable.AddCommand(self._System.CommmandLine)
#             self._Executable.AddCommand(self._Test.CommmandLine)
#             self._Executable.AddCommand(self._Algoritihm.CommmandLine)
#             self._Executable.AddCommand(self._Integrator.CommmandLine)
#             self._Executable.AddCommand(self._Analysis.CommmandLine)
#
#             #Write Loads from OpenSees Collector
#             self._Executable.AddCommand(TCL.CodeTitle('Load Pattern').CommandLine)
#             for obj in self._Loads:
#                 self._Executable.AddCommand(obj.CommmandLine)
#
#             #Write Solution Method from OpenSees Collector
#             self._Executable.AddCommand(self._SolutionMethod.CommandLine)
#
#         except:
#             print("%s Analysis object incomplete - cannot perform analysis"%self._Type)



