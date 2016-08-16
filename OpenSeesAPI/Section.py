__author__ = 'marafi'

"""
section secType? secTag? arg1? ...

The type of section created and the additional arguments required depends on the secType? provided in the command.

NOTE:
The valid queries to any section when creating an ElementRecorder are 'force', and 'deformation'. Some sections have additional queries to which they will respond. These are documented in the NOTES section for those sections.

The following contain information about secType? and the args required for each of the available section types:
Elastic Section
Fiber Section
NDFiber Section
Wide Flange Section
RC Section
Parallel Section
Section Aggregator
Uniaxial Section
Elastic Membrane Plate Section
Plate Fiber Section
Bidirectional Section
Isolator2spring Section
"""

from OpenSeesAPI.OpenSees import OpenSees

class Elastic(OpenSees):
    """
    section Elastic $secTag $E $A $Iz <$G $alphaY>
    section Elastic $secTag $E $A $Iz $Iy $G $J <$alphaY $alphaZ>

    $secTag	unique section tag
    $E	Young's Modulus
    $A	cross-sectional area of section
    $Iz	second moment of area about the local z-axis
    $Iy	second moment of area about the local y-axis (required for 3D analysis)
    $G	Shear Modulus (optional for 2D analysis, required for 3D analysis)
    $J	torsional moment of inertia of section (required for 3D analysis)
    $alphaY	shear shape factor along the local y-axis (optional)
    $alphaZ	shear shape factor along the local z-axis (optional)
    """
    def __init__(self, id, E, A, Iz, G=None, Iy=None, J=None, AlphaY=None, AlphaZ=None, **kwargs):
        self._id = id
        self._E = E
        self._A = A
        self._Iz = Iz
        self._G = G
        self._Iy =Iy
        self._J = J
        self._AlphaY = AlphaY
        self._AlphaZ = AlphaZ
        self._EndCommand = ''
        self.__dict__.update(kwargs)

        if self._J==None:
            if self._self._G != None:
                self._EndCommand = '%f %f'%(self._G, self._AlphaY)
            self._CommandLine =  'section Elastic %d %f %f %f %s'%(self._id, self._E, self._A, self._Iz, self._EndCommand)
        else:
            if self._AlphaY != None:
                self._EndCommand = '%f %f'%(self._AlphaY, self._AlphaZ)
            self._CommandLine =  'section Elastic %d %f %f %f %f %f %f %s'%(self._id, self._E, self._A , self._Iz, self._Iy, self._G, self._J, self._EndCommand)

class WFSection2d(OpenSees):
    """
    section WFSection2d $secTag $matTag $d $tw $bf $tf $Nfw $Nff

    $secTag	unique section tag
    $matTag	tag of uniaxialMaterial assigned to each fiber
    $d	section depth
    $tw	web thickness
    $bf	flange width
    $tf	flange thickness
    $Nfw	number of fibers in the web
    $Nff	number of fibers in each flange
    """
    def __init__(self, id, Mat, d, tw, bf, tf, Nfw, Nff, **kwargs):
        self._id = id
        self._Mat = Mat
        self._d = d
        self._tw = tw
        self._bf = bf
        self._tf = tf
        self._Nfw = Nfw
        self._Nff = Nff
        self.__dict__.update(kwargs)

        self._CommandLine =  'section WFSection2d %d %d %f %f %f %f %f %f'%(self._id, self._Mat.id, self._d, self._tw, self._bf, self._tf, self._Nfw, self._Nff)

class RCSection2d(OpenSees):
    """
    section RCSection2d $secTag $coreTag $coverTag $steelTag $d $b $cover $Atop $Abot $Aside $Nfcore $Nfcover $Nfs
    $secTag	unique section tag
    $coreTag	tag of uniaxialMaterial assigned to each fiber in the core region
    $coverTag	tag of uniaxialMaterial assigned to each fiber in the cover region
    $steelTag	tag of uniaxialMaterial assigned to each reinforcing bar
    $d	section depth
    $b	section width
    $cover	cover depth (assumed uniform around perimeter)
    $Atop	area of reinforcing bars in top layer
    $Abot	area of reinforcing bars in bottom layer
    $Aside	area of reinforcing bars on intermediate layers
    $Nfcore	number of fibers through the core depth
    $Nfcover	number of fibers through the cover depth
    $Nfs	number of bars on the top and bottom rows of reinforcement (Nfs-2 bars will be placed on the side rows)
    """
    def __init__(self, id, coreMat, coverMat, steelMat, d, b, cover, Atop, Abot, Aside ,Nfcore ,Nfcover, Nfs, **kwargs):
        self._id = id
        self._coverMat = coverMat
        self._steelMat = steelMat
        self._coreMat = coreMat
        self._d = d
        self._b = b
        self._cover = cover
        self._Atop = Atop
        self._Abot = Abot
        self._Aside = Aside
        self._Nfcore = Nfcore
        self._Nfcover = Nfcover
        self._Nfs = Nfs
        self.__dict__.update(kwargs)

        self._CommandLine = 'section RCSection2d %d %d %d %f %f %f %f %f %f %d %d %d'%(self._id, self._coreMat.id, self._coverMat.id, self._steelMat.id, self._d, self._b, self._cover, self._Atop, self._Abot, self._Aside, self._Nfcore, self._Nfcover, self._Nfs)

