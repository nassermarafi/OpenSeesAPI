"""
This class is used to create the following OpenSees TCL Commands:

"""

__author__ = 'Nasser'

# List of Available Commands
# These commands are used to get output from OpenSees:
# recorder
# record
# print
# printA
# logFile
# RealTime Output Commands

from OpenSeesAPI.OpenSees import OpenSees

class LogFile(OpenSees):
    """
    logFile $fileName <-append>
to save the warning and error messages that the running script generates from the interpreter to an output file given by $fileName. By default the file, if it exists prior to running, is overwritten with new data. If the -append option is provided the new data is appended to the end of the existing file.
    """
    def __init__(self, FileName):
        self._FileName = FileName
        self._CommandLine = 'logFile %s;'%FileName

class Recorder:
    class Node(OpenSees):
        """
        The Node recorder type records the response of a number of nodes at every converged step. The command to create a node recorder is:
        recorder Node <-file $fileName> <-xml $fileName> <-binary $fileName> <-tcp $inetAddress $port> <-precision $nSD> <-timeSeries $tsTag> <-time> <-dT $deltaT> <-closeOnWrite> <-node $node1 $node2 ...> <-nodeRange $startNode $endNode> <-region $regionTag> -dof ($dof1 $dof2 ...) $respType'
        $fileName	name of file to which output is sent.
        file output is either in xml format (-xml option), textual (-file option) or binary (-binary option)
        inetAddr	ip address, "xx.xx.xx.xx", of remote machine to which data is sent
        $port	port on remote machine awaiting tcp
        $nSD	number of significant digits (optional, default is 6)
        -time	optional, using this option places domain time in first entry of each data line, default is to have time ommitted
        -closeOnWrite	optional. using this option will instruct the recorder to invoke a close on the data handler after every timestep. If this is a file it will close the file on every step and then re-open it for the next step. Note, this greatly slows the execution time, but is useful if you need to monitor the data during the analysis.
        $deltaT	time interval for recording. will record when next step is $deltaT greater than last recorder step. (optional, default: records at every time step)
        $tsTag	the tag of a previously constructed TimeSeries, results from node at each time step are added to load factor from series
        $node1 $node2 ..	tags of nodes whose response is being recorded (optional, default: omitted)
        $startNode $endNode ..	tag for start and end nodes whose response is being recorded (optional, default: omitted)
        $regionTag	a region tag; to specify all nodes in the previously defined region. (optional)
        $dof1 dof2 ...	the specified dof at the nodes whose response is requested.
        $respType	a string indicating response required. Response types are given in table below.
        disp	displacement*
        vel	velocity*
        accel	acceleration*
        incrDisp	incremental displacement
        "eigen i"	eigenvector for mode i
        reaction	nodal reaction
        rayleighForces	damping forces

        RETURNS
        >0 an integer tag that can be used as a handle on the recorder for the remove recorder commmand.
        -1 recorder command failed if integer -1 returned.
        """
        def __init__(self, FilePath, Nodes, DOFs, Variable, Optional='', FileType='-file'):
            self._FilePath = FilePath
            self._Nodes = Nodes #Node Class in List
            self._DOFs = DOFs #[1,2,3]
            self._Variable = Variable #disp, vel, accel, reaction
            self._FileType = FileType
            self._Optional = Optional #-timeSeries id for accel
            OutputNodes = ''
            for node in self._Nodes:
                OutputNodes += ' %d'%node.id
            OutputDOF = ''
            for dof in self._DOFs:
                OutputDOF += ' %d'%dof

            self._CommandLine = 'recorder Node %s %s %s -time -node %s -dof %s %s'%(self._FileType,self._FilePath,
                                                                                    self._Optional, OutputNodes,
                                                                                    OutputDOF, self._Variable)

    class Element(OpenSees):
        """
        The Element recorder type records the response of a number of elements at every converged step. The response recorded is element-dependent and also depends on the arguments which are passed to the setResponse() element method.
        The command to create an element recorder is:
        recorder Element <-file $fileName> <-xml $fileName> <-binary $fileName> <-precision $nSD> <-time> <-closeOnWrite> <-dT $deltaT> <-ele ($ele1 $ele2 ...)> <-eleRange $startEle $endEle> <-region $regTag> $arg1 $arg2 ...
        $fileName	name of file to which output is sent.
        file output is either in xml format (-xml option), textual (-file option) or binary (-binary option)
        $nSD	number of significant digits (optional, default is 6)
        -time	(optional using this option places domain time in first entry of each data line, default is to have time ommitted)
        -closeOnWrite	optional. using this option will instruct the recorder to invoke a close on the data handler after every timestep. If this is a file it will close the file on every step and then re-open it for the next step. Note, this greatly slows the execution time, but is useful if you need to monitor the data during the analysis.
        $deltaT	time interval for recording. will record when next step is $deltaT greater than last recorder step. (optional, default: records at every time step)
        $ele1 $ele2 ..	tags of elements whose response is being recorded -- selected elements in domain (optional, default: omitted)
        $startEle $endEle ..	tag for start and end elements whose response is being recorded -- range of selected elements in domain (optional, default: omitted)
        $regTag	previously-defined tag of region of elements whose response is being recorded -- region of elements in domain (optional)
        $arg1 $arg2 ...	arguments which are passed to the setResponse() element method

        RETURNS
        >0 an integer tag that can be used as a handle on the recorder for the remove recorder commmand.
        -1 recorder command failed if integer -1 returned.
        """

        def __init__(self, FilePath, Elements, ResponseType, FileType='-file', Optional='', **kwargs):
            self._FilePath = FilePath
            self._Elements = Elements
            self._ResponseType = ResponseType
            self._FileType = FileType
            self._Optional = Optional

            self.__dict__.update(kwargs)

            self._CommandLine = 'recorder Element %s %s -time %s -ele %s %s'%(self._FileType, self._FilePath,
                                                                              self._Optional,
                                                                              ''.join(map(lambda x: ' %d'%x.id, self._Elements)),self._ResponseType)

class NodeDisp(OpenSees):
    def __init__(self, Node, DOF):
        self._Node = Node
        self._DOF = DOF

    @property
    def CommandLine(self):
        self._CommandLine = 'nodeDisp %d %d'%(self._Node.id, self._DOF)
        return self._CommandLine

class NodeReac(OpenSees):
    def __init__(self, Node, DOF):
        self._Node = Node
        self._DOF = DOF

    @property
    def CommandLine(self):
        self._CommandLine = 'nodeReaction %d %d'%(self._Node.id, self._DOF)
        return self._CommandLine

class NodeEigenVector(OpenSees):
    def __init__(self, Node, Mode, DOF, **kwargs):
        self._Node = Node
        self._Mode = Mode
        self._DOF = DOF
        self.__dict__.update(kwargs)

        self._CommandLine = 'nodeEigenvector %d %d %d'%(self._Node.id, self._Mode, self._DOF)