__author__ = 'marafi'

# Constant TimeSeries
# Linear TimeSeries
# Trigonometric TimeSeries
# Triangular TimeSeries
# Rectangular TimeSeries
# Pulse TimeSeries
# Path TimeSeries
# PeerMotion
# PeerNGAMotion

from OpenSeesAPI.OpenSees import OpenSees

class Path(OpenSees):
    def __init__(self, id, dt, ValuesList):
        self._id = id
        self._dt = dt
        self._ValueList = ValuesList
        self._CommandLine = 'timeSeries Path %d -dt %f -values {%s}'%(self._id, self._dt, ''.join([' %f'%x for x in self._ValueList]))