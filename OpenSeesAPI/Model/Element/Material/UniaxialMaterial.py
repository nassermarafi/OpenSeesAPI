"""
The following contain information about matType? and the args required for each of the available material types:
Steel & Reinforcing-Steel Materials
Steel01 Material
Steel02 Material -- Giuffr-Menegotto-Pinto Model with Isotropic Strain Hardening
Steel4 Material
Hysteretic Material
Reinforcing Steel Material
Dodd Restrepo
RambergOsgoodSteel Material
Concrete Materials
Concrete01 Material -- Zero Tensile Strength
Concrete02 Material -- Linear Tension Softening
Concrete04 Material -- Popovics Concrete Material
Concrete06 Material
Concrete07
Concrete01 Material With Stuff in the Cracks
ConfinedConcrete01 Material
Some Standard Uniaxial Materials
Elastic Uniaxial Material
Elastic-Perfectly Plastic Material
Elastic-Perfectly Plastic Gap Material
Elastic-No Tension Material
Parallel Material
Series Material
Other Uniaxial Materials
CastFuse Material
ViscousDamper Material
Modified Ibarra-Medina-Krawinkler Deterioration Model with Bilinear Hysteretic Response (Bilin Material)
Modified Ibarra-Medina-Krawinkler Deterioration Model with Peak-Oriented Hysteretic Response (ModIMKPeakOriented Material)
Modified Ibarra-Medina-Krawinkler Deterioration Model with Pinched Hysteretic Response (ModIMKPinching Material)
SAWS Material
BARSLIP Material
Bond_SP01 - - Strain Penetration Model for Fully Anchored Steel Reinforcing Bars
Fatigue Material
Hardening Material
Impact Material
Hyperbolic Gap Material
Limit State Material
MinMax Material
ElasticBilin Material
ElasticMultiLinear Material
MultiLinear Material
Initial Strain Material
Initial Stress Material
PathIndependent Material
Pinching4 Material
Engineered Cementitious Composites Material
SelfCentering Material
Viscous Material
BoucWen Material
BWBN Material (Pinching Hysteretic Bouc-Wen Material)
PyTzQz uniaxial materials for p-y, t-z and q-z elements for modeling soil-structure interaction through the piles in a structural foundation
PySimple1 Material
TzSimple1 Material
QzSimple1 Material
PyLiq1 Material
TzLiq1 Material
PySimple1Gen Command
TzSimple1Gen Command
KikuchiAikenHDR Material
KikuchiAikenLRB Material
AxialSp Material
AxialSpHD Material
Pinching Limit State Material
CFSWSWP Wood Sheathed cold-formed Steel Shear Wall Panel
CFSSSWP Steel Sheathed cold-formed Steel Shear Wall Panel
"""

__author__ = 'Nasser'

from OpenSeesAPI.OpenSees import OpenSees

class Elastic(OpenSees):
    """
    uniaxialMaterial Elastic $matTag $E <$eta> <$Eneg>
    $matTag	integer tag identifying material
    $E	tangent
    $eta	damping tangent (optional, default=0.0)
    $Eneg	tangent in compression (optional, default=E)
    """
    def __init__(self, id, E, **kwargs):
        self._id = id
        self._E = E
        self.__dict__.update(kwargs)

        self._CommandLine =  'uniaxialMaterial Elastic %d %f'%(self.id, self._E)

class ElasticPP(OpenSees):
    """
    uniaxialMaterial ElasticPP $matTag $E $epsyP <$epsyN $eps0>
    $matTag	integer tag identifying material
    $E	tangent
    $epsyP	strain or deformation at which material reaches plastic state in tension
    $epsyN	strain or deformation at which material reaches plastic state in compression.
    (optional, default is tension value)
    $eps0	initial strain (optional, default: zero)
    """
    def __init__(self, id, E, EpsilonPositive, EpsilonNegative=None, Epsilon0=None, **kwargs):
        self._id = id
        self._E = E
        self._EpsilonPositive = EpsilonPositive
        self._EpsilonNegative = EpsilonNegative
        self._Epsilon0 = Epsilon0
        self.__dict__.update(kwargs)

        self._Optional = ''
        if self._EpsilonNegative!=None:
            self._Optional += ' %f'%self._EpsilonNegative
        if self._Epsilon0!=None:
            self._Optional += ' %f'%self.Epsilon0

        self._CommandLine =  'uniaxialMaterial ElasticPP %d %f %f %s'%(self.id, self._E, self._EpsilonPositive, self._Optional)

