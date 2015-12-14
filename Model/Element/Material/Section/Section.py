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
        self._DOFList = DOFList #DOF in terms of P, Mz, Vy, My, Vx, and T
        self._Section = Section
        self.__dict__.update(kwargs)

    @property
    def CommandLine(self):
        if self._Section == None:
            self._CommandLine = 'section Aggregator %d %s'%(self._id, ''.join(map(lambda x: ' %d %s'%(x[0].id, x[1]), zip(*[self._MatList, self._DOFList]))))
        else:
            self._CommandLine = 'section Aggregator %d %s -section %d'%(self._id, ''.join(map(lambda x: ' %d %s'%(x[0].id, x[1]), zip(*[self._MatList, self._DOFList]))), self._Section.id)
        return self._CommandLine

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
