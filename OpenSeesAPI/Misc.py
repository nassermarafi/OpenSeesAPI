__author__ = 'Nasser'

# List of Available Commands
# eleResponse Command
# getTime Command
# getEleTags Command
# getNodeTags
# loadConst
# nodeCoord
# nodeDisp
# nodeVel
# nodeAccel
# nodeEigenvector
# nodeBounds
# print
# printA
# remove
# reset
# setTime
# setMaxOpenFiles
# testIter
# testNorms
# wipe
# wipeAnalysis
# exit Command

from OpenSeesAPI.OpenSees import OpenSees

class Wipe(OpenSees):
    def __init__(self):
        self._CommandLine = 'wipe all;'