class Hardening(OpenSees):
    """
    uniaxialMaterial Hysteretic $matTag $s1p $e1p $s2p $e2p <$s3p $e3p> $s1n $e1n $s2n $e2n <$s3n $e3n> $pinchX $pinchY $damage1 $damage2 <$beta>
    $matTag	integer tag identifying material
    $s1p $e1p	stress and strain (or force & deformation) at first point of the envelope in the positive direction
    $s2p $e2p	stress and strain (or force & deformation) at second point of the envelope in the positive direction
    $s3p $e3p	stress and strain (or force & deformation) at third point of the envelope in the positive direction (optional)
    $s1n $e1n	stress and strain (or force & deformation) at first point of the envelope in the negative direction
    $s2n $e2n	stress and strain (or force & deformation) at second point of the envelope in the negative direction
    $s3n $e3n	stress and strain (or force & deformation) at third point of the envelope in the negative direction (optional)
    $pinchx	pinching factor for strain (or deformation) during reloading
    $pinchy	pinching factor for stress (or force) during reloading
    $damage1	damage due to ductility: D1(mu-1)
    $damage2	damage due to energy: D2(Eii/Eult)
    $beta	power used to determine the degraded unloading stiffness based on ductility, mu-beta (optional, default=0.0)
    """
    def __init__(self, id, E, SigmaY, H_iso, H_kin, ETA=0.0, **kwargs):
        self._id = id
        self._E = E
        self._SigmaY = SigmaY
        self._H_iso = H_iso
        self._H_kin = H_kin
        self._ETA = ETA
        self.__dict__.update(kwargs)

        self._CommandLine =  'uniaxialMaterial Hardening %d %f %f %f %f %f'%(self.id, self._E, self._SigmaY, self._H_iso, self._H_kin, self._ETA)

class Steel01(OpenSees):
    """
    This command is used to construct a uniaxial bilinear steel material object with kinematic hardening and optional isotropic hardening described by a non-linear evolution equation (REF: Fedeas).
    uniaxialMaterial Steel01 $matTag $Fy $E0 $b <$a1 $a2 $a3 $a4>
    $matTag	integer tag identifying material
    $Fy	yield strength
    $E0	initial elastic tangent
    $b	strain-hardening ratio (ratio between post-yield tangent and initial elastic tangent)
    $a1	isotropic hardening parameter, increase of compression yield envelope as proportion of yield strength after a plastic strain of $a2*($Fy/E0). (optional)
    $a2	isotropic hardening parameter (see explanation under $a1). (optional).
    $a3	isotropic hardening parameter, increase of tension yield envelope as proportion of yield strength after a plastic strain of $a4*($Fy/E0). (optional)
    $a4	isotropic hardening parameter (see explanation under $a3). (optional)
    """
    def __init__(self, id, Fy, E, b, a1=None, a2=None, a3=None, a4=None, **kwargs):
        self._id = id
        self._Fy = Fy
        self._E = E
        self._b = b
        self._a1 = a1
        self._a2 = a2
        self._a3 = a3
        self._a4 = a4

        self.__dict__.update(kwargs)

        if self._a1 == None:
            self._CommandLine = 'uniaxialMaterial Steel01 %d %f %f %f '%(self._id, self._Fy, self._E, self._b)
        else:
            self._CommandLine = 'uniaxialMaterial Steel01 %d %f %f %f %f %f %f %f'%(self._id, self._Fy, self._E, self._b, self._a1, self._a2, self._a3, self._a4)

