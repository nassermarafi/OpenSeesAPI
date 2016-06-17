__author__ = 'marafi'

from OpenSeesAPI.OpenSees import OpenSees

class FiberSection(OpenSees):
    """
    This commnand allows the user to construct a FiberSection object. Each FiberSection object is composed of Fibers, with each fiber containing a UniaxialMaterial, an area and a location (y,z). The command to generate FiberSection object contains in { } the commands to generate all the fibers in the object. To construct a FiberSection and populate it, the following command is used:
    section Fiber $secTag <-GJ $GJ> {
    fiber...
    patch...
    layer...
    ...
    }

    $secTag	unique tag among sections
    $GJ	linear-elastic torsional stiffness assigned to the section (optional, default = no torsional stiffness)
    fiber...	command to generate a single fiber
    patch...	command to generate a number of fibers over a geometric cross-section
    layer...	command to generate a row of fibers along a geometric-arc
    """
    def __init__(self, id, fibers, GJ=None, **kwargs):
        self._id = id
        self._fibers = fibers
        self._GJ = GJ

        self.__dict__.update(kwargs)

        self._EndCommand = ''
        if self._GJ != None:
            self._EndCommand = '-GJ %f'%self._GJ
        self._CommandLine =  'section Fiber %d %s { \n'%(self._id, self._EndCommand)+''.join(map(lambda x: ' %s\n'%x._CommandLine, self._fibers))+'}'

    class Fiber:
        class Fiber(object):
            """
            fiber $yLoc $zLoc $A $matTag

            $yLoc	y coordinate of the fiber in the section (local coordinate system)
            $zLoc	z coordinate of the fiber in the section (local coordinate system)
            $A	area of the fiber.
            $matTag	material tag associated with this fiber (UniaxialMaterial tag for a FiberSection and NDMaterial tag for use in an NDFiberSection).
            """
            def __init__(self, yLoc, zLoc, A, Mat, **kwargs):
                self._yLoc = yLoc
                self._zLoc = zLoc
                self._A = A
                self._Mat = Mat
                self.__dict__.update(kwargs)

                self._CommandLine =  'fiber %f %f %f %d'%(self.yLoc, self._zLoc, self._A, self._Mat.id)

    class Layer:
        class Straight(object):
            """
            layer straight $matTag $numFiber $areaFiber $yStart $zStart $yEnd $zEnd

            $matTag	material tag of previously created material (UniaxialMaterial tag for a FiberSection or NDMaterial tag for use in an NDFiberSection)
            $numFibers	number of fibers along line
            $areaFiber	area of each fiber
            $yStart $zEnd	y and z-coordinates of first fiber in line (local coordinate system)
            $$yEnd $zEnd	y and z-coordinates of last fiber in line (local coordinate system)
            """
            def __init__(self, Mat, numFiber, areaFiber ,yStart ,zStart ,yEnd ,zEnd ,**kwargs):
                self._Mat = Mat
                self._numFiber = numFiber
                self._areaFiber = areaFiber
                self._yStart = yStart
                self._zStart = zStart
                self._yEnd = yEnd
                self._zEnd = zEnd
                self.__dict__.update(kwargs)

                self._CommandLine =  'layer straight %d %d %f %f %f %f %f'%(self._Mat.id, self._numFiber, self._areaFiber, self._yStart, self._zStart, self._yEnd, self._zEnd)

        class Circ(object):
            """
            layer circ $matTag $numFiber $areaFiber $yCenter $zCenter $radius <$startAng $endAng>

            $matTag	material tag of previously created material (UniaxialMaterial tag for a FiberSection or NDMaterial tag for use in an NDFiberSection)
            $numFiber	number of fibers along arc
            $areaFiber	area of each fiber
            $yCenter $zCenter	y and z-coordinates of center of circular arc
            $radius	radius of circlular arc
            $startAng	starting angle (optional, default = 0.0)
            $endAng	ending angle (optional, default = 360.0 - 360/$numFiber)
            """
            def __init__(self, Mat, numFiber, areaFiber, yCenter, zCenter, radius, startAng=None, endAng=None, **kwargs):
                self._Mat = Mat
                self._numFiber = numFiber
                self._areaFiber = areaFiber
                self._yCenter = yCenter
                self._zCenter = zCenter
                self._radius = radius
                self._startAng = startAng
                self._endAng = endAng
                self.__dict__.update(kwargs)

                if startAng != None:
                    self._EndCommand = '%f %f'%(self._startAng, self._endAng)
                else:
                    self._EndCommand = ''
                self._CommandLine =  'layer circ %d %d %f %f %f %f %s'%(self._Mat.id, self._numFiber, self._areaFiber, self._yCenter, self._zCenter, self._radius, self._EndCommand)

    class Patch:
        class Quad(object):
            """
            patch quad $matTag $numSubdivIJ $numSubdivJK $yI $zI $yJ $zJ $yK $zK $yL $zL
            $matTag	tag of previously defined material (UniaxialMaterial tag for a FiberSection or NDMaterial tag for use in an NDFiberSection)
            $numSubdivIJ	number of subdivisions (fibers) in the IJ direction.
            $numSubdivJK	number of subdivisions (fibers) in the JK direction.
            $yI $zI	y & z-coordinates of vertex I (local coordinate system)
            $yJ $zJ	y & z-coordinates of vertex J (local coordinate system)
            $yK $zK	y & z-coordinates of vertex K (local coordinate system)
            $yL $zL	y & z-coordinates of vertex L (local coordinate system)
            """
            def __init__(self, Mat, numSubDivIJ, numSubDibJK, yI, zI, yJ, zJ, yK, zK, yL, zL, **kwargs):
                self._Mat = Mat
                self._numSubDivIJ = numSubDivIJ
                self._numSubDivJK = numSubDibJK
                self._yI = yI
                self._zI = zI
                self._yJ = yJ
                self._zJ = zJ
                self._yK = yK
                self._zK = zK
                self.yL = yL
                self.zL = zL
                self.__dict__.update(kwargs)

                self._CommandLine =  'patch quad %d %d %d %f %f %f %f %f %f %f %f'%(self._Mat.id, self._numSubDivIJ, self._numSubDivJK, self._yI, self._zI, self._yJ, self._zJ, self._yK, self._zK, self._yL, self._zL)

        class Rect(object):
            """
            patch rect $matTag $numSubdivY $numSubdivZ $yI $zI $yJ $zJ
            $matTag	tag of previously defined material (UniaxialMaterial tag for a FiberSection or NDMaterial tag for use in an NDFiberSection)
            $numSubdivY	number of subdivisions (fibers) in the local y direction.
            $numSubdivZ	number of subdivisions (fibers) in the local z direction.
            $yI $zI	y & z-coordinates of vertex I (local coordinate system)
            $yJ $zJ	y & z-coordinates of vertex J (local coordinate system)
            """
            def __init__(self, Mat, numSubDivIJ, numSubDibJK, yI, zI, yJ, zJ, **kwargs):
                self._Mat = Mat
                self._numSubDivIJ = numSubDivIJ
                self._numSubDivJK = numSubDibJK
                self._yI = yI
                self._zI = zI
                self._yJ = yJ
                self._zJ = zJ
                self.__dict__.update(kwargs)

                self._CommandLine =  'patch rect %d %d %d %f %f %f %f'%(self._Mat.id, self._numSubDivIJ, self._numSubDivJK, self._yI, self._zI, self._yJ, self._zJ)

        class Circ(object):
            """
            patch circ $matTag $numSubdivCirc $numSubdivRad $yCenter $zCenter $intRad $extRad <$startAng $endAng>

            $matTag	tag of previously defined material (UniaxialMaterial tag for a FiberSection or NDMaterial tag for use in an NDFiberSection)
            $numSubdivCirc	number of subdivisions (fibers) in the circumferential direction
            $numSubdivRad	number of subdivisions (fibers) in the radial direction.
            $yCenter $zCenter	y & z-coordinates of the center of the circle
            $intRad	internal radius
            $extRad	external radius
            $startAng	starting angle (optional. default=0.0)
            $endAng	ending angle (optional. default=360.0)
            """
            def __init__(self, Mat, numSubDivIJ, numSubDibJK, yCenter, zCenter, intRad, extRad, startAng=None, endAng=None, **kwargs):
                self._Mat = Mat
                self._numSubDivIJ = numSubDivIJ
                self._numSubDivJK = numSubDibJK
                self._yCenter = yCenter
                self._zCenter = zCenter
                self._intRad = intRad
                self._extRad = extRad
                self._startAng = startAng
                self._endAng = endAng
                self.__dict__.update(kwargs)

                if startAng != None:
                    self._EndCommand = '%f %f'%(self._startAng, self._endAng)
                else:
                    self._EndCommand = ''
                self._CommandLine =  'patch circ %d %d %d %f %f %f %f %s'%(self._Mat.id, self._numSubDivIJ, self._numSubDivJK, self._yCenter, self._zCenter, self._intRad, self._extRad, self._EndCommand)

