"""
Elastic Isotropic Material
Elastic Orthotropic Material
J2 Plasticity Material
Drucker Prager Material
Concrete Damage Model
Plane Stress Material
Plane Strain Material
Multi Axial Cyclic Plasticity
Bounding Cam Clay
Plate Fiber Material
Plane Stress Concrete Materials
Tsinghua Sand Models
CycLiqCP Material (Cyclic ElasticPlasticity)
CycLiqCPSP Material
Manzari Dafalias Material
Materials for Modeling Concrete Walls
PlaneStressUserMaterial
PlateFromPlaneStress
PlateRebar
LayeredShell
Contact Materials for 2D and 3D
ContactMaterial2D
ContactMaterial3D
Wrapper material for Initial State Analysis
InitialStateAnalysisWrapper
UC San Diego soil models (Linear/Nonlinear, dry/drained/undrained soil response under general 2D/3D static/cyclic loading conditions (please visit UCSD for examples)
PressureIndependMultiYield Material
PressureDependMultiYield Material
PressureDependMultiYield02 Material
UC San Diego Saturated Undrained soil
FluidSolidPorousMaterial
UCDavis Soil Models
"""

__author__ = 'marafi'

from OpenSeesAPI.OpenSees import OpenSees

class ElasticIsotropic(OpenSees):
    """
    nDMaterial ElasticIsotropic $matTag $E $v <$rho>
    $matTag	integer tag identifying material
    $E	elastic Modulus
    $v	Poisson's ratio
    $rho	mass density, optional default = 0.0.
    """
    def __init__(self, id, E, v, rho=None, **kwargs):
        self._id = id
        self._E = E
        self._v = v
        self._rho = rho
        self.__dict__.update(kwargs)

        if self._rho != None:
            self._CommandLine = 'nDMaterial ElasticIsotropic %d %f %f '%(self._id, self._E, self._v)
        else:
            self._CommandLine = 'nDMaterial ElasticIsotropic %d %f %f %f'%(self._id, self._E, self._v, self._rho)

class PlaneStress(OpenSees):
    """
    nDMaterial PlaneStress $matTag $threeDtag
    $matTag	integer tag identifying material
    $otherTag	tag of perviously defined 3d ndMaterial material
    """
    def __init__(self, id, NdMat, **kwargs):
        self._id = id
        self._NdMat = NdMat
        self.__dict__.update(kwargs)

        self._CommandLine = 'nDMaterial PlaneStress %d %d'%(self._id, self._NdMat.id)

class PlaneStrain(OpenSees):
    """
    nDMaterial PlaneStrain $matTag $threeDtag
    $matTag	integer tag identifying material
    $threeDTag	integer tag of previously defined 3d ndMaterial material
    """
    def __init__(self, id, NdMat, **kwargs):
        self._id = id
        self._NdMat = NdMat
        self.__dict__.update(kwargs)

        self._CommandLine = 'nDMaterial PlaneStrain %d %d'%(self._id, self._NdMat.id)

"""
nDmaterial PlaneStressUserMaterial $matTag 40 7 $fc $ft $fcu $epsc0 $epscu $epstu $stc
$matTag
integer tag identifying material
$fc
concrete compressive strength at 28 days (positive)
$ft
concrete tensile strength (positive)
$fcu
concrete crushing strength (negative)
$epsc0
concrete strain at maximum strength (negative)
$epscu
concrete strain at crushing strength (negative)
$epstu
ultimate tensile strain (positive)
$stc
shear retention factor
nDmaterial PlateFromPlaneStress $newmatTag $matTag $OutofPlaneModulus
$newmatTag
new integer tag identifying material deriving from pre-defined PlaneStressUserMaterial
$matTag
integer tag identifying PlaneStressUserMaterial
$OutofPlaneModulus
shear modulus of out plane
2. Multi-dimensional Reinforcement Material
This command is used to create the multi-dimensional reinforcement material.

nDmaterial PlateRebar $newmatTag $matTag $sita
$newmatTag
new integer tag identifying material deriving from pre-defined uniaxial steel material
$matTag
integer tag identifying uniaxial steel material
$sita
define the angle of steel layer, 90 (longitudinal steel), 0 (tranverse steel)
3. Define the Section of the Multi-layer Shell element
This command will create the section of the multi-layer shell element, including the
Multi-dimensional concrete, reinforcement material and the corresponding thickness.
section LayeredShell $sectionTag $nLayers $matTag1 $thickness1...$matTagn $thicknessn
$sectionTag
unique tag among sections
$nLayers
total numbers of layers
$matTag1
material tag of first layer
$thickness1
thickness of first layer

$matTagn
material tag of last layer
$thicknessn
thickness of last layer
"""