class Bilin(OpenSees):
    """
    uniaxialMaterial Bilin $matTag $K0 $as_Plus $as_Neg $My_Plus $My_Neg $Lamda_S $Lamda_C $Lamda_A $Lamda_K $c_S $c_C $c_A $c_K $theta_p_Plus $theta_p_Neg $theta_pc_Plus $theta_pc_Neg $Res_Pos $Res_Neg $theta_u_Plus $theta_u_Neg $D_Plus $D_Neg <$nFactor>
    $matTag	integer tag identifying material
    $K0	elastic stiffness
    $as_Plus	strain hardening ratio for positive loading direction
    $as_Neg	strain hardening ratio for negative loading direction
    $My_Plus	effective yield strength for positive loading direction
    $My_Neg	effective yield strength for negative loading direction (negative value)
    $Lamda_S	Cyclic deterioration parameter for strength deterioration
    $Lamda_C	Cyclic deterioration parameter for post-capping strength deterioration
    $Lamda_A	Cyclic deterioration parameter for acceleration reloading stiffness deterioration (is not a deterioration mode for a component with Bilinear hysteretic response).
    $Lamda_K	Cyclic deterioration parameter for unloading stiffness deterioration
    $c_S	rate of strength deterioration. The default value is 1.0.
    $c_C	rate of post-capping strength deterioration. The default value is 1.0.
    $c_A	rate of accelerated reloading deterioration. The default value is 1.0.
    $c_K	rate of unloading stiffness deterioration. The default value is 1.0.
    $theta_p_Plus	pre-capping rotation for positive loading direction (often noted as plastic rotation capacity)
    $theta_p_Neg	pre-capping rotation for negative loading direction (often noted as plastic rotation capacity) (positive value)
    $theta_pc_Plus	post-capping rotation for positive loading direction
    $theta_pc_Neg	post-capping rotation for negative loading direction (positive value)
    $Res_Pos	residual strength ratio for positive loading direction
    $Res_Neg	residual strength ratio for negative loading direction (positive value)
    $theta_u_Plus	ultimate rotation capacity for positive loading direction
    $theta_u_Neg	ultimate rotation capacity for negative loading direction (positive value)
    $D_Plus	rate of cyclic deterioration in the positive loading direction (this parameter is used to create assymetric hysteretic behavior for the case of a composite beam). For symmetric hysteretic response use 1.0.
    $D_Neg	rate of cyclic deterioration in the negative loading direction (this parameter is used to create assymetric hysteretic behavior for the case of a composite beam). For symmetric hysteretic response use 1.0.
    $nFactor	elastic stiffness amplification factor, mainly for use with concentrated plastic hinge elements (optional, default = 0).
    """
    def __init__(self, id, E, asPlus, asNeg, MyPlus, MyNeg, LamdaS, LamdaC, LamdaA, LamdaK, cS, cC, cA, cK, thetaPPlus, thetaPNeg, thetaPcPlus, thetaPcNeg, ResPos, ResNeg, thetaUPlus, thetaUNeg, DPlus, DNeg, nFactor=None, **kwargs):
        self._id = id
        self._E = E
        self._asPlus = asPlus
        self._asNeg = asNeg
        self._MyPlus = MyPlus
        self._MyNeg = MyNeg
        self._LamdaS = LamdaS
        self._LambaC = LamdaC
        self._LamdaA = LamdaA
        self._LamdaK = LamdaK
        self._cS = cS
        self._cC = cC
        self._cA = cA
        self._cK = cK
        self._thetaPPlus = thetaPPlus
        self._thetaPNeg = thetaPNeg
        self._thetaPcPlus = thetaPcPlus
        self._thetaPcNeg = thetaPcNeg
        self._ResPos = ResPos
        self._ResNeg = ResNeg
        self._thetaUPlus = thetaUPlus
        self._thetaUNeg = thetaUNeg
        self._DPlus = DPlus
        self._DNeg = DNeg
        self._nFactor = nFactor
        self._EndCommand = ''
        self.__dict__.update(kwargs)

        if self._nFactor != None:
            self._EndCommand = ' %f'%self._nFactor
        self._CommandLine = 'uniaxialMaterial Bilin %d %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %s'%(self._id, self._E, self._asPlus, self._asNeg, self._MyPlus, self._MyNeg, self._LamdaS, self._LambaC, self._LamdaA, self._LamdaK, self._cS, self._cC, self._cA, self._cK, self._thetaPPlus, self._thetaPNeg, self._thetaPcPlus, self._thetaPcNeg, self._ResPos, self._ResNeg, self._thetaUPlus, self._thetaUNeg, self._DPlus, self._DNeg, self._EndCommand)

