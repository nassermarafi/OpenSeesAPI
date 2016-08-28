"""
This class is used to create the following OpenSees TCL Commands:

"""

__author__ = 'Nasser'

# This Stores All The OpenSees Instances

import OpenSeesAPI

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

        self._Executable = OpenSeesAPI.Executable(OpenSeesCommand, FileLocation, TCLFileName)
        self._Object = []
        self._Nodes = []
        self._Elements = []
        self._Materials = []
        self._Sections = []
        self._Constraints = []
        self._Quadrilaterals = []
        self._ElementIds = {}
        self._NodeIds = {}
        self._MaterialIds = {}
        self._SectionIds = {}

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

    def AddConstraint(self, Constraint):
        self._Constraints.append(Constraint)
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
        Node = OpenSeesAPI.Model.Node.Node(id, X, Y, Z, GridX=GridX, GridY=GridY, GridZ=GridZ, NodeType=NodeType,_Notes=_Notes)
        self._Nodes.append(Node)
        return Node

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