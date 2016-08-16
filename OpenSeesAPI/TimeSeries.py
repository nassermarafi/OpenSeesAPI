"""
This class is used to create the following OpenSees TCL Commands:
Constant TimeSeries
Linear TimeSeries
Trigonometric TimeSeries
Triangular TimeSeries
Rectangular TimeSeries
Pulse TimeSeries
Path TimeSeries
PeerMotion
PeerNGAMotion
"""

__author__ = 'marafi'

from OpenSeesAPI.OpenSees import OpenSees

class Path(OpenSees):
    """
    This command is used to construct a Path TimeSeries object. The relationship between load factor and time is input by the user as a series of discrete points in the 2d space (load factor, time). The input points can come from a file or from a list in the script. When the time specified does not match any of the input points, linear interpolation is used between points. There are many ways to specify the load path:
    For a load path where the factors are specified in a tcl list with a constant time interval between points:
    timeSeries Path $tag -dt $dt -values {list_of_values} <-factor $cFactor>
    For a load path where the factors are specified in a file for a constant time interval between points:
    timeSeries Path $tag -dt $dt -filePath $filePath <-factor $cFactor>
    For a load path where the values are specified at non-constant time intervals:
    timeSeries Path $tag -time {list_of_times} -values {list_of_values} <-factor $cFactor>
    For a load path where both time and values are specified in a list included in the command
    timeSeries Path $tag -fileTime $fileTime -filePath $filePath <-factor $cFactor>
    """
    def __init__(self, id, dt, ValuesList):
        self._id = id
        self._dt = dt
        self._ValueList = ValuesList
        self._CommandLine = 'timeSeries Path %d -dt %f -values {%s}'%(self._id, self._dt, ''.join([' %f'%x for x in self._ValueList]))