class ModIMKPeakOriented(OpenSees):
    """
    uniaxialMaterial ModIMKPeakOriented $matTag $K0 $as_Plus $as_Neg $My_Plus $My_Neg $Lamda_S $Lamda_C $Lamda_A $Lamda_K $c_S $c_C $c_A $c_K $theta_p_Plus $theta_p_Neg $theta_pc_Plus $theta_pc_Neg $Res_Pos $Res_Neg $theta_u_Plus $theta_u_Neg $D_Plus $D_Neg
    $matTag	integer tag identifying material
    $K0	elastic stiffness
    $as_Plus	strain hardening ratio for positive loading direction
    $as_Neg	strain hardening ratio for negative loading direction
    $My_Plus	effective yield strength for positive loading direction
    $My_Neg	effective yield strength for negative loading direction (negative value)
    $Lamda_S	Cyclic deterioration parameter for strength deterioration [see definitions in Lignos and Krawinkler (2011)]
    $Lamda_C	Cyclic deterioration parameter for post-capping strength deterioration [see definitions in Lignos and Krawinkler (2011)]
    $Lamda_A	Cyclic deterioration parameter for acceleration reloading stiffness deterioration [see definitions in Lignos and Krawinkler (2011)]
    $Lamda_K	Cyclic deterioration parameter for unloading stiffness deterioration [see definitions in Lignos and Krawinkler (2011)]
    $c_S	rate of strength deterioration. The default value is 1.0.
    $c_C	rate of post-capping strength deterioration. The default value is 1.0.
    $c_A	rate of accelerated reloading deterioration. The default value is 1.0.
    $c_K	rate of unloading stiffness deterioration. The default value is 1.0.
    $theta_p_Plus	pre-capping rotation for positive loading direction (often noted as plastic rotation capacity)
    $theta_p_Neg	pre-capping rotation for negative loading direction (often noted as plastic rotation capacity) (must be defined as a positive value)
    $theta_pc_Plus	post-capping rotation for positive loading direction
    $theta_pc_Neg	post-capping rotation for negative loading direction (must be defined as a positive value)
    $Res_Pos	residual strength ratio for positive loading direction
    $Res_Neg	residual strength ratio for negative loading direction (must be defined as a positive value)
    $theta_u_Plus	ultimate rotation capacity for positive loading direction
    $theta_u_Neg	ultimate rotation capacity for negative loading direction (must be defined as a positive value)
    $D_Plus	rate of cyclic deterioration in the positive loading direction (this parameter is used to create assymetric hysteretic behavior for the case of a composite beam). For symmetric hysteretic response use 1.0.
    $D_Neg	rate of cyclic deterioration in the negative loading direction (this parameter is used to create assymetric hysteretic behavior for the case of a composite beam). For symmetric hysteretic response use 1.0.
    """
    def __init__(self, id, E, asPlus, asNeg, MyPlus, MyNeg, LamdaS, LamdaC, LamdaA, LamdaK, cS, cC, cA, cK, thetaPPlus, thetaPNeg, thetaPcPlus, thetaPcNeg, ResPos, ResNeg, thetaUPlus, thetaUNeg, DPlus, DNeg, nFactor=None, **kwargs):
        self._id = id
        self._E = E
        self._asPlus = asPlus
        self._asNeg = asNeg
        self._MyPlus = MyPlus
        self._MyNeg = MyNeg
        self._LamdaS = LamdaS
        self._LambaC = LamdaC
        self._LamdaA = LamdaA
        self._LamdaK = LamdaK
        self._cS = cS
        self._cC = cC
        self._cA = cA
        self._cK = cK
        self._thetaPPlus = thetaPPlus
        self._thetaPNeg = thetaPNeg
        self._thetaPcPlus = thetaPcPlus
        self._thetaPcNeg = thetaPcNeg
        self._ResPos = ResPos
        self._ResNeg = ResNeg
        self._thetaUPlus = thetaUPlus
        self._thetaUNeg = thetaUNeg
        self._DPlus = DPlus
        self._DNeg = DNeg
        self.__dict__.update(kwargs)

        self._CommandLine = 'uniaxialMaterial ModIMKPeakOriented %d %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f'%(self._id, self._E, self._asPlus, self._asNeg, self._MyPlus, self._MyNeg, self._LamdaS, self._LambaC, self._LamdaA, self._LamdaK, self._cS, self._cC, self._cA, self._cK, self._thetaPPlus, self._thetaPNeg, self._thetaPcPlus, self._thetaPcNeg, self._ResPos, self._ResNeg, self._thetaUPlus, self._thetaUNeg, self._DPlus, self._DNeg)