class NDFiber(OpenSees):
    """
    section NDFiber $secTag {
    fiber...
    patch...
    layer...
    ...
    }

    $secTag	unique tag among all sections
    fiber...	command to generate a single fiber.
    patch...	command to generate a number of fibers over a geometric cross-section
    layer...	command to generate a row of fibers along a geometric-arc
    """
    def __init__(self, id, fibers, **kwargs):
        self._id = id
        self._fibers = fibers
        self.__dict__.update(kwargs)

        self._CommandLine =  'section Fiber %d { \n'%(self._id)+''.join(map(lambda x: ' %s\n'%x._CommandLine, self._fibers))+'}'

class Aggregator(OpenSees):
    """
    section Aggregator $secTag $matTag1 $dof1 $matTag2 $dof2 ....... <-section $sectionTag>

    $secTag	unique section tag
    $matTag1 $matTag2 ...	tag of previously-defined UniaxialMaterial objects
    $dof1 $dof2 ...	the force-deformation quantity to be modeled by this section object. One of the following section dof may be used:
    P Axial force-deformation
    Mz Moment-curvature about section local z-axis
    Vy Shear force-deformation along section local y-axis
    My Moment-curvature about section local y-axis
    Vz Shear force-deformation along section local z-axis
    T Torsion Force-Deformation
    $sectionTag	tag of previously-defined Section object to which the UniaxialMaterial objects are aggregated as additional force-deformation relationships
    """
    def __init__(self, id, MatList, DOFList, Section=None, **kwargs):
        self._id = id
        self._MatList = MatList
        self._DOFList = DOFList
        self._Section = Section
        self.__dict__.update(kwargs)

        if self._Section == None:
            self._CommandLine = 'section Aggregator %d %s'%(self._id, ''.join(map(lambda x: ' %d %d'%(x[0].id, x[1]), zip(*[self._MatList, self._DOFList]))))
        else:
            self._CommandLine = 'section Aggregator %d %s -section %d'%(self._id, ''.join(map(lambda x: ' %d %s'%(x[0].id, x[1]), zip(*[self._MatList, self._DOFList]))), self._Section.id)




class Uniaxial(OpenSees):
    """
    section Uniaxial $secTag $matTag $quantity

    $secTag	unique section tag
    $matTag	tag of uniaxial material
    $quantity	the force-deformation quantity to be modeled by this section object. One of the following strings is used:
    P Axial force-deformation
    Mz Moment-curvature about section local z-axis
    Vy Shear force-deformation along section local y-axis
    My Moment-curvature about section local z-axis
    Vz Shear force-deformation along section local z-axis
    T Torsion Force-Deformation
    """
    def __init__(self, id, Mat, quantity):
        self._id = id
        self._Mat = Mat
        self._quantity = quantity

        self._CommandLine = 'section Uniaxial %d %d %s'%(self._id, self._Mat.id, self._quantity)

class ElasticMembranePlateSection(OpenSees):
    """
    section ElasticMembranePlateSection $secTag $E $nu $h $rho

    $secTag	unique section tag
    $E	Young's Modulus
    $nu	Poisson's Ratio
    $h	depth of section
    $rho	mass density
    """
    def __init__(self, id, E, nu, h, rho, **kwargs):
        self._id = id
        self._E = E
        self._nu = nu
        self._h = h
        self._rho = rho
        self.__dict__.update(kwargs)

        self._CommandLine = 'section ElasticMembranePlateSection %d %f %f %f %f'%(self._id, self._E, self._nu, self._h, self._rho)

class PlateFiber(OpenSees):
    """
    section PlateFiber $secTag $matTag $h

    $secTag	unique section tag
    $matTag	nDMaterial tag to be assigned to each fiber
    $h	plate thickness
    """
    def __init__(self, id, Mat, h):
        self._id = id
        self._Mat = Mat
        self._h = h

        self._CommandLine = 'section PlateFiber %d %d %f'%(self._id, self._Mat.id, self._h)

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

