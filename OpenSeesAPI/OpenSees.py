"""
This class is used to create the following OpenSees TCL Commands:

"""

__author__ = 'Nasser'

class Executable(object):
    def __init__(self, OpenSeesCommand, FileLocation, TCLFileName):
        import os

        self._OpenSeesCommand = OpenSeesCommand
        self._Filelocation = FileLocation
        self._TCLFileName = TCLFileName
        self._TCLFileLocation = os.path.join(FileLocation,TCLFileName)
        self._CommandLines = []
        self._Console = None
        try:
            self._Log = self._TCLFileName[:-4]+'.log'
        except:
            print('TCL File Name Too Short')

    def AddCommand(self, Command):
        self._CommandLines.append(Command)

    def StartAnalysis(self, SuppressOutput = True):
        # Write Command Lines to Tcl File
        tcl = open(self._TCLFileLocation,'w')
        for line in self._CommandLines:
            tcl.write(line+'\n')
        tcl.close()

        # Run OpenSees
        print('Running OpenSees Tcl File: %s'%(self._TCLFileName))
        from subprocess import Popen, PIPE, STDOUT
        if SuppressOutput:
            import os
            FNULL = open(os.devnull, 'w')
            p = Popen([self._OpenSeesCommand, self._TCLFileLocation], cwd=self._Filelocation, stdout=FNULL, stderr=STDOUT)
            p.wait()
        else:
            p = Popen([self._OpenSeesCommand, self._TCLFileLocation], cwd=self._Filelocation )
            p.wait()

    def DeleteTCLFile(self):
        try:
            import os
            os.remove(self._TCLFileLocation)
        except:
            print('Error Deleting TCL File')

    def DeleteLogFile(self):
        try:
            import os
            os.remove(self._Filelocation+self._Log)
        except:
            print('Error Deleting LOG File')

    @property
    def LogFileName(self):
        return self._Log

class OpenSees(object):
    def __init__(self):
        self._CommandLine = None
        self._Executable = Executable(None)

    @property
    def CommandLine(self):
        try:
            return self._CommandLine + ';    #' + self._Notes
        except:
            return self._CommandLine

    @property
    def id(self):
        return self._id

    def Execute(self):
        self._Executable.StartAnalysis()

    def AddObject(self, Object):
        self._Executable.AddCommand(Object.CommandLine())