class ModIMKPinched(OpenSees):
    """
    uniaxialMaterial ModIMKPinching $matTag $K0 $as_Plus $as_Neg $My_Plus $My_Neg $FprPos $FprNeg $A_pinch $Lamda_S $Lamda_C $Lamda_A $Lamda_K $c_S $c_C $c_A $c_K $theta_p_Plus $theta_p_Neg $theta_pc_Plus $theta_pc_Neg $Res_Pos $Res_Neg $theta_u_Plus $theta_u_Neg $D_Plus $D_Neg
    $matTag	integer tag identifying material
    $K0	elastic stiffness
    $as_Plus	strain hardening ratio for positive loading direction
    $as_Neg	strain hardening ratio for negative loading direction
    $My_Plus	effective yield strength for positive loading direction
    $My_Neg	effective yield strength for negative loading direction (Must be defined as a negative value)
    $FprPos	Ratio of the force at which reloading begins to force corresponding to the maximum historic deformation demand (positive loading direction)
    $FprNeg	Ratio of the force at which reloading begins to force corresponding to the absolute maximum historic deformation demand (negative loading direction)
    $A_Pinch	Ratio of reloading stiffness
    $Lamda_S	Cyclic deterioration parameter for strength deterioration [see definitions in Lignos and Krawinkler (2011)]
    $Lamda_C	Cyclic deterioration parameter for post-capping strength deterioration [see definitions in Lignos and Krawinkler (2011)]
    $Lamda_A	Cyclic deterioration parameter for acceleration reloading stiffness deterioration [see definitions in Lignos and Krawinkler (2011)]
    $Lamda_K	Cyclic deterioration parameter for unloading stiffness deterioration [see definitions in Lignos and Krawinkler (2011)]
    $c_S	rate of strength deterioration. The default value is 1.0.
    $c_C	rate of post-capping strength deterioration. The default value is 1.0.
    $c_A	rate of accelerated reloading deterioration. The default value is 1.0.
    $c_K	rate of unloading stiffness deterioration. The default value is 1.0.
    $theta_p_Plus	pre-capping rotation for positive loading direction (often noted as plastic rotation capacity)
    $theta_p_Neg	pre-capping rotation for negative loading direction (often noted as plastic rotation capacity) (must be defined as a positive value)
    $theta_pc_Plus	post-capping rotation for positive loading direction
    $theta_pc_Neg	post-capping rotation for negative loading direction (must be defined as a positive value)
    $Res_Pos	residual strength ratio for positive loading direction
    $Res_Neg	residual strength ratio for negative loading direction (must be defined as a positive value)
    $theta_u_Plus	ultimate rotation capacity for positive loading direction
    $theta_u_Neg	ultimate rotation capacity for negative loading direction (must be defined as a positive value)
    $D_Plus	rate of cyclic deterioration in the positive loading direction (this parameter is used to create assymetric hysteretic behavior for the case of a composite beam). For symmetric hysteretic response use 1.0.
    $D_Neg	rate of cyclic deterioration in the negative loading direction (this parameter is used to create assymetric hysteretic behavior for the case of a composite beam). For symmetric hysteretic response use 1.0.
    """
    def __init__(self, id, E, asPlus, asNeg, MyPlus, MyNeg, FprPos, FprNeg, APinch, LamdaS, LamdaC, LamdaA, LamdaK, cS, cC, cA, cK, thetaPPlus, thetaPNeg, thetaPcPlus, thetaPcNeg, ResPos, ResNeg, thetaUPlus, thetaUNeg, DPlus, DNeg, nFactor=None, **kwargs):
        self._id = id
        self._E = E
        self._asPlus = asPlus
        self._asNeg = asNeg
        self._MyPlus = MyPlus
        self._MyNeg = MyNeg
        self._FprPos = FprPos
        self._FprNeg = FprNeg
        self._APinch = APinch
        self._LamdaS = LamdaS
        self._LambaC = LamdaC
        self._LamdaA = LamdaA
        self._LamdaK = LamdaK
        self._cS = cS
        self._cC = cC
        self._cA = cA
        self._cK = cK
        self._thetaPPlus = thetaPPlus
        self._thetaPNeg = thetaPNeg
        self._thetaPcPlus = thetaPcPlus
        self._thetaPcNeg = thetaPcNeg
        self._ResPos = ResPos
        self._ResNeg = ResNeg
        self._thetaUPlus = thetaUPlus
        self._thetaUNeg = thetaUNeg
        self._DPlus = DPlus
        self._DNeg = DNeg
        self.__dict__.update(kwargs)

        self._CommandLine = 'uniaxialMaterial ModIMKPinching %d %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f'%(self._id, self._E, self._asPlus, self._asNeg, self._MyPlus, self._MyNeg, self._FprPos, self._APinch, self._FprNeg, self._LamdaS, self._LambaC, self._LamdaA, self._LamdaK, self._cS, self._cC, self._cA, self._cK, self._thetaPPlus, self._thetaPNeg, self._thetaPcPlus, self._thetaPcNeg, self._ResPos, self._ResNeg, self._thetaUPlus, self._thetaUNeg, self._DPlus, self._DNeg)

class Clough(OpenSees):
    """
    uniaxialMaterial Clough  $matTag $elstk $myPos $myNeg $alphaHardScaled $resStrRatio $alphaCapScaled	$thetaCapPos $thetaCapNeg $lambdaS $lambdaK $lambdaA $lambdaD  $c $c $c $c
    """
    def __init__(self, id, Ke, My, MyNeg, AlphaYield, Residual, AlphaPC, ThetaCappingPos, ThetaCappingNeg, LambdaS, LambdaK, LambdaA, LambdaD, cS, cK, cA, cD, **kwargs):
        self._id = id
        self._Ke = Ke
        self._My = My
        self._MyNeg = MyNeg
        self._AlphaYield = AlphaYield
        self._Residual = Residual
        self._AlphaPC = AlphaPC
        self._ThetaCappingPos = ThetaCappingPos
        self._ThetaCappingNeg = ThetaCappingNeg
        self._LambdaS = LambdaS
        self._LambdaK = LambdaK
        self._LambdaA = LambdaA
        self._LambdaD = LambdaD
        self._cS = cS
        self._cK = cK
        self._cA = cA
        self._cD = cD
        self.__dict__.update(kwargs)

        self.RunCommandLine()

    def RunCommandLine(self):
        self._CommandLine = 'uniaxialMaterial Clough %d %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f'%(self._id, self._Ke, self._My, self._MyNeg, self._AlphaYield, self._Residual, self._AlphaPC, self._ThetaCappingPos, self._ThetaCappingNeg, self._LambdaS, self._LambdaK, self._LambdaA, self._LambdaD, self._cS, self._cK, self._cA, self._cD)

