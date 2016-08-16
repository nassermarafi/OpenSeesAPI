"""
This class is used to create the following OpenSees TCL Commands:
The following contain information about transfType? and the args required for each of the available geometric transformation types:
Linear Transformation
PDelta Transformation
Corotational Transformation
"""

__author__ = 'Nasser'

from OpenSeesAPI.OpenSees import OpenSees

class Linear(OpenSees):
    """
    For a two-dimensional problem:
    geomTransf Linear $transfTag <-jntOffset $dXi $dYi $dXj $dYj>
    For a three-dimensional problem:
    geomTransf Linear $transfTag $vecxzX $vecxzY $vecxzZ <-jntOffset $dXi $dYi $dZi $dXj $dYj $dZj>

    $transfTag	integer tag identifying transformation
    $vecxzX $vecxzY $vecxzZ	X, Y, and Z components of vecxz, the vector used to define the local x-z plane of the local-coordinate system. The local y-axis is defined by taking the cross product of the vecxz vector and the x-axis.
    These components are specified in the global-coordinate system X,Y,Z and define a vector that is in a plane parallel to the x-z plane of the local-coordinate system.
    These items need to be specified for the three-dimensional problem.
    $dXi $dYi $dZi	joint offset values -- offsets specified with respect to the global coordinate system for element-end node i (the number of arguments depends on the dimensions of the current model). The offset vector is oriented from node i to node j as shown in a figure below. (optional)
    $dXj $dYj $dZj	joint offset values -- offsets specified with respect to the global coordinate system for element-end node j (the number of arguments depends on the dimensions of the current model). The offset vector is oriented from node j to node i as shown in a figure below. (optional)

    A refresher on Euclidean Geometry and Coordinate Systems:
    A single vector may be defined by two points. It has length, direction, and location in space. When this vector is used to define a coordinate axis, only its direction is important. Now any 2 vectors, Vr and Vs, not parallel, define a plane that is parallel to them both. The cross-product of these vectors define a third vector, Vt, that is perpendicular to both Vr and Vs and hence normal to the plane: Vt = Vr X Vs.

    The element coordinate system is specified as follows:
    The x-axis is a vector given by the two element nodes; The vector vecxz is a vector the user specifies that must not be parallel to the x-axis. The x-axis along with the vecxz Vector define the xz plane. The local y-axis is defined by taking the cross product of the x-axis vector and the vecxz vector (Vy = Vxz X Vx). The local z-axis is then found simply by taking the cross product of the y-axis and x-axis vectors (Vz = Vx X Vy). The section is attached to the element such that the y-z coordinate system used to specify the section corresponds to the y-z axes of the element.
    """
    def __init__(self, id, VectorX=None, VectorY=None, VectorZ=None, **kwargs):
        self._id = id
        self._VectorX = VectorX
        self._VectorY = VectorY
        self._VectorZ = VectorZ

        self.__dict__.update(kwargs)

        if self._VectorX == None:
            self._CommandLine =  'geomTransf Linear %d'%(self.id)
        else:
            self._CommandLine =  'geomTransf Linear %d %d %d %d'%(self.id, self._VectorX, self._VectorY, self._VectorZ)


class PDelta(OpenSees):
    """
    For a two-dimensional problem:
    geomTransf PDelta $transfTag <-jntOffset $dXi $dYi $dXj $dYj>
    For a three-dimensional problem:
    geomTransf PDelta $transfTag $vecxzX $vecxzY $vecxzZ <-jntOffset $dXi $dYi $dZi $dXj $dYj $dZj>

    $transfTag	integer tag identifying transformation
    $vecxzX $vecxzY $vecxzZ	X, Y, and Z components of vecxz, the vector used to define the local x-z plane of the local-coordinate system. The local y-axis is defined by taking the cross product of the vecxz vector and the x-axis.
    These components are specified in the global-coordinate system X,Y,Z and define a vector that is in a plane parallel to the x-z plane of the local-coordinate system.
    These items need to be specified for the three-dimensional problem.
    $dXi $dYi $dZi	joint offset values -- offsets specified with respect to the global coordinate system for element-end node i (the number of arguments depends on the dimensions of the current model). The offset vector is oriented from node i to node j as shown in a figure below. (optional)
    $dXj $dYj $dZj	joint offset values -- offsets specified with respect to the global coordinate system for element-end node j (the number of arguments depends on the dimensions of the current model). The offset vector is oriented from node j to node i as shown in a figure below. (optional)
    """
    def __init__(self, id, VectorX=None, VectorY=None, VectorZ=None, **kwargs):
        self._id = id
        self._VectorX = VectorX
        self._VectorY = VectorY
        self._VectorZ = VectorZ

        self.__dict__.update(kwargs)

        if self._VectorX == None:
            self._CommandLine =  'geomTransf PDelta %d'%(self.id)
        else:
            self._CommandLine =  'geomTransf PDelta %d %d %d %d'%(self.id, self._VectorX, self._VectorY, self._VectorZ)

class Corotational(OpenSees):
    """
    For a two-dimensional problem:
    geomTransf Corotational $transfTag <-jntOffset $dXi $dYi $dXj $dYj>
    For a three-dimensional problem:
    geomTransf Corotational $transfTag $vecxzX $vecxzY $vecxzZ
PDelta
    $transfTag	integer tag identifying transformation
    $vecxzX $vecxzY $vecxzZ	X, Y, and Z components of vecxz, the vector used to define the local x-z plane of the local-coordinate system. The local y-axis is defined by taking the cross product of the vecxz vector and the x-axis.
    These components are specified in the global-coordinate system X,Y,Z and define a vector that is in a plane parallel to the x-z plane of the local-coordinate system.
    These items need to be specified for the three-dimensional problem.
    $dXi $dYi	joint offset values -- absolute offsets specified with respect to the global coordinate system for element-end node i (optional)
    $dXj $dYj	joint offset values -- absolute offsets specified with respect to the global coordinate system for element-end node j (optional)

    The element coordinate system is specified as follows:
    The x-axis is the axis connecting the two element nodes; the y- and z-axes are then defined using a vector that lies on a plane parallel to the local x-z plane -- vecxz. The local y-axis is defined by taking the cross product of the vecxz vector and the x-axis. The z-axis by taking cross product of x and new y. The section is attached to the element such that the y-z coordinate system used to specify the section corresponds to the y-z axes of the element.
   """
    def __init__(self, id, VectorX=None, VectorY=None, VectorZ=None, **kwargs):
        self._id = id
        self._VectorX = VectorX
        self._VectorY = VectorY
        self._VectorZ = VectorZ

        self.__dict__.update(kwargs)

        if self._VectorX == None:
            self._CommandLine =  'geomTransf Corotational %d'%(self.id)
        else:
            self._CommandLine =  'geomTransf Corotational %d %d %d %d'%(self.id, self._VectorX, self._VectorY, self._VectorZ)