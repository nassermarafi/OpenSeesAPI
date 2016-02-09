"""
This class is used to create the following OpenSees TCL Commands:
This command is used to perform the analysis.
analyze $numIncr <$dt> <$dtMin $dtMax $Jd>
$numIncr	number of analysis steps to perform.
$dt	time-step increment. Required if transient or variable transient analysis
$dtMin $dtMax	minimum and maximum time steps. Required if a variable time step transient analysis was specified.
$Jd	number of iterations user would like performed at each step. The variable transient analysis will change current time step if last analysis step took more or less iterations than this to converge.
Required if a variable time step transient analysis was specified.
RETURNS:
0 if successful
<0 if NOT successful

EXAMPLE:
set ok [anlayze 10]; # perform 10 static analysis steps
set ok [analyze 2000 0.01]; # perform 2000 transient time steps at 0.01 increments

"""

__author__ = 'Nasser'


from OpenSeesAPI.OpenSees import OpenSees

class Analyze(OpenSees):
    def __init__(self, Steps, Increments=None):
        self._Steps = Steps
        self._Increments = Increments

    @property
    def CommandLine(self):
        if self._Increments == None:
            self._CommandLine = 'set ok [analyze %d]'%self._Steps
        else:
            self._CommandLine = 'set ok [analyze %d %f]'%(self._Steps, self._Increments)

        return self._CommandLine