class Hysteretic(OpenSees):
    """
    This command is used to construct a uniaxial bilinear hysteretic material object with pinching of force and deformation, damage due to ductility and energy, and degraded unloading stiffness based on ductility.
    uniaxialMaterial Hysteretic $matTag $s1p $e1p $s2p $e2p <$s3p $e3p> $s1n $e1n $s2n $e2n <$s3n $e3n> $pinchX $pinchY $damage1 $damage2 <$beta>
    $matTag	integer tag identifying material
    $s1p $e1p	stress and strain (or force & deformation) at first point of the envelope in the positive direction
    $s2p $e2p	stress and strain (or force & deformation) at second point of the envelope in the positive direction
    $s3p $e3p	stress and strain (or force & deformation) at third point of the envelope in the positive direction (optional)
    $s1n $e1n	stress and strain (or force & deformation) at first point of the envelope in the negative direction
    $s2n $e2n	stress and strain (or force & deformation) at second point of the envelope in the negative direction
    $s3n $e3n	stress and strain (or force & deformation) at third point of the envelope in the negative direction (optional)
    $pinchx	pinching factor for strain (or deformation) during reloading
    $pinchy	pinching factor for stress (or force) during reloading
    $damage1	damage due to ductility: D1(mu-1)
    $damage2	damage due to energy: D2(Eii/Eult)
    $beta	power used to determine the degraded unloading stiffness based on ductility, mu-beta (optional, default=0.0)
    """
    def __init__(self, id, s1p,e1p,s2p,e2p,s1n,e1n,s2n,e2n,pinchx,pinchy,damage1,damage2,s3p=None,e3p=None,s3n=None,e3n=None,beta=None,**kwargs):
        self._id = id
        self._s1p = s1p
        self._e1p = e1p
        self._s2p = s2p
        self._e2p = e2p
        self._s1n = s1n
        self._e1n = e1n
        self._s2n = s2n
        self._e2n = e2n
        self._pinchx = pinchx
        self._pinchy = pinchy
        self._damage1 = damage1
        self._damage2 = damage2
        self._beta = beta
        self._s3p = s3p
        self._e3p = e3p
        self._s3n = s3n
        self._e3n = e3n

        self.__dict__.update(kwargs)
        if beta==None:
            self._Optional = ''
        else:
            self._Optional = ' %f'%self._beta

        if self._s3p==None:
            self._CommandLine = 'uniaxialMaterial Hysteretic %d %f %f %f %f %f %f %f %f %f %f %f %f %s'%(self._id, self._s1p, self._e1p, self._s2p, self._e2p, self._s1n, self._e1n, self._s2n, self._e2n, self._pinchx, self._pinchy, self._damage1, self._damage2, self._Optional)
        else:
            self._CommandLine = 'uniaxialMaterial Hysteretic %d %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %s'%(self._id, self._s1p, self._e1p, self._s2p, self._e2p, self._s3p, self._e3p, self._s1n, self._e1n, self._s2n, self._e2n, self._s3n, self._e3n, self._pinchx, self._pinchy, self._damage1, self._damage2, self._Optional)

class MinMax(OpenSees):
    """
    This command is used to construct a MinMax material object. This stress-strain behaviour for this material is provided by another material. If however the strain ever falls below or above certain threshold values, the other material is assumed to have failed. From that point on, values of 0.0 are returned for the tangent and stress.
    uniaxialMaterial MinMax $matTag $otherTag <-min $minStrain> <-max $maxStrain>

    $matTag	integer tag identifying material
    $otherTag	tag of the other material
    $minStrain	minimum value of strain. optional default = -1.0e16.
    $maxStrain	max value of strain. optional default = 1.0e16.
    """
    def __init__(self, id, OtherMaterial, minStrain, maxStrain, **kwargs):
        self._id = id
        self._OtherMaterial = OtherMaterial
        self._minStrain = minStrain
        self._maxStrain = maxStrain
        self.__dict__.update(kwargs)

        self._CommandLine =  'uniaxialMaterial MinMax %d %d -min %f -max %f'%(self._id, self._OtherMaterial.id, self._minStrain, self._maxStrain)

class Concrete01(OpenSees):
    """
    This command is used to construct a uniaxial Kent-Scott-Park concrete material object with degraded linear unloading/reloading stiffness according to the work of Karsan-Jirsa and no tensile strength. (REF: Fedeas).
    uniaxialMaterial Concrete01 $matTag $fpc $epsc0 $fpcu $epsU
    $matTag	integer tag identifying material
    $fpc	concrete compressive strength at 28 days (compression is negative)*
    $epsc0	concrete strain at maximum strength*
    $fpcu	concrete crushing strength *
    $epsU	concrete strain at crushing strength*
    NOTE:
    Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).
    The initial slope for this model is (2*$fpc/$epsc0)
    """
    def __init__(self, id, fpc, epsc0, fpcu, epsU, **kwargs):
        self._id = id
        self._fpc = fpc
        self._epsc0 = epsc0
        self._fpcu = fpcu
        self._epsU = epsU

        self.__dict__.update(kwargs)

        self._CommandLine =  'uniaxialMaterial Concrete01 %d %f %f %f %f'%(self._id, self._fpc, self._epsc0, self._fpcu, self._epsU)

