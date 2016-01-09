__author__ = 'Nasser'

from OpenSeesAPI.OpenSees import OpenSees

class Puts(OpenSees):
    def __init__(self, Output):
        self._Output = Output
        self._CommandLine = 'puts "%s"'%Output

class CodeCommentor(OpenSees):
    def __init__(self, Comment):
        self._Comment = Comment

    @property
    def CommandLine(self):
        self._CommandLine = '#'+self._Comment
        return self._CommandLine

class CodeTitle(OpenSees):
    def __init__(self, Comment):
        self._Comment = Comment

    @property
    def CommandLine(self):
        self._CommandLine = '\n#####################\n'+ 'puts "%s"'%self._Comment+'\n#####################\n'
        return self._CommandLine

class TCLScript(OpenSees):
    def __init__(self, Script):
        self._CommandLine = Script

class LogFile(OpenSees):
    def __init__(self, FileName):
        self._CommandLine = 'logFile %s'%FileName

## Make Directory

## For Loops

## While Loops

## Print Function

## Other Functions

## Misc Command