class Steel02(OpenSees):
    """
    This command is used to construct a uniaxial Giuffre-Menegotto-Pinto steel material object with isotropic strain hardening.
    uniaxialMaterial Steel02 $matTag $Fy $E $b $R0 $cR1 $cR2 <$a1 $a2 $a3 $a4 $sigInit>
    $matTag	integer tag identifying material
    $Fy	yield strength
    $E0	initial elastic tangent
    $b	strain-hardening ratio (ratio between post-yield tangent and initial elastic tangent)
    $R0 $CR1 $CR2	parameters to control the transition from elastic to plastic branches.
    Recommended values: $R0=between 10 and 20, $cR1=0.925, $cR2=0.15
    $a1	isotropic hardening parameter, increase of compression yield envelope as proportion of yield strength after a plastic strain of $a2*($Fy/E0). (optional)
    $a2	isotropic hardening parameter (see explanation under $a1). (optional default = 1.0).
    $a3	isotropic hardening parameter, increase of tension yield envelope as proportion of yield strength after a plastic strain of $a4*($Fy/E0). (optional default = 0.0)
    $a4	isotropic hardening parameter (see explanation under $a3). (optional default = 1.0)
    $sigInit	Initial Stress Value (optional, default: 0.0) the strain is calculated from epsP=$sigInit/$E
    if (sigInit!= 0.0) { double epsInit = sigInit/E; eps = trialStrain+epsInit; } else eps = trialStrain;
    """
    def __init__(self, id, Fy, E0, b, R0=15, CR1=0.925, CR2=0.15, a1=None,a2=None,a3=None,a4=None,sigInit=None, **kwargs):
        self._id = id
        self._Fy = Fy
        self._E0 = E0
        self._b = b
        self._R0 = R0
        self._CR1 = CR1
        self._CR2 = CR2
        self._a1 = a1
        self._a2 = a2
        self._a3 = a3
        self._a4 = a4
        self._sigInit = sigInit

        self.__dict__.update(kwargs)

        if self._a1 == None:
            self._CommandLine =  'uniaxialMaterial Steel02 %d %f %f %f %f %f %f'%(self._id, self._Fy, self._E0, self._b, self._R0, self._CR1, self._CR2)
        else:
            self._CommandLine =  'uniaxialMaterial Steel02 %d %f %f %f %f %f %f %f %f %f %f %f'%(self._id, self._Fy, self._E0, self._b, self._R0, self._CR1, self._CR2, self._a1, self._a2, self._a3, self._a4, self._sigInit)

class Concrete04(OpenSees):
    """
    This command is used to construct a uniaxial Popovics concrete material object with degraded linear unloading/reloading stiffness according to the work of Karsan-Jirsa and tensile strength with exponential decay.
    uniaxialMaterial Concrete04 $matTag $fc $ec $ecu $Ec <$fct $et> <$beta>
    $matTag	integer tag identifying material
    $fc	floating point values defining concrete compressive strength at 28 days (compression is negative)*
    $ec	floating point values defining concrete strain at maximum strength*
    $ecu	floating point values defining concrete strain at crushing strength*
    $Ec	floating point values defining initial stiffness**
    $fct	floating point value defining the maximum tensile strength of concrete
    $et	floating point value defining ultimate tensile strain of concrete
    $beta	loating point value defining the exponential curve parameter to define the residual stress (as a factor of $ft) at $etu
    NOTE:
    Compressive concrete parameters should be input as negative values.
    The envelope of the compressive stress-strain response is defined using the model proposed by Popovics (1973). If the user defines Ec = 57000*sqrt(|fcc|)(in psi)' then the envelope curve is identical to proposed by Mander et al. (1988).
    Model Characteristic: For loading in compression, the envelope to the stress-strain curve follows the model proposed by Popovics (1973) until the concrete crushing strength is achieved and also for strains beyond that corresponding to the crushing strength. For unloading and reloading in compression, the Karsan-Jirsa model (1969) is used to determine the slope of the curve. For tensile loading, an exponential curve is used to define the envelope to the stress-strain curve. For unloading and reloading in tensile, the secant stiffness is used to define the path.
    """
    def __init__(self, id, fc, ec, ecu, Ec, fct=None, et=None, beta=None, **kwargs):
        self._id = id
        self._fc = fc
        self._ec = ec
        self._ecu = ecu
        self._Ec = Ec
        self._fct = fct
        self._et = et
        self._beta = beta

        self.__dict__.update(kwargs)

        self._Optional = ''

        if self._fct != None:
            self._Optional += ' %f %f'%(self._fct,self._et)
        if self._beta != None:
            self._Optional += ' %f'%self._beta

        self._CommandLine =  'uniaxialMaterial Concrete04 %d %f %f %f %f %s'%(self._id, self._fc, self._ec, self._ecu, self._Ec, self._Optional)

class ReinforcingSteel():
    """
    uniaxialMaterial ReinforcingSteel $matTag $fy $fu $Es $Esh $esh $eult < -GABuck $lsr $beta $r $gama > < -DMBuck $lsr < $alpha >> < -CMFatigue $Cf $alpha $Cd > < -IsoHard <$a1 <$limit> > >
    $matTag	unique material object integer tag
    $fy	Yield stress in tension (see Figure 1)
    $fu	Ultimate stress in tension
    $Es	Initial elastic tangent
    $Esh	Tangent at initial strain hardening
    $esh	Strain corresponding to initial strain hardening
    $eult	Strain at peak stress
    -GABuck	Buckling Model Based on Gomes and Appleton (1997)
    $lsr	Slenderness Ratio (see Figure 2)
    $beta	Amplification factor for the buckled stress strain curve. (see Figure 3)
    $r	Buckling reduction factor
    r can be a real number between [0.0 and 1.0]
    r=1.0 full reduction (no buckling)
    r=0.0 no reduction
    0.0<r<1.0 linear interpolation between buckled and unbuckled curves
    $gamma	Buckling constant (see Figures 3 and 4)
    -DMBuck	Buckling model based on Dhakal and Maekawa (2002)
    $lsr	Slenderness Ratio (see Figure 2)
    $alpha	Adjustment Constant usually between 0.75 and 1.0
    Default: alpha=1.0, this parameter is optional.

    -CMFatigue	Coffin-Manson Fatigue and Strength Reduction
    $Cf	Coffin-Manson constant C (see Figure 5)
    $alpha	Coffin-Manson constant a (see Figure 5)
    $Cd	Cyclic strength reduction constant (see Figure 6 and Equation 3)


    -IsoHard	Isotropic Hardening / Diminishing Yield Plateau
    $a1	Hardening constant (default = 4.3)
    $limit	Limit for the reduction of the yield plateau. % of original plateau length to remain (0.01 < limit < 1.0 )
    Limit =1.0, then no reduction takes place (default =0.01)

    -MPCurveParams	Menegotto and Pinto Curve Parameters see Fig 6b
    $R1	(default = 0.333)
    $R2	(default = 18)
    $R3	(default = 4)
    """
    class GABuck(OpenSees):
        #This command is used to construct a ReinforcingSteel uniaxial material object. This object is intended to be used in a reinforced concrete fiber section as the steel reinforcing material.
        def __init__(self, id, fy, fu, Es, Esh, esh, eult, Isr, beta, r, gamma, Cf, alpha,Cd, **kwargs):
            self._id = id
            self._fy = fy
            self._fu = fu
            self._Es = Es
            self._Esh = Esh
            self._esh = esh
            self._eult = eult
            self._Isr = Isr
            self._beta = beta
            self._r = r
            self._gamma = gamma
            self._Cf = Cf
            self._alpha = alpha
            self._Cd = Cd

            self._CommandLine = 'uniaxialMaterial ReinforcingSteel %d %f %f %f %f %f %f -GABuck %f %f %f %f -CMFatigue %f %f %f'%(self._id, self._fy, self._fu, self._Es, self._Esh, self._esh, self._eult, self._Isr, self._beta, self._r, self._gamma, self._Cf, self._alpha, self._Cd)

    class DMBuck(OpenSees):
        #This command is used to construct a ReinforcingSteel uniaxial material object. This object is intended to be used in a reinforced concrete fiber section as the steel reinforcing material.
        def __init__(self, id, fy, fu, Es, Esh, esh, eult, Isr, beta, r, gamma, Cf, alpha,Cd, **kwargs):
            self._id = id
            self._fy = fy
            self._fu = fu
            self._Es = Es
            self._Esh = Esh
            self._esh = esh
            self._eult = eult
            self._Isr = Isr
            self._alpha = alpha

            self._CommandLine = 'uniaxialMaterial ReinforcingSteel %d %f %f %f %f %f %f -DMBuck %f %f'%(self._id, self._fy, self._fu, self._Es, self._Esh, self._esh, self._eult, self._Isr, self._alpha)

class Concrete02(OpenSees):
    """
    uniaxialMaterial Concrete02 $matTag $fpc $epsc0 $fpcu $epsU $lambda $ft $Ets
    $matTag	integer tag identifying material
    $fpc	concrete compressive strength at 28 days (compression is negative)*
    $epsc0	concrete strain at maximum strength*
    $fpcu	concrete crushing strength *
    $epsU	concrete strain at crushing strength*
    $lambda	ratio between unloading slope at $epscu and initial slope
    $ft	tensile strength
    $Ets	tension softening stiffness (absolute value) (slope of the linear tension softening branch)

    NOTE:
    Compressive concrete parameters should be input as negative values.
    The initial slope for this model is (2*$fpc/$epsc0)
    """

    def __init__(self, id, fc, ec, fpcu, ecu, lam, ft, Ets, **kwargs):
        self._id = id
        self._fc = fc
        self._ec = ec
        self._fpcu = fpcu
        self._ecu = ecu
        self._lam = lam
        self._ft = ft
        self._Ec = Ets

        self.__dict__.update(kwargs)

        self._CommandLine =  'uniaxialMaterial Concrete02 %d %f %f %f %f %f %f %f'%(self._id, self._fc, self._ec, self._fpcu, self._ecu, self._lam, self._ft, self._Ec)

