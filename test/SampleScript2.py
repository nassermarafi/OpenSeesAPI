__author__ = 'marafi'
import os
import numpy as np

########################## Input Parameters ##########################

# This is Elcentro's Ground Motion in g
GMData = 386.4*np.array([0.0063,0.00364,0.00099,0.00428,0.00758,0.01087,0.00682,0.00277,-0.00128,0.00368,0.00864,0.0136,0.00727,0.00094,0.0042,0.00221,0.00021,0.00444,0.00867,0.0129,0.01713,-0.00343,-0.024,-0.00992,0.00416,0.00528,0.01653,0.02779,0.03904,0.02449,0.00995,0.00961,0.00926,0.00892,-0.00486,-0.01864,-0.03242,-0.03365,-0.05723,-0.04534,-0.03346,-0.03201,-0.03056,-0.02911,-0.02766,-0.04116,-0.05466,-0.06816,-0.08166,-0.06846,-0.05527,-0.04208,-0.04259,-0.04311,-0.02428,-0.00545,0.01338,0.03221,0.05104,0.06987,0.0887,0.04524,0.00179,-0.04167,-0.08513,-0.12858,-0.17204,-0.12908,-0.08613,-0.08902,-0.09192,-0.09482,-0.09324,-0.09166,-0.09478,-0.09789,-0.12902,-0.07652,-0.02401,0.02849,0.08099,0.1335,0.186,0.2385,0.21993,0.20135,0.18277,0.1642,0.14562,0.16143,0.17725,0.13215,0.08705,0.04196,-0.00314,-0.04824,-0.09334,-0.13843,-0.18353,-0.22863,-0.27372,-0.31882,-0.25024,-0.18166,-0.11309,-0.04451,0.02407,0.09265,0.16123,0.22981,0.29839,0.23197,0.16554,0.09912,0.0327,-0.03372,-0.10014,-0.16656,-0.23299,-0.29941,-0.00421,0.29099,0.2238,0.15662,0.08943,0.02224,-0.04495,0.01834,0.08163,0.14491,0.2082,0.18973,0.17125,0.13759,0.10393,0.07027,0.03661,0.00295,-0.03071,-0.00561,0.01948,0.04458,0.06468,0.08478,0.10487,0.05895,0.01303,-0.03289,-0.07882,-0.03556,0.00771,0.05097,0.01013,-0.03071,-0.07156,-0.1124,-0.15324,-0.11314,-0.07304,-0.03294,0.00715,-0.0635,-0.13415,-0.2048,-0.12482,-0.04485,0.03513,0.1151,0.19508,0.12301,0.05094,-0.02113,-0.0932,-0.02663,0.03995,0.10653,0.17311,0.11283,0.05255,-0.00772,0.01064,0.029,0.04737,0.06573,0.02021,-0.0253,-0.07081,-0.04107,-0.01133,0.00288,0.01709,0.03131,-0.02278,-0.07686,-0.13095,-0.18504,-0.14347,-0.1019,-0.06034,-0.01877,0.0228,-0.00996,-0.04272,-0.02147,-0.00021,0.02104,-0.01459,-0.05022,-0.08585,-0.12148,-0.15711,-0.19274,-0.22837,-0.18145,-0.13453,-0.08761,-0.04069,0.00623,0.05316,0.10008,0.147,0.09754,0.04808,-0.00138,0.05141,0.1042,0.15699,0.20979,0.26258,0.16996,0.07734,-0.01527,-0.10789,-0.20051,-0.06786,0.06479,0.01671,-0.03137,-0.07945,-0.12753,-0.17561,-0.22369,-0.27177,-0.15851,-0.04525,0.06802,0.18128,0.14464,0.108,0.07137,0.03473,0.09666,0.1586,0.22053,0.18296,0.14538,0.1078,0.07023,0.03265,0.06649,0.10033,0.13417,0.10337,0.07257,0.04177,0.01097,-0.01983,0.04438,0.1086,0.17281,0.10416,0.03551,-0.03315,-0.1018,-0.07262,-0.04344,-0.01426,0.01492,-0.02025,-0.05543,-0.0906,-0.12578,-0.16095,-0.19613,-0.14784,-0.09955,-0.05127,-0.00298,-0.01952,-0.03605,-0.05259,-0.04182,-0.03106,-0.02903,-0.02699,0.02515,0.0177,0.02213,0.02656,0.00419,-0.01819,-0.04057,-0.06294,-0.02417,0.0146,0.05337,0.02428,-0.0048,-0.03389,-0.00557,0.02274,0.00679,-0.00915,-0.02509,-0.04103,-0.05698,-0.01826,0.02046,0.00454,-0.01138,-0.00215,0.00708,0.00496,0.00285,0.00074,-0.00534,-0.01141,0.00361,0.01863,0.03365,0.04867,0.0304,0.01213,-0.00614,-0.02441,0.01375,0.01099,0.00823,0.00547,0.00812,0.01077,-0.00692,-0.02461,-0.0423,-0.05999,-0.07768,-0.09538,-0.06209,-0.0288,0.00448,0.03777,0.01773,-0.00231,-0.02235,0.01791,0.05816,0.03738,0.0166,-0.00418,-0.02496,-0.04574,-0.02071,0.00432,0.02935,0.01526,0.01806,0.02086,0.00793,-0.00501,-0.01795,-0.03089,-0.01841,-0.00593,0.00655,-0.02519,-0.05693,-0.04045,-0.02398,-0.0075,0.00897,0.00384,-0.00129,-0.00642,-0.01156,-0.02619,-0.04082,-0.05545,-0.04366,-0.03188,-0.06964,-0.05634,-0.04303,-0.02972,-0.01642,-0.00311,0.0102,0.0235,0.03681,0.05011,0.02436,-0.00139,-0.02714,-0.00309,0.02096,0.04501,0.06906,0.05773,0.0464,0.03507,0.03357,0.03207,0.03057,0.0325,0.03444,0.03637,0.01348,-0.00942,-0.03231,-0.02997,-0.03095,-0.03192,-0.02588,-0.01984,-0.01379,-0.00775,-0.01449,-0.02123,0.01523,0.0517,0.08816,0.12463,0.16109,0.12987,0.09864,0.06741,0.03618,0.00495,0.0042,0.00345,0.00269,-0.05922,-0.12112,-0.18303,-0.12043,-0.05782,0.00479,0.0674,0.13001,0.08373,0.03745,0.06979,0.10213,-0.03517,-0.17247,-0.13763,-0.10278,-0.06794,-0.0331,-0.03647,-0.03984,-0.00517,0.0295,0.06417,0.09883,0.1335,0.05924,-0.01503,-0.08929,-0.16355,-0.06096,0.04164,0.01551,-0.01061,-0.03674,-0.06287,-0.08899,-0.0543,-0.01961,0.01508,0.04977,0.08446,0.05023,0.016,-0.01823,-0.05246,-0.08669,-0.06769,-0.0487,-0.0297,-0.01071,0.00829,-0.00314,0.02966,0.06246,-0.00234,-0.06714,-0.04051,-0.01388,0.01274,0.00805,0.03024,0.05243,0.02351,-0.00541,-0.03432,-0.06324,-0.09215,-0.12107,-0.0845,-0.04794,-0.01137,0.0252,0.06177,0.04028,0.0188,0.04456,0.07032,0.09608,0.12184,0.0635,0.00517,-0.05317,-0.03124,-0.0093,0.01263,0.03457,0.03283,0.03109,0.02935,0.04511,0.06087,0.07663,0.09239,0.05742,0.02245,-0.01252,0.0068,0.02611,0.04543,0.01571,-0.01402,-0.04374,-0.07347,-0.0399,-0.00633,0.02724,0.0608,0.03669,0.01258,-0.01153,-0.03564,-0.00677,0.0221,0.05098,0.07985,0.06915,0.05845,0.04775,0.03706,0.02636,0.05822,0.09009,0.12196,0.10069,0.07943,0.05816,0.03689,0.01563,-0.00564,-0.0269,-0.04817,-0.06944,-0.0907,-0.11197,-0.11521,-0.11846,-0.1217,-0.12494,-0.165,-0.20505,-0.15713,-0.10921,-0.06129,-0.01337,0.03455,0.08247,0.07576,0.06906,0.06236,0.08735,0.11235,0.13734,0.12175,0.10616,0.09057,0.07498,0.08011,0.08524,0.09037,0.06208,0.03378,0.00549,-0.02281,-0.05444,-0.0403,-0.02615,-0.01201,-0.02028,-0.02855,-0.06243,-0.03524,-0.00805,-0.04948,-0.03643,-0.02337,-0.03368,-0.01879,-0.00389,0.011,0.02589,0.01446,0.00303,-0.0084,0.00463,0.01766,0.03069,0.04372,0.02165,-0.00042,-0.02249,-0.04456,-0.03638,-0.02819,-0.02001,-0.01182,-0.02445,-0.03707,-0.04969,-0.05882,-0.06795,-0.07707,-0.0862,-0.09533,-0.06276,-0.03018,0.00239,0.03496,0.04399,0.05301,0.03176,0.01051,-0.01073,-0.03198,-0.05323,0.00186,0.05696,0.01985,-0.01726,-0.05438,-0.01204,0.03031,0.07265,0.11499,0.07237,0.02975,-0.01288,0.01212,0.03711,0.03517,0.03323,0.01853,0.00383,0.00342,-0.02181,-0.04704,-0.07227,-0.0975,-0.12273,-0.08317,-0.04362,-0.00407,0.03549,0.07504,0.1146,0.07769,0.04078,0.00387,0.00284,0.00182,-0.05513,0.04732,0.05223,0.05715,0.06206,0.06698,0.07189,0.02705,-0.01779,-0.06263,-0.10747,-0.15232,-0.12591,-0.0995,-0.07309,-0.04668,-0.02027,0.00614,0.03255,0.00859,-0.01537,-0.03932,-0.06328,-0.03322,-0.00315,0.02691,0.01196,-0.003,0.00335,0.0097,0.01605,0.02239,0.04215,0.06191,0.08167,0.03477,-0.01212,-0.01309,-0.01407,-0.05274,-0.02544,0.00186,0.02916,0.05646,0.08376,0.01754,-0.04869,-0.02074,0.00722,0.03517,-0.00528,-0.04572,-0.08617,-0.0696,-0.05303,-0.03646,-0.01989,-0.00332,0.01325,0.02982,0.01101,-0.00781,-0.02662,-0.00563,0.01536,0.03635,0.05734,0.03159,0.00584,-0.01992,-0.00201,0.01589,-0.01024,-0.03636,-0.06249,-0.0478,-0.03311,-0.04941,-0.0657,-0.082,-0.0498,-0.0176,0.0146,0.0468,0.079,0.0475,0.016,-0.0155,-0.00102,0.01347,0.02795,0.04244,0.05692,0.03781,0.0187,-0.00041,-0.01952,-0.00427,0.01098,0.02623,0.04148,0.01821,-0.00506,-0.00874,-0.03726,-0.06579,-0.026,0.0138,0.05359,0.09338,0.05883,0.02429,-0.01026,-0.0448,-0.01083,-0.01869,-0.02655,-0.03441,-0.02503,-0.01564,-0.00626,-0.01009,-0.01392,0.0149,0.04372,0.03463,0.02098,0.00733,-0.00632,-0.01997,0.00767,0.03532,0.03409,0.03287,0.03164,0.02403,0.01642,0.00982,0.00322,-0.00339,0.02202,-0.01941,-0.06085,-0.10228,-0.07847,-0.05466,-0.03084,-0.00703,0.01678,0.01946,0.02214,0.02483,0.01809,-0.00202,-0.02213,-0.00278,0.01656,0.0359,0.05525,0.07459,0.06203,0.04948,0.03692,-0.00145,0.04599,0.04079,0.03558,0.03037,0.03626,0.04215,0.04803,0.05392,0.04947,0.04502,0.04056,0.03611,0.03166,0.00614,-0.01937,-0.04489,-0.0704,-0.09592,-0.07745,-0.05899,-0.04052,-0.02206,-0.00359,0.01487,0.01005,0.00523,0.00041,-0.00441,-0.00923,-0.01189,-0.01523,-0.01856,-0.0219,-0.00983,0.00224,0.01431,0.00335,-0.0076,-0.01856,-0.00737,0.00383,0.01502,0.02622,0.01016,-0.0059,-0.02196,-0.00121,0.01953,0.04027,0.02826,0.01625,0.00424,0.00196,-0.00031,-0.00258,-0.00486,-0.00713,-0.00941,-0.01168,-0.01396,-0.0175,-0.02104,-0.02458,-0.02813,-0.03167,-0.03521,-0.04205,-0.04889,-0.03559,-0.02229,-0.00899,0.00431,0.01762,0.00714,-0.00334,-0.01383,0.01314,0.04011,0.06708,0.0482,0.02932,0.01043,-0.00845,-0.02733,-0.04621,-0.03155,-0.01688,-0.00222,0.01244,0.02683,0.04121,0.05559,0.03253,0.00946,-0.0136,-0.01432,-0.01504,-0.01576,-0.04209,-0.02685,-0.01161,0.00363,0.01887,0.03411,0.03115,0.02819,0.02917,0.03015,0.03113,0.00388,-0.02337,-0.05062,-0.0382,-0.02579,-0.01337,-0.00095,0.01146,0.02388,0.03629,0.01047,-0.01535,-0.04117,-0.06699,-0.05207,-0.03715,-0.02222,-0.0073,0.00762,0.02254,0.03747,0.04001,0.04256,0.04507,0.04759,0.0501,0.04545,0.0408,0.02876,0.01671,0.00467,-0.00738,-0.00116,0.00506,0.01128,0.0175,-0.00211,-0.02173,-0.04135,-0.06096,-0.08058,-0.06995,-0.05931,-0.04868,-0.03805,-0.02557,-0.0131,-0.00063,0.01185,0.02432,0.0368,0.04927,0.02974,0.01021,-0.00932,-0.02884,-0.04837,-0.0679,-0.04862,-0.02934,-0.01006,0.00922,0.02851,0.04779,0.02456,0.00133,-0.0219,-0.04513,-0.06836,-0.04978,-0.0312,-0.01262,0.00596,0.02453,0.04311,0.06169,0.08027,0.09885,0.06452,0.03019,-0.00414,-0.03848,-0.07281,-0.05999,-0.04717,-0.03435,-0.03231,-0.03028,-0.02824,-0.00396,0.02032,0.00313,-0.01406,-0.03124,-0.04843,-0.06562,-0.05132,-0.03702,-0.02272,-0.00843,0.00587,0.02017,0.02698,0.03379,0.04061,0.04742,0.05423,0.03535,0.01647,0.01622,0.01598,0.01574,0.00747,-0.0008,-0.00907,0.00072,0.01051,0.0203,0.03009,0.03989,0.03478,0.02967,0.02457,0.03075,0.03694,0.04313,0.04931,0.0555,0.06168,-0.00526,-0.0722,-0.06336,-0.05451,-0.04566,-0.03681,-0.03678,-0.03675,-0.03672,-0.01765,0.00143,0.02051,0.03958,0.05866,0.03556,0.01245,-0.01066,-0.03376,-0.05687,-0.04502,-0.03317,-0.02131,-0.00946,0.00239,-0.00208,-0.00654,-0.01101,-0.01548,-0.012,-0.00851,-0.00503,-0.00154,0.00195,0.00051,-0.00092,0.01135,0.02363,0.0359,0.04818,0.06045,0.07273,0.02847,-0.01579,-0.06004,-0.05069,-0.04134,-0.03199,-0.03135,-0.03071,-0.03007,-0.01863,-0.00719,0.00425,0.0157,0.02714,0.03858,0.02975,0.02092,0.02334,0.02576,0.02819,0.03061,0.03304,0.01371,-0.00561,-0.02494,-0.02208,-0.01923,-0.01638,-0.01353,-0.01261,-0.0117,-0.00169,0.00833,0.01834,0.02835,0.03836,0.04838,0.03749,0.0266,0.01571,0.00482,-0.00607,-0.01696,-0.0078,0.00136,0.01052,0.01968,0.02884,-0.00504,-0.03893,-0.02342,-0.00791,0.00759,0.0231,0.00707,-0.00895,-0.02498,-0.041,-0.05703,-0.0292,-0.00137,0.02645,0.05428,0.03587,0.01746,-0.00096,-0.01937,-0.03778,-0.02281,-0.00784,0.00713,0.0221,0.03707,0.05204,0.06701,0.08198,0.03085,-0.02027,-0.0714,-0.12253,-0.08644,-0.05035,-0.01426,0.02183,0.05792,0.094,0.13009,0.03611,-0.05787,-0.04802,-0.03817,-0.02832,-0.01846,-0.00861,-0.03652,-0.06444,-0.06169,-0.05894,-0.05618,-0.06073,-0.06528,-0.04628,-0.02728,-0.00829,0.01071,0.0297,0.03138,0.03306,0.03474,0.03642,0.04574,0.05506,0.06439,0.07371,0.08303,0.03605,-0.01092,-0.0579,-0.04696,-0.03602,-0.02508,-0.01414,-0.03561,-0.05708,-0.07855,-0.06304,-0.04753,-0.03203,-0.01652,-0.00102,0.00922,0.01946,0.0297,0.03993,0.05017,0.06041,0.07065,0.08089,-0.00192,-0.08473,-0.07032,-0.0559,-0.04148,-0.05296,-0.06443,-0.0759,-0.08738,-0.09885,-0.06798,-0.0371,-0.00623,0.02465,0.05553,0.0864,0.11728,0.14815,0.08715,0.02615,-0.03485,-0.09584,-0.071,-0.04616,-0.02132,0.00353,0.02837,0.05321,-0.00469,-0.06258,-0.12048,-0.0996,-0.07872,-0.05784,-0.03696,-0.01608,0.0048,0.02568,0.04656,0.06744,0.08832,0.1092,0.13008,0.10995,0.08982,0.06969,0.04955,0.04006,0.03056,0.02107,0.01158,0.0078,0.00402,0.00024,-0.00354,-0.00732,-0.0111,-0.0078,-0.0045,-0.0012,0.0021,0.0054,-0.00831,-0.02203,-0.03575,-0.04947,-0.06319,-0.05046,-0.03773,-0.025,-0.01227,0.00046,0.00482,0.00919,0.01355,0.01791,0.02228,0.00883,-0.00462,-0.01807,-0.03152,-0.02276,-0.01401,-0.00526,0.0035,0.01225,0.02101,0.01437,0.00773,0.0011,0.00823,0.01537,0.02251,0.01713,0.01175,0.00637,0.01376,0.02114,0.02852,0.03591,0.04329,0.03458,0.02587,0.01715,0.00844,-0.00027,-0.00898,-0.00126,0.00645,0.01417,0.02039,0.02661,0.03283,0.03905,0.04527,0.03639,0.0275,0.01862,0.00974,0.00086,-0.01333,-0.02752,-0.04171,-0.02812,-0.01453,-0.00094,0.01264,0.02623,0.0169,0.00756,-0.00177,-0.01111,-0.02044,-0.02977,-0.03911,-0.02442,-0.00973,0.00496,0.01965,0.03434,0.02054,0.00674,-0.00706,-0.02086,-0.03466,-0.02663,-0.0186,-0.01057,-0.00254,-0.00063,0.00128,0.00319,0.0051,0.00999,0.01488,0.00791,0.00093,-0.00605,0.00342,0.01288,0.02235,0.03181,0.04128,0.02707,0.01287,-0.00134,-0.01554,-0.02975,-0.04395,-0.03612,-0.02828,-0.02044,-0.0126,-0.00476,0.00307,0.01091,0.00984,0.00876,0.00768,0.00661,0.01234,0.01807,0.0238,0.02953,0.03526,0.02784,0.02042,0.013,-0.03415,-0.00628,-0.00621,-0.00615,-0.00609,-0.00602,-0.00596,-0.0059,-0.00583,-0.00577,-0.00571,-0.00564,-0.00558,-0.00552,-0.00545,-0.00539,-0.00532,-0.00526,-0.0052,-0.00513,-0.00507,-0.00501,-0.00494,-0.00488,-0.00482,-0.00475,-0.00469,-0.00463,-0.00456,-0.0045,-0.00444,-0.00437,-0.00431,-0.00425,-0.00418,-0.00412,-0.00406,-0.00399,-0.00393,-0.00387,-0.0038,-0.00374,-0.00368,-0.00361,-0.00355,-0.00349,-0.00342,-0.00336,-0.0033,-0.00323,-0.00317,-0.00311,-0.00304,-0.00298,-0.00292,-0.00285,-0.00279,-0.00273,-0.00266,-0.0026,-0.00254,-0.00247,-0.00241,-0.00235,-0.00228,-0.00222,-0.00216,-0.00209,-0.00203,-0.00197,-0.0019,-0.00184,-0.00178,-0.00171,-0.00165,-0.00158,-0.00152,-0.00146,-0.00139,-0.00133,-0.00127,-0.0012,-0.00114,-0.00108,-0.00101,-0.00095,-0.00089,-0.00082,-0.00076,-0.0007,-0.00063,-0.00057,-0.00051,-0.00044,-0.00038,-0.00032,-0.00025,-0.00019,-0.00013,-0.00006,0]+list(np.zeros(1000)))
Dt = 0.02

#### Methods used

def CreateNodesFromGrids2D(OData, XGrid, YGrid):
    Nodes = []
    for i in range(len(XGrid)):
        for j in range(len(YGrid)):
            Nodes.append(OData.CreateNode(XGrid[i],YGrid[j],GridX=i, GridY=j,GroupId=j,_Notes='At GridX: %d, GridY: %d'%(i,j)))
    return Nodes

def CreateNodesFromGrids3D(OData, XGrid, YGrid, ZGrid):
    Nodes = []
    for i in range(len(XGrid)):
        for j in range(len(YGrid)):
            for k in range(len(ZGrid)):
                Nodes.append(OData.CreateNode(XGrid[i],YGrid[j],ZGrid[k],GridX=i, GridY=j,GridZ=k,GroupId=k,_Notes='At GridX: %d, GridY: %d, GridZ: %d'%(i,j,k)))
    return Nodes

def AddElasticColumnsToDatabase(OData, column_grids, z_grids, section, transformation_tag, plot_name):
    column_elements = []
    for j in range(1, len(z_grids)):
        for i in range(0, len(column_grids)):
            start = OData.GetNodesByGrid(column_grids[i][0], column_grids[i][1], z_grids[j-1])[0]
            end = OData.GetNodesByGrid(column_grids[i][0], column_grids[i][1], z_grids[j])[0]

            Name = OData.GetFreeElementId(5,z_grids[j])

            import OpenSeesAPI
            Element = OpenSeesAPI.Model.Element.Element.ElasticBeamColumn(Name, start,end,section._A, section._E, section._Iz, transformation_tag, G=section._G, J=section._J, Iy=section._Iy, _PlotName=plot_name ,_Notes=plot_name)
            OData.AddElement(Element)
            column_elements.append(Element)
    return column_elements

def AddElasticBeamsToDatabase(OData, beam_grids, z_grids, section, transformation_tag, plot_name):
    beams_elements = []
    for j in range(0, len(z_grids)):
        for i in range(0, len(beam_grids)):
            NodeI = OData.GetNodesByGrid(beam_grids[i][0], beam_grids[i][1], z_grids[j])[0]
            NodeJ = OData.GetNodesByGrid(beam_grids[i][2], beam_grids[i][3], z_grids[j])[0]
            Name = OData.GetFreeElementId(6,z_grids[j])

            import OpenSeesAPI

            #Pinned Beam Option
            SubNodeI = OData.CreateNode(NodeI.X,NodeI.Y,NodeI.Z,2,NodeI.GridX,NodeI.GridY,NodeI.GridZ,_Notes='Pinned Beam Node at:'+plot_name)
            SubNodeJ = OData.CreateNode(NodeJ.X,NodeJ.Y,NodeJ.Z,2,NodeJ.GridX,NodeJ.GridY,NodeJ.GridZ,_Notes='Pinned Beam Node at:'+plot_name)
            L = ((NodeI.X-NodeJ.X)**2.+(NodeI.Y-NodeJ.Y)**2.)**.5
            EI = section._E*section._Iz*6./L
            RigidMat = OData.AddMaterial(OpenSeesAPI.Model.Element.Material.UniaxialMaterial.Elastic(OData.GetFreeMaterialId(9,NodeI.GridZ),EI*1000,_Notes='Rigid Beam ZeroLength Stiffness at:'+plot_name))
            FlexMat = OData.AddMaterial(OpenSeesAPI.Model.Element.Material.UniaxialMaterial.Elastic(OData.GetFreeMaterialId(9,NodeI.GridZ),EI*0.001,_Notes='Pinned Beam ZeroLength Stiffness at:'+plot_name))
            ZeroDOF1 = OData.AddConstraint(OpenSeesAPI.Model.Element.Element.ZeroLength(OData.GetFreeElementId(9,NodeI.GridZ),NodeI,SubNodeI,[RigidMat,RigidMat,RigidMat,FlexMat,FlexMat,FlexMat],[1,2,3,4,5,6],_Notes='Pinning Beam at:'+plot_name))
            ZeroDOF2 = OData.AddConstraint(OpenSeesAPI.Model.Element.Element.ZeroLength(OData.GetFreeElementId(9,NodeI.GridZ),NodeJ,SubNodeJ,[RigidMat,RigidMat,RigidMat,FlexMat,FlexMat,FlexMat],[1,2,3,4,5,6],_Notes='Pinning Beam at:'+plot_name))
            Element = OpenSeesAPI.Model.Element.Element.ElasticBeamColumn(Name, SubNodeI, SubNodeJ, section._A, section._E, section._Iz, transformation_tag, G=section._G, J=section._J, Iy=section._Iy, _PlotName=plot_name ,_Notes=plot_name)

            #Beam Not Pinned Option
            # Element = OpenSeesAPI.Model.Element.Element.ElasticBeamColumn(Name, NodeI, NodeJ, section._A, section._E, section._Iz, transformation_tag, G=section._G, J=section._J, Iy=section._Iy, _PlotName=plot_name ,_Notes=plot_name)

            OData.AddElement(Element)
            beams_elements.append(Element)
    return beams_elements

def GetNodeBetweenTwoNodes3D(OData, NodeI, NodeJ, PercentageWay, NodeType,_Notes=''):
    Location_X = (NodeJ.X-NodeI.X)*PercentageWay + NodeI.X
    Location_Y = (NodeJ.Y-NodeI.Y)*PercentageWay + NodeI.Y
    Location_Z = (NodeJ.Z-NodeI.Z)*PercentageWay + NodeI.Z

    node = OData.CreateNode(Location_X,Location_Y,Location_Z,NodeType=NodeType,GridX=NodeJ.GridX,GridY=NodeJ.GridY,GridZ=NodeJ.GridZ,_Notes=_Notes)
    return node

def AddNonLinearBraceToDatabase(OData, BraceGrids, BraceLevels, BRBSection, GeoTranfs, _PlotName):
    elements = []
    for j in range(0, len(BraceLevels)):
        for i in range(0, len(BraceGrids)):
            NodeI = OData.GetNodesByGrid(BraceGrids[i][0], BraceGrids[i][1], BraceLevels[j]-1)[0]
            NodeJ = OData.GetNodesByGrid(BraceGrids[i][2], BraceGrids[i][3], BraceLevels[j])[0]

            TopNode = GetNodeBetweenTwoNodes3D(OData,NodeI,NodeJ,.7,2)

            import OpenSeesAPI

            # BRB_Element = OData.AddElement(OpenSeesAPI.Model.Element.Element.Truss(NameBRB, NodeI, TopNode, BRBSection._As, BRBSection._Material,_PlotName=_PlotName))
            # Rigid = 29e3*10
            # Rigid_Element = OData.AddElement(OpenSeesAPI.Model.Element.Element.ElasticBeamColumn(NameRigid, TopNode, NodeJ, BRBSection._As, Rigid, BRBSection._As**10, GeoTranfs, Rigid, BRBSection._As**10, BRBSection._As**2,_PlotName='Rigid Element'))

            # Pinned BRb Element
            TopTopNode = OData.CreateNode(NodeJ.X,NodeJ.Y,NodeJ.Z,2,NodeJ.GridX,NodeJ.GridY,NodeJ.GridZ,GroupId=NodeJ.GridZ,_Notes='Equal DOF Node for Brace')
            BottomBottomNode = OData.CreateNode(NodeI.X,NodeI.Y,NodeI.Z,2,NodeI.GridX,NodeI.GridY,NodeI.GridZ,GroupId=NodeI.GridZ,_Notes='Equal DOF Node for Brace')

            SteelE = 29000
            RigidFactor = 1000
            FreeFactor = 0.001
            RigidMat = OData.AddMaterial(OpenSeesAPI.Model.Element.Material.UniaxialMaterial.Elastic(OData.GetFreeMaterialId(9,NodeI.GridZ), SteelE*RigidFactor*BRBSection._As))
            FreeMat = OData.AddMaterial(OpenSeesAPI.Model.Element.Material.UniaxialMaterial.Elastic(OData.GetFreeMaterialId(9,NodeI.GridZ), SteelE*FreeFactor*BRBSection._As))

            TopBRB_Pin = OData.AddElement(OpenSeesAPI.Model.Element.Element.ZeroLength(OData.GetFreeElementId(9,BraceLevels[j]),TopTopNode,NodeJ,[RigidMat,RigidMat,RigidMat,FreeMat,FreeMat,FreeMat],[1,2,3,4,5,6]))
            Rigid_Element = OData.AddElement(OpenSeesAPI.Model.Element.Element.ElasticBeamColumn(OData.GetFreeElementId(9,BraceLevels[j]), TopNode, NodeJ, BRBSection._As, SteelE*RigidFactor, BRBSection._As*FreeFactor, GeoTranfs, G=SteelE*FreeFactor, J=BRBSection._As,Iy= BRBSection._As,_PlotName='Rigid Element'))
            BRB_Element = OData.AddElement(OpenSeesAPI.Model.Element.Element.Truss(OData.GetFreeElementId(7,BraceLevels[j]), BottomBottomNode, TopTopNode, BRBSection._As, BRBSection._Material,_PlotName=_PlotName))
            BottomBRB_Pin = OData.AddElement(OpenSeesAPI.Model.Element.Element.ZeroLength(OData.GetFreeElementId(9,BraceLevels[j]),NodeI,BottomBottomNode,[RigidMat,RigidMat,RigidMat,FreeMat,FreeMat,FreeMat],[1,2,3,4,5,6]))

            elements.append(BRB_Element)
    return elements

def AddElasticWallsToDatabase(OData, WallGrids, WallLevels, Section, XGrids, YGrids, ZGrids, MeshSize, PlotName):
    import OpenSeesAPI
    for j in range(0,len(WallLevels)):
        for i in range(0,len(WallGrids)):
            tempX = []
            tempX.append(XGrids[WallGrids[i][0]])
            if WallGrids[i][0] != WallGrids[i][2]:
                for k in range(WallGrids[i][0]+1,WallGrids[i][2]+1):
                    if XGrids[k]-XGrids[k-1] > MeshSize:
                        Split = int((XGrids[k]-XGrids[k-1])/float(MeshSize))
                        Size = (XGrids[k]-XGrids[k-1])/float(Split)
                        for l in range(Split-1):
                            tempX.append(XGrids[k-1]+Size*(l+1))
                    tempX.append(XGrids[k])

            tempY = []
            tempY.append(YGrids[WallGrids[i][1]])
            if WallGrids[i][1] != WallGrids[i][3]:
                for k in range(WallGrids[i][1]+1,WallGrids[i][3]+1):
                    if YGrids[k]-YGrids[k-1] > MeshSize:
                        Split = int((YGrids[k]-YGrids[k-1])/float(MeshSize))
                        Size = (YGrids[k]-YGrids[k-1])/float(Split)
                        for l in range(Split-1):
                            tempY.append(YGrids[k-1]+Size*(l+1))
                    tempY.append(YGrids[k])

            tempZ = []
            tempZ.append(ZGrids[WallLevels[j]-1])
            for k in range(WallLevels[j]-1,WallLevels[j]):
                if ZGrids[k+1]-ZGrids[k] > MeshSize:
                    Split = int((ZGrids[k+1]-ZGrids[k])/float(MeshSize))
                    Size = (ZGrids[k+1]-ZGrids[k])/float(Split)
                    for l in range(Split-1):
                        tempZ.append(ZGrids[k]+Size*(l+1))
                tempZ.append(ZGrids[k+1])

            HorizontalPlan = tempX if len(tempX)>len(tempY) else tempY
            PerpDirection = tempY if len(tempX)>len(tempY) else tempX

            NodeArray = [[0 for x in range(len(tempZ))] for x in range(len(HorizontalPlan))]

            # Fill in Node Array
            for c in range(len(tempZ)):
                for b in range(len(HorizontalPlan)):
                    if len(tempX)>len(tempY):
                        Nodes = list(filter(lambda x: x.X == tempX[b] and x.Y == tempY[0] and x.Z == tempZ[c] and (x.NodeType == 1 or x.NodeType == 4), OData._Nodes))
                        if len(Nodes) == 1:
                            NodeArray[b][c] = Nodes[0]
                        else:
                            NodeArray[b][c] = OData.CreateNode(tempX[b],tempY[0],tempZ[c],NodeType=4,_Notes='Wall Node')
                    else:
                        Nodes = list(filter(lambda x: x.X == tempX[0] and x.Y == tempY[b] and x.Z == tempZ[c] and (x.NodeType == 1 or x.NodeType == 4), OData._Nodes))
                        if len(Nodes) == 1:
                            NodeArray[b][c] = Nodes[0]
                        else:
                            NodeArray[b][c] = OData.CreateNode(tempX[0],tempY[b],tempZ[c],NodeType=4,_Notes='Wall Node')

            # Create Elements
            for c in range(1,len(tempZ)):
                for b in range(1,len(HorizontalPlan)):
                    OData.AddQuadrilateral(OpenSeesAPI.Model.Element.Element.ShellMITC4(OData.GetFreeElementId(8,WallLevels[j]), NodeArray[b-1][c-1], NodeArray[b][c-1], NodeArray[b][c],NodeArray[b-1][c], Section ,_Notes=PlotName,_PlotName=PlotName))

def AddMeshedSlabToDatabase(OData, SlabGrids, SlabLevels, Section, xgrids, ygrids, zgrids, MeshSize, PlotName):
    import OpenSeesAPI
    for i in range(0,len(SlabLevels)):
        for j in range(0,len(SlabGrids)):

            Z = zgrids[SlabLevels[i]]

            SouthWestX = xgrids[SlabGrids[j][0]]
            SouthWestY = ygrids[SlabGrids[j][1]]
            NorthEastX = xgrids[SlabGrids[j][4]]
            NorthEastY = ygrids[SlabGrids[j][5]]

            XGrids = []
            YGrids = []

            ONodes_Z = OData.GetNodesByZCoordinate(Z,NodeType=1)+OData.GetNodesByZCoordinate(Z,NodeType=4)
            for node in ONodes_Z:
                if SouthWestX <= node.X and SouthWestY <= node.Y and NorthEastX >= node.X and NorthEastY >= node.Y:
                    if not(XGrids.__contains__(node.X)):
                        XGrids.append(node.X)
                    if not(YGrids.__contains__(node.Y)):
                        YGrids.append(node.Y)


            XGrids.sort()
            YGrids.sort()

            #Make sure the grid spacing is smaller than the mesh size
            for m in range(1,len(XGrids)):
                if XGrids[m] - XGrids[m-1] > MeshSize:
                    split = int((XGrids[m] - XGrids[m-1])/float(MeshSize))
                    splitlength = float((XGrids[m] - XGrids[m-1]))/split
                    for n in range(1,split):
                        XGrids.append(XGrids[m-1]+splitlength*(n))
            XGrids.sort()

            for m in range(1,len(YGrids)):
                if YGrids[m] - YGrids[m-1] > MeshSize:
                    split = int((YGrids[m] - YGrids[m-1])/float(MeshSize))
                    splitlength = float((YGrids[m] - YGrids[m-1]))/split
                    for n in range(1,split):
                        YGrids.append(YGrids[m-1]+splitlength*(n))
            YGrids.sort()

            #Create Nodes
            NodeArray = [[0 for x in range(len(YGrids))] for x in range(len(XGrids))]

            for a in range(0,len(XGrids)):
                for b in range(0,len(YGrids)):
                    Nodes = list(filter(lambda x: x.X == XGrids[a] and x.Y == YGrids[b] and x.Z == Z and (x.NodeType == 1 or x.NodeType == 4), OData._Nodes))
                    if len(Nodes) == 1:
                        NodeArray[a][b] = Nodes[0]
                    else:
                        NodeArray[a][b] = OData.CreateNode(XGrids[a],YGrids[b],Z,4,_Notes='Slab Node')

            #Create Quads
            for a in range(1,len(XGrids)):
                for b in range(1,len(YGrids)):
                    Element = OpenSeesAPI.Model.Element.Element.ShellMITC4(OData.GetFreeElementId(8,SlabLevels[i]), NodeArray[a-1][b-1], NodeArray[a-1][b], NodeArray[a][b],NodeArray[a][b-1], Section ,_Notes=PlotName,_PlotName=PlotName)
                    OData.AddQuadrilateral(Element)

def TBI_BRB_A(GMDataX,GMDataY, Dt, T1=None,T2=None, SupressOutput=True, Viewer = False, Animation = False, PushOver=False, OpenSeesCommand = 'OpenSeesSP', TestingModeOff=True):
    ### TesingMode
    TestingModeOff = TestingModeOff

    ### Import Libraries
    import os
    import numpy as np

    #Variables
    g=386.1

    #region ########################## Pre-Initialization ##########################
    import OpenSeesAPI

    #endregion

    #region ########################## Initializing ##########################

    ### Create OpenSees Database

    import time
    import uuid
    randomnumber = str(uuid.uuid4()).replace('-','').upper()
    timestamp = ''#time.strftime("%y%m%d-%H%M%S")+randomnumber
    ModelName = 'TBI-BRB'
    FileName = '%s-%s.tcl'%(ModelName,timestamp)

    FileLocation = os.getcwd()+'/tcl/'
    ResultFileLocation = os.getcwd()+'/tcl/Results/'
    OData = OpenSeesAPI.Database.Collector(OpenSeesCommand, FileLocation, FileName)

    if not os.path.exists(FileLocation): #Make Directory is unavailable
        os.makedirs(FileLocation)
    if not os.path.exists(ResultFileLocation): #Make Directory is unavailable
        os.makedirs(ResultFileLocation)

    #endregion

    #region ########################## Setup and Source Definition ##########################
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Initialization'))
    OData.AddObject(OpenSeesAPI.Model.BasicBuilder(3,6))
    OData.AddObject(OpenSeesAPI.Output.LogFile(OData.Executable.LogFileName)) # Start Log File

    #endregion

    #region ########################## Define Building Geometry, Nodes and Constraints ##########################
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Geometry Setup'))

    #Defining Grids
    XGrids = np.array([0, 342, 822, 1002, 1182, 1362, 1542, 1722, 1902, 2382, 2724])
    YGrids = np.array([0, 339, 679, 918, 1158, 1320, 1482, 1722, 1962, 2301, 2640])
    if TestingModeOff:
        ZGrids = 12*np.array([0, 12, 24, 36, 48, 66, 79.5, 93, 106.5, 120, 133.5, 147, 160.5, 174, 187.5, 201, 214.5, 228, 241.5, 255, 268.5, 282, 295.5, 309, 322.5, 336, 349.5, 363, 376.5, 390, 403.5, 417, 430.5, 444, 457.5, 471, 484.5, 498, 511.5, 525, 538.5, 552, 565.5, 579, 592.5])
    else:
        ZGrids = 12*np.array([0, 12, 24, 36, 48])

    #Create Grid Nodes
    GridNodes = CreateNodesFromGrids3D(OData, XGrids, YGrids, ZGrids)

    #Create Diaphragm Nodes
    DiaphragmNodes = []
    for i in range(5,len(ZGrids)):
        DiaphragmNodes.append(OData.CreateNode((XGrids[-1]-XGrids[0])/2.,(YGrids[-1]-YGrids[0])/2.,ZGrids[i],3,_Notes='Rigid Diaphragm Node at ZGrid: %d'%i))
        DiaphragmNodes[-1].__setattr__('Used',True)

    #Defining Floor Weights
    g = 386.4
    if TestingModeOff:
        FloorMass = np.array([0,86*2.75,86*2.75,86*2.75,506.85*2.75,137,127,127,127,120,120,120,120,120,
                              115, 115, 115,115,115,
                              107,107,107,107,107,
                              102,102,102,102,
                              96,96,96,96,
                              92,92,92,92,92,
                              88,88,88,88,88,88,88,88,
                              105.66])*18190/g/1000
        EquivLoad = np.array([0,86,86,86,506.85,137,127,127,127,120,120,120,120,120,
                              115, 115, 115,115,115,
                              107,107,107,107,107,
                              102,102,102,102,
                              96,96,96,96,
                              92,92,92,92,92,
                              88,88,88,88,88,88,88,88,
                              105.66])*18190/g/1000
    else:
        FloorMass = np.array([0,86*2.75,86*2.75,86*2.75,506.85*2.75])*18190/g/1000
        EquivLoad = np.array([0,86,86,86,506.85])*18190/g/1000

    #endregion

    #region ########################## Define Geometric Transformations ##########################
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Define Geometric Transformations'))

    #Define Geometry Transformations for Beams and Column
    GeoTransfLinear = OData.AddObject(OpenSeesAPI.Model.Element.GeomTransf.Linear(1,VectorX=0,VectorY=1,VectorZ=0)) #Apply to Everything Else
    ColumnGeoTransfPDelta = OData.AddObject(OpenSeesAPI.Model.Element.GeomTransf.PDelta(2,VectorX=0,VectorY=1,VectorZ=0)) #Apply To Leaning Column
    BeamGeoTransfPDelta = OData.AddObject(OpenSeesAPI.Model.Element.GeomTransf.PDelta(3,VectorX=0,VectorY=0,VectorZ=1)) #Apply To Beams
    BraceGeoTransfPDelta = OData.AddObject(OpenSeesAPI.Model.Element.GeomTransf.PDelta(4,VectorX=0,VectorY=0,VectorZ=1)) #Apply To Braces

    #endregion

    ##############################################################################
    ### All OpenSEES Objects are adding directly to the Database Beyond This Point
    ##############################################################################

    #region ########################## Define Materials and Sections ##########################
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Define Materials and Sections'))

    ElasticRigid = OData.AddObject(OpenSeesAPI.Model.Element.Material.UniaxialMaterial.Elastic(OData.GetFreeMaterialId(4,0),1e9,_Notes='This is made to match the initial bond-slip M-rot'))
    ElasticFree = OData.AddObject(OpenSeesAPI.Model.Element.Material.UniaxialMaterial.Elastic(OData.GetFreeMaterialId(4,0),1e1,_Notes='ElasticSteel - Used For Leaning Column Strut'))

    Column_Gravity = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(1,1), 29000.0, 1064, 1000.0, G=11500.0, J=1000.0, Iy=1000.0))

    Column_18_15 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(1,1),29000,143.224137931034,5358.4525862069,G=11153.8461538462,J=30992.3631465517,Iy=5358.4525862069 ))
    Column_21_15 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(1,1),29000,180.68275862069,9178.18448275862,G=11153.8461538462,J=61415.7711206897,Iy=9178.18448275862 ))
    Column_24_2 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(1,1),29000,254.620689655172,16935.3563218391,G=11153.8461538462,J=97951.1724137931,Iy=16935.3563218391 ))
    Column_27_2 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(1,1),29000,303.975862068966,25550.2692528736,G=11153.8461538462,J=165320.375646552,Iy=25550.2692528736 ))
    Column_30_25 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(1,1),29000,397.844827586207,41346.0847701149,G=11153.8461538462,J=239138.604525862,Iy=41346.0847701149 ))
    Column_33_25 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(1,1),29000,459.096551724138,57673.058045977,G=11153.8461538462,J=365410.072844828,Iy=57673.058045977 ))
    Column_36_25 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(1,1),29000,523.886206896552,78134.5537356322,G=11153.8461538462,J=536442.571767241,Iy=78134.5537356322 ))
    Column_39_25 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(1,1),29000,596.55875862069,103732.243747126,G=11153.8461538462,J=774042.504603448,Iy=103732.243747126 ))
    Column_42_3 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(1,1),29000,722.731034482759,146850.951724138,G=11153.8461538462,J=982652.337931035,Iy=146850.951724138 ))
    Column_45_3 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(1,1),29000,802.955172413793,186824.568103448,G=11153.8461538462,J=1330621.61702586,Iy=186824.568103448 ))
    Column_48_3 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(1,1),29000,886.71724137931,234027.434482759,G=11153.8461538462,J=1764172.45862069,Iy=234027.434482759 ))
    Column_51_3 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(1,1),29000,974.01724137931,289213.409482759,G=11153.8461538462,J=2296364.22737069,Iy=289213.409482759 ))
    Column_54_3 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(1,1),29000,1064.85517241379,353168.193103448,G=11153.8461538462,J=2941187.64827586,Iy=353168.193103448 ))
    Column_56_3 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(1,1),29000,1127.37931034483,401078.689655172,G=11153.8461538462,J=3440973.67241379,Iy=401078.689655172 ))
    Column_60_3 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(1,1),29000,1257.14482758621,510686.193103448,G=11153.8461538462,J=4629349.14827586,Iy=510686.193103448 ))

    W14X53 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(2,1),29000,15.6,57.7,G=11153.8461538462,J=1.94,Iy=541))
    W14X68 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(2,1),29000,20,121,G=11154.2307692308,J=3.01,Iy=722))
    W16X100 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(2,1),29000,29.4,186,G=11153.8461538462,J=7.73,Iy=1490))
    W14X132 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(2,1),29000,38.8,548,G=11153.8461538462,J=12.3,Iy=1530))
    W14X159 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(2,1),29000,46.7,748,G=11153.8461538462,J=19.7,Iy=1900))
    W16X100 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(2,1),29000,29.4,186,G=11153.8461538462,J=7.73,Iy=1490))
    W14X176 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(2,1),29000,51.8,838,G=11153.8461538462,J=26.5,Iy=2140))
    W24X162 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(2,1),29000,47.8,443,G=11153.8461538462,J=18.5,Iy=5170))
    W24X131 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(2,1),29000,38.6,340,G=11153.8461538462,J=9.5,Iy=4020))
    W14X193 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.Elastic(OData.GetFreeMaterialId(2,1),29000,56.8,931,G=11154.2307692308,J=34.8,Iy=2400))

    Wall_18_5000 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.ElasticMembranePlateSection(OData.GetFreeMaterialId(1,1),5000*.3,0.2*0.5/0.4,18,0.0,_Notes='18 inch Wall 5000 psi'))
    Wall_24_5000 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.ElasticMembranePlateSection(OData.GetFreeMaterialId(1,1),5000*.3,0.2*0.5/0.4,24,0.0,_Notes='24 inch Wall 5000 psi'))

    Slab_4_4000 = OData.AddObject(OpenSeesAPI.Model.Element.Material.Section.ElasticMembranePlateSection(OData.GetFreeMaterialId(1,1),4000*.3,0.2,4,0.0,_Notes='3.25Conc + 3indeck'))

    #endregion

    #region ########################## Define Rotational Springs for Plastic Hinge ##########################
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Define Rotational Springs for Plastic Hinge'))

    #Define Rotational Spring
    class BRB_Truss_Section:
        def __init__(self, id, As, E, Fy, Ry, w, Beta):
            self._id = id
            self._As = As
            self._E = E
            self._Fy = Fy
            self._Ry = Ry
            self._w = w
            self._Beta = Beta
            self._Ko = E

            self._s1p = Ry*Fy
            self._e1p = self._s1p/self._Ko
            self._s2p = w * Ry * Fy
            self._e2p = 10*self._e1p
            self._s3p = self._s2p + (self._e1p*10)*0.0125*self._Ko
            self._e3p = self._e2p * 2

            self._s1n = -1*Ry*Fy
            self._e1n = -1*self._e1p
            self._s2n = -1*Beta*w*Ry*Fy
            self._e2n = -1*self._e2p
            self._s3n = -1*(-1*self._s2n + 0.0125*self._Ko*(self._e1p*10))
            self._e3n = -1*self._e3p

            self._pinchx = 1.0
            self._pinchy = 1.0
            self._damage1 = 0.0
            self._damage2 = 0.0
            self._degradation = 0.001

            self._BRBMaterial = OpenSeesAPI.Model.Element.Material.UniaxialMaterial.Hysteretic(id, self._s1p, self._e1p,
                self._s2p, self._e2p, self._s1n,
                self._e1n, self._s2n, self._e2n,
                self._pinchx, self._pinchy, self._damage1, self._damage2,
                self._s3p, self._e3p,self._s3n, self._e3n)

            self._Material = OpenSeesAPI.Model.Element.Material.UniaxialMaterial.MinMax(OData.GetFreeMaterialId(1,1),self._BRBMaterial,self._e3n,self._e3p)
            OData.AddObject(self._BRBMaterial)

            # self._Material = self._BRBMaterial
            OData.AddObject(self._Material)

    Brace_205= BRB_Truss_Section(OData.GetFreeMaterialId(3,1), 5.99415204678363, 29000, 38, 1.1,1.25,1.1)
    Brace_228= BRB_Truss_Section(OData.GetFreeMaterialId(3,1), 6.66666666666667, 29000, 38, 1.1,1.25,1.1)
    Brace_239= BRB_Truss_Section(OData.GetFreeMaterialId(3,1), 6.98830409356725, 29000, 38, 1.1,1.25,1.1)
    Brace_274= BRB_Truss_Section(OData.GetFreeMaterialId(3,1), 8.01169590643275, 29000, 38, 1.1,1.25,1.1)
    Brace_308= BRB_Truss_Section(OData.GetFreeMaterialId(3,1), 9.00584795321637, 29000, 38, 1.1,1.25,1.1)
    Brace_342= BRB_Truss_Section(OData.GetFreeMaterialId(3,1), 10, 29000, 38, 1.1,1.25,1.1)
    Brace_376= BRB_Truss_Section(OData.GetFreeMaterialId(3,1), 10.9941520467836, 29000, 38, 1.1,1.25,1.1)
    Brace_380= BRB_Truss_Section(OData.GetFreeMaterialId(3,1), 11.1111111111111, 29000, 38, 1.1,1.25,1.1)
    Brace_462= BRB_Truss_Section(OData.GetFreeMaterialId(3,1), 13.5087719298246, 29000, 38, 1.1,1.25,1.1)
    Brace_479= BRB_Truss_Section(OData.GetFreeMaterialId(3,1), 14.0058479532164, 29000, 38, 1.1,1.25,1.1)
    Brace_513= BRB_Truss_Section(OData.GetFreeMaterialId(3,1), 15, 29000, 38, 1.1,1.25,1.1)
    Brace_530= BRB_Truss_Section(OData.GetFreeMaterialId(3,1), 15.4970760233918, 29000, 38, 1.1,1.25,1.1)
    Brace_589= BRB_Truss_Section(OData.GetFreeMaterialId(3,1), 17.2222222222222, 29000, 38, 1.1,1.25,1.1)
    Brace_633= BRB_Truss_Section(OData.GetFreeMaterialId(3,1), 18.5087719298246, 29000, 38, 1.1,1.25,1.1)
    Brace_703= BRB_Truss_Section(OData.GetFreeMaterialId(3,1), 20.5555555555556, 29000, 38, 1.1,1.25,1.1)
    Brace_855= BRB_Truss_Section(OData.GetFreeMaterialId(3,1), 25, 29000, 38, 1.1,1.25,1.1)
    Brace_923= BRB_Truss_Section(OData.GetFreeMaterialId(3,1), 26.9883040935673, 29000, 38, 1.1,1.25,1.1)
    Brace_950= BRB_Truss_Section(OData.GetFreeMaterialId(3,1), 27.7777777777778, 29000, 38, 1.1,1.25,1.1)
    Brace_1026= BRB_Truss_Section(OData.GetFreeMaterialId(3,1), 30, 29000, 38, 1.1,1.25,1.1)

    ########################## Define Elements ##########################
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Define Elements'))

    #### Gravity Columns ####
    #Defining Column Grids & Levels - Define Grid Numbers Where Columns Occur

    ColumnSet = []
    ColumnGrids =   [
                    [2,2],[4,2],[6,2],[8,2],
                    [2,8],[4,8],[6,8],[8,8]
                    ] # What Grids the Columns Occur
    if TestingModeOff:
       ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(0, 45), Column_Gravity,ColumnGeoTransfPDelta,'Columns - Gravity'))
    else:
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(0, 5), Column_Gravity,ColumnGeoTransfPDelta,'Columns - Gravity'))

    #### Gravity Columns ####
    #Defining Column Grids - Define Grid Numbers Where Columns Occur

    ColumnGrids = [
                    [1,2],[9,2],[1,8],[9,8]
                   ] # What Grids the Columns Occur
    if TestingModeOff:
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(14, 45), Column_Gravity,ColumnGeoTransfPDelta,'Columns - Gravity'))

    #### Lateral Columns ####
    #Defining Column Grids - Define Grid Numbers Where Columns Occur

    ColumnGrids = [
                    [1,2], [1,8],
                    [9,2], [9,8]
                    ] # What Grids the Columns Occur
    if TestingModeOff:
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(0, 4), Column_39_25, ColumnGeoTransfPDelta,'Columns - 54x54inch '))
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(3, 6), Column_36_25, ColumnGeoTransfPDelta,'Columns - 51x51inch '))
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(5, 8), Column_30_25, ColumnGeoTransfPDelta,'Columns - 48x48inch '))
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(7, 10), Column_27_2, ColumnGeoTransfPDelta,'Columns - 48x48inch '))
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(9, 12), Column_24_2, ColumnGeoTransfPDelta,'Columns - 48x48inch '))
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(11, 15), Column_21_15, ColumnGeoTransfPDelta,'Columns - 48x48inch '))
    else:
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(0, 5), Column_39_25, ColumnGeoTransfPDelta,'Columns - 54x54inch '))


    #Defining Column Grids - Define Grid Numbers Where Columns Occur
    ColumnGrids = [[1,4],[1,6],
                   [2,4],[2,6],
                   [4,4],[4,6],
                   [6,4],[6,6],
                   [8,4],[8,6],
                   [9,4],[9,6]] # What Grids the Columns Occur
    if TestingModeOff:
        #Defining Column Elements
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(0, 4), Column_54_3, ColumnGeoTransfPDelta,'Columns - 54x54inch '))
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(3, 8), Column_51_3, ColumnGeoTransfPDelta,'Columns - 51x51inch '))
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(7, 12), Column_48_3, ColumnGeoTransfPDelta,'Columns - 48x48inch '))
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(11, 14), Column_45_3, ColumnGeoTransfPDelta,'Columns - 45x45inch '))
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(13, 16), Column_42_3, ColumnGeoTransfPDelta,'Columns - 42x42inch '))
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(15, 20), Column_39_25, ColumnGeoTransfPDelta,'Columns - 39x39inch '))
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(19, 22), Column_36_25, ColumnGeoTransfPDelta,'Columns - 36x36inch '))
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(21, 24), Column_33_25, ColumnGeoTransfPDelta,'Columns - 33x33inch '))
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(23, 26), Column_30_25, ColumnGeoTransfPDelta,'Columns - 30x30inch '))
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(25, 28), Column_27_2, ColumnGeoTransfPDelta,'Columns - 27x27inch '))
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(27, 32), Column_24_2, ColumnGeoTransfPDelta,'Columns - 24x24inch '))
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(31, 45), Column_21_15, ColumnGeoTransfPDelta,'Columns - 21x21inch '))
    else:
        ColumnSet.extend(AddElasticColumnsToDatabase(OData,ColumnGrids,range(0, 5), Column_54_3, ColumnGeoTransfPDelta,'Columns - 54x54inch '))

    #### Beams ####
    BeamSet = []
    #Defining Beam Grids - Start Grids to End Grids
    #1X & 9X
    BeamGrids = [[1,2,1,3], [1,3,1,4],  [1,6,1,7], [1,7,1,8], #Grid 0X
                 [9,2,9,3], [9,3,9,4],  [9,6,9,7], [9,7,9,8], #Grid 8X
                 ]  # What grids do the beams connect to
    if TestingModeOff:
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(1, 4), W24X131, BeamGeoTransfPDelta,'Beam - W24x131'))
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(4, 5), W24X162, BeamGeoTransfPDelta,'Beam - W24x162'))
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(5, 12), W14X193, BeamGeoTransfPDelta,'Beam - W14x193'))
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(12, 15), W14X176, BeamGeoTransfPDelta,'Beam - W14x176'))
    else:
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(1, 5), W24X131, BeamGeoTransfPDelta,'Beam - W24x131'))

    #1-(4/6) X
    BeamGrids = [ [1,4,1,5], [1,5,1,6], #Grid 0X
                  [9,4,9,5], [9,5,9,6] #Grid 8X
                 ]  # What grids do the beams connect to
    if TestingModeOff:
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(1, 15), W16X100, BeamGeoTransfPDelta,'Beam - W16x100'))
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(15, 24), W14X159, BeamGeoTransfPDelta,'Beam - W14x159'))
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(24, 28), W14X132, BeamGeoTransfPDelta,'Beam - W14x132'))
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(28, 32), W16X100, BeamGeoTransfPDelta,'Beam - W16x100'))
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(32, 40), W14X68, BeamGeoTransfPDelta,'Beam - W14x68'))
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(40, 45), W14X53, BeamGeoTransfPDelta,'Beam - W14x53'))
    else:
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(1, 5), W16X100, BeamGeoTransfPDelta,'Beam - W16x100'))

    #2 4 6 8 X
    BeamGrids = [
                 [2,4,2,5], [2,5,2,6], [4,4,4,5], [4,5,4,6], #Grid 1-3X
                 [6,4,6,5], [6,5,6,6], [8,4,8,5], [8,5,8,6], #Grid 5-7X
                 ]  # What grids do the beams connect to
    if TestingModeOff:
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(1, 15), W16X100, BeamGeoTransfPDelta,'Beam - W16x100'))
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(15, 24), W14X159, BeamGeoTransfPDelta,'Beam - W14x159'))
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(24, 28), W14X132, BeamGeoTransfPDelta,'Beam - W14x132'))
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(28, 32), W16X100, BeamGeoTransfPDelta,'Beam - W16x100'))
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(32, 40), W14X68, BeamGeoTransfPDelta,'Beam - W14x68'))
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(40, 45), W14X53, BeamGeoTransfPDelta,'Beam - W14x53'))
    else:
       BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(1, 5), W16X100, BeamGeoTransfPDelta,'Beam - W16x100'))

    #4Y & 6Y
    BeamGrids = [
                 [2,4,3,4], [3,4,4,4], [4,4,5,4], [5,4,6,4], [6,4,7,4], [7,4,8,4], #Grid 2Y
                 [2,6,3,6], [3,6,4,6], [4,6,5,6], [5,6,6,6], [6,6,7,6], [7,6,8,6] #Grid 4Y
                 ]  # What grids do the beams connect to
    if TestingModeOff:
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(1, 15), W16X100, BeamGeoTransfPDelta,'Beam - W16x100'))
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(15, 24), W14X159, BeamGeoTransfPDelta,'Beam - W14x159'))
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(24, 28), W14X132, BeamGeoTransfPDelta,'Beam - W14x132'))
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(28, 32), W16X100, BeamGeoTransfPDelta,'Beam - W16x100'))
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(32, 40), W14X68, BeamGeoTransfPDelta,'Beam - W14x68'))
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(40, 45), W14X53, BeamGeoTransfPDelta,'Beam - W14x53'))
    else:
        BeamSet.extend(AddElasticBeamsToDatabase(OData, BeamGrids, range(1, 5), W16X100, BeamGeoTransfPDelta,'Beam - W16x100'))

    #### Braces ####
    #Define Braces
    #Grid 1X #Define Bottom-to-Top
    BraceGrids = [ [1,4,1,5], [1,6,1,5] ]#Grid 0X #Define Bottom-to-Top
    BraceSet = []
    if TestingModeOff:
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(1, 15), Brace_530, BraceGeoTransfPDelta, 'BRB - 530 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(15, 24), Brace_855, BraceGeoTransfPDelta, 'BRB - 855 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(24, 28), Brace_633, BraceGeoTransfPDelta, 'BRB - 633 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(28, 32), Brace_530, BraceGeoTransfPDelta, 'BRB - 530 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(32, 40), Brace_308, BraceGeoTransfPDelta, 'BRB - 308 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(40, 45), Brace_205, BraceGeoTransfPDelta, 'BRB - 205 k'))
    else:
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(1, 5), Brace_530, BraceGeoTransfPDelta, 'BRB - 530 k'))

    BraceGrids = [[1,2,1,3], [1,4,1,3],  [1,6,1,7], [1,8,1,7]]
    if TestingModeOff:
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(1, 4), Brace_633, BraceGeoTransfPDelta, 'BRB - 633 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(4, 7), Brace_923, BraceGeoTransfPDelta, 'BRB - 923 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(7, 15), Brace_855, BraceGeoTransfPDelta, 'BRB - 855 k'))
    else:
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(1, 5), Brace_633, BraceGeoTransfPDelta, 'BRB - 633 k'))

    #Grid 9X
    BraceGrids = [[9,4,9,5], [9,6,9,5] ]#Grid 0X #Define Bottom-to-Top
    if TestingModeOff:
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(1, 15), Brace_530, BraceGeoTransfPDelta, 'BRB - 530 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(15, 24), Brace_855, BraceGeoTransfPDelta, 'BRB - 855 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(24, 28), Brace_633, BraceGeoTransfPDelta, 'BRB - 633 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(28, 32), Brace_530, BraceGeoTransfPDelta, 'BRB - 530 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(32, 40), Brace_308, BraceGeoTransfPDelta, 'BRB - 308 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(40, 45), Brace_205, BraceGeoTransfPDelta, 'BRB - 205 k'))
    else:
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(1, 5), Brace_530, BraceGeoTransfPDelta, 'BRB - 530 k'))

    BraceGrids = [[9,2,9,3], [9,4,9,3], [9,6,9,7], [9,8,9,7] ]
    if TestingModeOff:
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(1, 4), Brace_633, BraceGeoTransfPDelta, 'BRB - 633 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(4, 7), Brace_923, BraceGeoTransfPDelta, 'BRB - 923 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(7, 15), Brace_855, BraceGeoTransfPDelta, 'BRB - 855 k'))
    else:
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(1, 5), Brace_633, BraceGeoTransfPDelta, 'BRB - 633 k'))

    #Grid 2,8X
    BraceGrids = [[2,4,2,5], [2,6,2,5], [8,4,8,5], [8,6,8,5]]
    if TestingModeOff:
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(1, 36), Brace_462, BraceGeoTransfPDelta, 'BRB - 462 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(36, 40), Brace_376, BraceGeoTransfPDelta, 'BRB - 376 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(40, 43), Brace_308, BraceGeoTransfPDelta, 'BRB - 308 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(43, 45), Brace_239, BraceGeoTransfPDelta, 'BRB - 239 k'))
    else:
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(1, 5), Brace_462, BraceGeoTransfPDelta, 'BRB - 462 k'))

    #Grid 4,6X
    BraceGrids = [ [4,4,4,5], [4,6,4,5], [6,4,6,5], [6,6,6,5]]
    if TestingModeOff:
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(1, 36), Brace_462, BraceGeoTransfPDelta, 'BRB - 462 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(36, 40), Brace_376, BraceGeoTransfPDelta, 'BRB - 376 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(40, 45), Brace_239, BraceGeoTransfPDelta, 'BRB - 239 k'))
    else:
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(1, 5), Brace_462, BraceGeoTransfPDelta, 'BRB - 462 k'))

    #Grid 4Y
    BraceGrids = [ [2,4,3,4], [4,4,3,4], [4,4,5,4], [6,4,5,4], [6,4,7,4], [8,4,7,4] ]
    if TestingModeOff:
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(1, 4), Brace_479, BraceGeoTransfPDelta, 'BRB - 479 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(4, 30), Brace_530, BraceGeoTransfPDelta, 'BRB - 530 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(30, 35), Brace_462, BraceGeoTransfPDelta, 'BRB - 462 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(35, 39), Brace_342, BraceGeoTransfPDelta, 'BRB - 342 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(39, 42), Brace_274, BraceGeoTransfPDelta, 'BRB - 274 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(42, 45), Brace_239, BraceGeoTransfPDelta, 'BRB - 239 k'))
    else:
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(1, 5), Brace_479, BraceGeoTransfPDelta, 'BRB - 479 k'))

    #Grid 6Y
    BraceGrids = [ [2,6,3,6], [4,6,3,6], [4,6,5,6], [6,6,5,6], [6,6,7,6], [8,6,7,6] ]
    if TestingModeOff:
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(1, 4), Brace_479, BraceGeoTransfPDelta, 'BRB - 479 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(4, 30), Brace_530, BraceGeoTransfPDelta, 'BRB - 530 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(30, 35), Brace_462, BraceGeoTransfPDelta, 'BRB - 462 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(35, 39), Brace_342, BraceGeoTransfPDelta, 'BRB - 342 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(39, 42), Brace_274, BraceGeoTransfPDelta, 'BRB - 274 k'))
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(42, 45), Brace_239, BraceGeoTransfPDelta, 'BRB - 239 k'))
    else:
        BraceSet.extend(AddNonLinearBraceToDatabase(OData, BraceGrids, range(1, 5), Brace_479, BraceGeoTransfPDelta, 'BRB - 479 k'))

    #### Walls ####

    WallGrids = [[0,0,0,10],
             [0,0,10,0],
             [0,10,10,10],
             [10,0,10,10]]

    if TestingModeOff:
        WallSet = AddElasticWallsToDatabase(OData, WallGrids, range(1,3), Wall_24_5000, XGrids, YGrids, ZGrids, 6*12, 'Walls - 24 - inches')
        WallSet = AddElasticWallsToDatabase(OData, WallGrids, range(3,5), Wall_18_5000, XGrids, YGrids, ZGrids, 6*12, 'Walls - 18 - inches')
    else:
        WallSet = AddElasticWallsToDatabase(OData, WallGrids, range(1,5), Wall_24_5000, XGrids, YGrids, ZGrids, 6*12, 'Walls - 24 - inches')

    #### Slabs ####
    SlabGrids = [[0,0,10,0,10,10,0,10]]

    SlabSet = AddMeshedSlabToDatabase(OData, SlabGrids, range(1,5),Slab_4_4000, XGrids, YGrids, ZGrids, 6*12, 'Slabs - 4 - inch')

    #endregion

    ##############################################################################
    #region ### Start Writing Elements to the Executible File
    ##############################################################################

    # Setting Nodes as Used
    for object in set(OData._Elements):
        object._NodeI.__setattr__('Used',True)
        object._NodeJ.__setattr__('Used',True)
        try:
            object._NodeK.__setattr__('Used',True)
            object._NodeL.__setattr__('Used',True)
            object._NodeC.__setattr__('Used',True)
        except:
            pass

    # Setting Nodes as Used in Quanrilaters
    for object in set(OData._Quadrilaterals):
        object._NodeI.__setattr__('Used',True)
        object._NodeJ.__setattr__('Used',True)
        object._NodeK.__setattr__('Used',True)
        object._NodeL.__setattr__('Used',True)

    #Writing Nodes to File
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Defining Nodes'))
    for obj in OData._Nodes:
        try:
            if obj.Used:
                OData.Executable.AddCommand(obj.CommandLine)
        except:
            continue

    #Defining Fixity
    SupportZeroLengthElements = []
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Defining Node Fixity'))
    for i in range(len(XGrids)):
        for j in range(len(YGrids)):
            node = OData.GetNodesByGrid(i,j,0,NodeType=1)[0]
            if hasattr(node, 'Used'):
                supportnode = OData.CreateNode(node.X,node.Y,node.Z,2,node.GridX,node.GridY,node.GridZ,0,_Notes='Used to Extract Reactions')
                OData.AddObject(supportnode)
                supportnode.__setattr__('Used',True)
                SupportZeroLengthElements.append(OData.AddObject(OpenSeesAPI.Model.Element.Element.ZeroLength(OData.GetFreeElementId(9,1),supportnode,node,[ElasticRigid, ElasticRigid, ElasticRigid],[1,2,3])))
                OData.AddObject(OpenSeesAPI.Model.Constraint.Fix(supportnode,[1,1,1,1,1,1]))
    Nodes = OData.GetNodesByGrid(i,j,0,NodeType=3)
    for node in Nodes:
        supportnode = OData.CreateNode(node.X,node.Y,node.Z,2,node.GridX,node.GridY,node.GridZ,0,_Notes='Used to Extract Reactions')
        OData.AddObject(supportnode)
        supportnode.__setattr__('Used',True)
        SupportZeroLengthElements.append(OData.AddObject(OpenSeesAPI.Model.Element.Element.ZeroLength(OData.GetFreeElementId(9,1),supportnode,node,[ElasticRigid, ElasticRigid, ElasticRigid],[1,2,3])))
        OData.AddObject(OpenSeesAPI.Model.Constraint.Fix(node,[1,1,1,1,1,1]))

    #Define Fixity for Diaphragm Master Nodes
    for i in range(0,len(DiaphragmNodes)):
        OData.AddObject(OpenSeesAPI.Model.Constraint.Fix(DiaphragmNodes[i],[0,0,1,1,1,0],_Notes='Fix Diaphragm Master Nodes'))

    LowerStoriesCenterNodes = []
    for i in range(1,5):
        LowerStoriesCenterNodes.append(OData.GetNodesByGrid(int(len(XGrids)/2),int(len(YGrids)/2),i)[0])

    OutputNodes = [None]+LowerStoriesCenterNodes+DiaphragmNodes

    #Defining Diaphragms
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Defining Diaphragms'))
    for i in range(5,len(ZGrids)):
        Nodes = OData.GetNodesByZCoordinate(ZGrids[i],1)+OData.GetNodesByZCoordinate(ZGrids[i],4)
        Nodes = list(filter(lambda x: hasattr(x,'Used'),Nodes))
        OData.AddObject(OpenSeesAPI.Model.Constraint.RigidDiaphragm(3,OutputNodes[i],Nodes[0:],_Notes='Rigid Diaphrams at Zgrid: %d'%i))

    #Defining Masses

    # Distribute Masses To all the nodes on the lower stories since Rigid Diaphargms are not used here
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Defining Node Mass'))
    for i in range(1,5):
        MassNodes = OData.GetNodesByZCoordinate(ZGrids[i],NodeType=1)+OData.GetNodesByZCoordinate(ZGrids[i],NodeType=4)
        MassNodes = list(filter(lambda x: x.Used if hasattr(x,'Used') else False, MassNodes))
        for node in MassNodes:
            OData.AddObject(OpenSeesAPI.Model.Node.Mass(node,[FloorMass[i]/len(MassNodes),FloorMass[i]/len(MassNodes),1e-6,1e-6,1e-6,1e-6],_Notes='Mass at GridZ: %d'%(i)))

    #Add the mass to the diaphargm nodes only
    for i in range(5,len(ZGrids)):
        RZ = FloorMass[i]*((107.*12.)**2.+(170.*12.)**2.)/12.
        OData.AddObject(OpenSeesAPI.Model.Node.Mass(OutputNodes[i],[FloorMass[i],FloorMass[i],1.e-6,1.e-6,1.e-6,RZ],_Notes='Mass at GridZ: %d'%(i)))

    #Add Rayleigh Damping to Nodes

    #Write Element from OpenSees Collector
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Writing Materials'))
    for obj in OData._Materials:
        OData.Executable.AddCommand(obj.CommandLine)

    #Write Sections from OpenSees Collector
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Writing Sections'))
    for obj in OData._Sections:
        OData.Executable.AddCommand(obj.CommandLine)

    #Write Elements from OpenSees Collector
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Writing Elements'))
    for obj in OData._Elements:
        OData.Executable.AddCommand(obj.CommandLine)

    #Write Shells from OpenSees Collector
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Writing Shells'))
    for obj in OData._Quadrilaterals:
        OData.Executable.AddCommand(obj.CommandLine)

    #Write Constraints from OpenSees Collector
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Writing Constraints'))
    for obj in OData._Constraints:
        OData.Executable.AddCommand(obj.CommandLine)

    ########################## Eigenvalue Analysis ##########################
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Eigenvalue Analysis'))

    if PushOver == True or (T1 == None and T2 == None):
        OData.AddObject(OpenSeesAPI.Analysis.Eigen(3))
        for mode in range(1,2):
            for i in range(1,len(ZGrids)):
                OData.AddObject(OpenSeesAPI.TCL.TCLScript('set EigenVector%d%d [nodeEigenvector %d %d %d]'%(mode,i,OutputNodes[i].id,mode,1)))
                OData.AddObject(OpenSeesAPI.TCL.TCLScript('puts \" EigenVector Mode:%d Story:%d $EigenVector%d%d \"'%(mode,i,mode,i)))

    #endregion
    ##############################################################################

    #region ########################## Rayleigh Damping ##########################
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Rayleigh Damping'))

    #Check To see if Eigen Value Analysis is to be overridden

    if PushOver == True or (T1 == None and T2 == None):
        # Adding Rayleigh Damping to the Mass Matrix Only
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set zeta 0.05'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set alpha0 [expr $zeta*$w1*$w2/($w1+$w2)]'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set alpha1 [expr $zeta*2.0/($w1+$w2)]'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('rayleigh $alpha0 0 $alpha1 0'))
    else:
        # Adding Rayleigh Damping to the Mass Matrix Only
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set zeta 0.05'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set w1 [expr 2*3.141592654/%f]'%T1))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set w2 [expr 2*3.141592654/%f]'%T2))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set alpha0 [expr $zeta*$w1*$w2/($w1+$w2)]'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set alpha1 [expr $zeta*2.0/($w1+$w2)]'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('rayleigh $alpha0 0 $alpha1 0'))

    #endregion

    #region ########################## Loads ##########################
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Loads'))

    # Add Loads
    Loads = []
    for i in range(1,len(ZGrids)):
        Nodes = OData.GetNodesByZCoordinate(ZGrids[i],1)
        Nodes = list(filter(lambda x: hasattr(x, 'Used'),Nodes))
        XColumnGrids = [1,2,4,6,8,9]
        YColumnGrids = [2,4,6,8]
        Nodes = list(filter(lambda x: XColumnGrids.__contains__(x.GridX),Nodes))
        Nodes = list(filter(lambda x: YColumnGrids.__contains__(x.GridY),Nodes))
        for node in Nodes:
            ApproxLoad = -1*EquivLoad[i]*g/len(Nodes)
            Loads.append(OpenSeesAPI.Model.Pattern.Load(node,[0, 0, ApproxLoad,0 ,0, 0]))

    OData.AddObject(OpenSeesAPI.Model.Pattern.Plain(100,'Linear',Loads))

    #endregion

    #region ########################## Time Series ##########################
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Time Series'))

    TimeSeriesX = OpenSeesAPI.Model.TimeSeries.Path(1,Dt, GMDataX)
    TimeSeriesY = OpenSeesAPI.Model.TimeSeries.Path(2,Dt, GMDataY)
    OData.AddObject(TimeSeriesX)
    OData.AddObject(TimeSeriesY)

    #endregion

    #region ########################## Recorders ##########################
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Recorder Setup'))

    OutputFolder = 'Results/'

    OutputNode = [OutputNodes[-1]]
    SupportNodes = OData.GetNodesByZCoordinate(0,NodeType=2)

    Displacement_X_File_Name = '%s-NodeD-X-%s.dat'%(ModelName,timestamp)
    OData.AddObject(OpenSeesAPI.Output.Recorder.Node(OutputFolder+Displacement_X_File_Name, OutputNode, [1], 'disp'))

    Displacement_Y_File_Name = '%s-NodeD-Y-%s.dat'%(ModelName,timestamp)
    OData.AddObject(OpenSeesAPI.Output.Recorder.Node(OutputFolder+Displacement_Y_File_Name, OutputNode, [2], 'disp'))

    Acceleration_X_File_Name = '%s-NodeA-X-%s.dat'%(ModelName,timestamp)
    OData.AddObject(OpenSeesAPI.Output.Recorder.Node(OutputFolder+Acceleration_X_File_Name, OutputNode, [1], 'accel','-timeSeries %d'%TimeSeriesX.id))

    Acceleration_Y_File_Name = '%s-NodeA-Y-%s.dat'%(ModelName,timestamp)
    OData.AddObject(OpenSeesAPI.Output.Recorder.Node(OutputFolder+Acceleration_Y_File_Name, OutputNode, [2], 'accel','-timeSeries %d'%TimeSeriesY.id))

    Reaction_X_File_Name = '%s-NodeReact-X-%s.dat'%(ModelName,timestamp)
    OData.AddObject(OpenSeesAPI.Output.Recorder.Node(OutputFolder+Reaction_X_File_Name, SupportNodes, [1], 'reaction'))

    Reaction_Y_File_Name = '%s-NodeReact-Y-%s.dat'%(ModelName,timestamp)
    OData.AddObject(OpenSeesAPI.Output.Recorder.Node(OutputFolder+Reaction_Y_File_Name, SupportNodes, [2], 'reaction'))

    #Record Def. At all Nodes for OpenSeesAnimation
    AllNodes = list(filter(lambda x: hasattr(x, 'Used'), OData._Nodes))
    All_Node_Disp_File_Name = '%s-AllNodeDisp-%s.dat'%(ModelName,timestamp)
    OData.AddObject(OpenSeesAPI.Output.Recorder.Node(OutputFolder+All_Node_Disp_File_Name, AllNodes, [1,2,3], 'disp'))

    #Record All Column Element Forces
    All_Column_Forces_File_Name = '%s-AllColumnForce-%s.dat'%(ModelName,timestamp)
    OData.AddObject(OpenSeesAPI.Output.Recorder.Element(OutputFolder+All_Column_Forces_File_Name,ColumnSet,'globalForce'))

    #Record All Braces Element Forces
    All_Braces_Forces_File_Name = '%s-AllBraceForce-%s.dat'%(ModelName,timestamp)
    OData.AddObject(OpenSeesAPI.Output.Recorder.Element(OutputFolder+All_Braces_Forces_File_Name,BraceSet,'globalForce'))

    ########################## Gravity Analysis ##########################
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Gravity Analysis'))

    NoOfGravitySteps = 5
    OData.AddObject(OpenSeesAPI.Analysis.Constraints.Transformation())
    OData.AddObject(OpenSeesAPI.Analysis.Numberer.RCM())
    OData.AddObject(OpenSeesAPI.Analysis.System.Mumps())
    # OData.AddObject(OpenSeesAPI.Analysis.System.BandGeneral())
    OData.AddObject(OpenSeesAPI.Analysis.Test.NormUnbalance(1e-3, 1000))
    OData.AddObject(OpenSeesAPI.Analysis.Algorithm.KrylovNewton())
    OData.AddObject(OpenSeesAPI.Analysis.Integrator.Static.LoadControl(1.0/NoOfGravitySteps,1,0.2,0.2))
    OData.AddObject(OpenSeesAPI.Analysis.Analysis.Static())
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('set ok [analyze %d]'%NoOfGravitySteps))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('if {$ok == 0} {puts "Gravity Analysis Success" } else {puts "Gravity Analysis Failed"} '))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('loadConst -time 0.0'))

    #endregion

    #region ########################## Display Results ##########################
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Display Results'))

    #endregion

    #region ########################## Pushover Analysis ##########################
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Pushover Analysis'))

    if PushOver:
        #Define Analysis
        OData.AddObject(OpenSeesAPI.Analysis.Constraints.Transformation())
        OData.AddObject(OpenSeesAPI.Analysis.Numberer.RCM())
        OData.AddObject(OpenSeesAPI.Analysis.System.Mumps())
        # OData.AddObject(OpenSeesAPI.Analysis.Test.NormUnbalance(1e-6, 200, 5))
        OData.AddObject(OpenSeesAPI.Analysis.Test.EnergyIncr(1e-4, 1000, 5))
        OData.AddObject(OpenSeesAPI.Analysis.Algorithm.NewtonLineSearch())
        ControlNode = OutputNodes[-1]
        OData.AddObject(OpenSeesAPI.Analysis.Integrator.Static.DisplacementControl(ControlNode, 1, 0.1))
        OData.AddObject(OpenSeesAPI.Analysis.Analysis.Static())

        #Load Pattern
        Loads = []
        for i in range(1,len(ZGrids)):
            Nodes = OData.GetNodesByZCoordinate(ZGrids[i],1)
            Nodes = list(filter(lambda x: hasattr(x,'Used'),Nodes)) #Filter for used nodes
            for node in Nodes:
                Loads.append(OpenSeesAPI.TCL.TCLScript('load %d $EigenVector%d%d 0 0 0 0 0'%(node.id, 1,i)))
        OData.AddObject(OpenSeesAPI.Model.Pattern.Plain(200,'Linear', Loads))

        #Run Analysis
        MaxU = ZGrids[-1]*0.20
        MaxIteration = 200
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set ok 0;'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set MaxU %f;'%MaxU))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set MaxStep %d;'%MaxIteration))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set step 0;'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set currentDisp 0;'))

        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set Yielded 0;'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set Stiffness 0;'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set PreviousStiffness 0;'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set PreviousReaction 0;'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set PreviousDisp 0;'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set YieldReaction 0;'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set TotalReaction 0;'))

        OData.AddObject(OpenSeesAPI.TCL.TCLScript('while {$ok == 0 & $step < $MaxStep & $currentDisp < $MaxU} {'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set ok [analyze 1]'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set currentDisp [nodeDisp %d 1]'%ControlNode.id))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('puts "Running Push Over Step: $step"'))

        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set PreviousStiffness [expr $Stiffness];'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set PreviousReaction $TotalReaction;'))

        #Find Out When The Structure Yields and then Stop analysis at 80% of the Yield Strength
        # GroundFloorColumns=filter(lambda x: SupportNodes.__contains__(x._NodeI),OData._Elements)
        for i in range(len(SupportZeroLengthElements)):
            # OData.AddObject(OpenSeesAPI.TCL.TCLScript('puts [lindex [eleResponse %d forces] 0] ;'%(SupportZeroLengthElements[i].id)))
            OData.AddObject(OpenSeesAPI.TCL.TCLScript('set NodeReaction%d [lindex [eleResponse %d forces] 0];'%(i,SupportZeroLengthElements[i].id)))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set TotalReaction [expr %s];'%(''.join(map(lambda x: '$NodeReaction%d+'%x,range(0,len(SupportZeroLengthElements))))[:-1])))

        #NodeReaction is not working
        # for i in range(len(SupportNodes)):
        #     OData.AddObject(OpenSeesAPI.TCL.TCLScript('set NodeReaction%d [nodeReaction %d 1];'%(i,SupportNodes[i].id)))
        # OData.AddObject(OpenSeesAPI.TCL.TCLScript('set TotalReaction [expr %s];'%(''.join(map(lambda x: '$NodeReaction%d+'%x,range(0,len(SupportNodes))))[:-1])))

        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set Stiffness [expr abs(($TotalReaction-$PreviousReaction)/($currentDisp-$PreviousDisp))];'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('puts $Stiffness;'))
        #Check If 60 Percent Yield Reaction Reached
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('if {[expr 0.6*abs($YieldReaction)] > [expr abs($TotalReaction)] & $Yielded == 1} {break};'))

        #Trigger Yielding
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('if {$step != 0 & [expr abs(($Stiffness-$PreviousStiffness)/$Stiffness)] > 1e-3} {'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set Yielded 1;'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set YieldReaction [expr abs($TotalReaction)]\n};'))

        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set step [expr $step+1]'))

        OData.AddObject(OpenSeesAPI.TCL.TCLScript('}'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('if {$ok == 0} {puts "Analysis Success"} else { puts "Analysis Failed" }'))
    #endregion

    #region ########################## Time History Analysis ##########################
    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Time History Analysis'))

    if not(PushOver):
        #Define Analysis
        OData.AddObject(OpenSeesAPI.Analysis.Constraints.Transformation())
        OData.AddObject(OpenSeesAPI.Analysis.Numberer.RCM())
        # OData.AddObject(OpenSeesAPI.Analysis.System.BandGeneral())
        OData.AddObject(OpenSeesAPI.Analysis.System.Mumps(Optional='-ICNTL 30'))
        # OData.AddObject(OpenSeesAPI.Analysis.Test.NormUnbalance(1e-6, 200, 5))#EnergyIncr(1e-6, 10))
        OData.AddObject(OpenSeesAPI.Analysis.Test.EnergyIncr(1.0e-4, 1000, pFlag=0))
        OData.AddObject(OpenSeesAPI.Analysis.Algorithm.NewtonLineSearch())
        OData.AddObject(OpenSeesAPI.Analysis.Integrator.Transient.Newmark(0.5,0.25))
        OData.AddObject(OpenSeesAPI.Analysis.Analysis.Transient())

        #Load Pattern
        OData.AddObject(OpenSeesAPI.Model.Pattern.UniformExcitation(400,1,TimeSeriesX))
        OData.AddObject(OpenSeesAPI.Model.Pattern.UniformExcitation(401,2,TimeSeriesY))

        #Run Analysis
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set ok 0;'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set Nsteps %d;'%len(GMDataX)))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set step 0;'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('while {$ok == 0 & $step < [expr $Nsteps +1]} {'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('puts "Running Time History Step: $step"'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set ok [analyze 1 %f]'%(Dt)))
        def SolutionAlgorithim(OData, Dt, Tol, Steps):
            #Insert within the While loop, make sure parameter "ok" is defined
            OData.AddObject(OpenSeesAPI.TCL.TCLScript('if {$ok != 0} {'))
            OData.AddObject(OpenSeesAPI.TCL.TCLScript('puts "Trying Lower Dt: %f and Tol: %f ... "'%(Dt,Tol)))
            OData.AddObject(OpenSeesAPI.TCL.TCLScript('puts "Trying Newton Line Search ... "'))
            OData.AddObject(OpenSeesAPI.Analysis.Test.EnergyIncr(Tol,1000,0))
            OData.AddObject(OpenSeesAPI.Analysis.Algorithm.NewtonLineSearch(Tolerance=0.8))
            OData.AddObject(OpenSeesAPI.TCL.TCLScript('set ok [analyze %d %f ]'%(Steps,Dt)))
            OData.AddObject(OpenSeesAPI.TCL.TCLScript('}'))

            OData.AddObject(OpenSeesAPI.TCL.TCLScript('if {$ok != 0} {'))
            OData.AddObject(OpenSeesAPI.TCL.TCLScript('puts "Trying Newton with Initial Tangent ... "'))
            OData.AddObject(OpenSeesAPI.Analysis.Test.NormDispIncr(Tol,1000,0))
            OData.AddObject(OpenSeesAPI.Analysis.Algorithm.Newton(Initial=True))
            OData.AddObject(OpenSeesAPI.TCL.TCLScript('set ok [analyze %d %f ]'%(Steps,Dt)))
            OData.AddObject(OpenSeesAPI.TCL.TCLScript('}'))

            OData.AddObject(OpenSeesAPI.TCL.TCLScript('if {$ok != 0} {'))
            OData.AddObject(OpenSeesAPI.TCL.TCLScript('puts "Trying Broyden ... "'))
            OData.AddObject(OpenSeesAPI.Analysis.Test.EnergyIncr(Tol,1000,0))
            OData.AddObject(OpenSeesAPI.Analysis.Algorithm.Broyden(8))
            OData.AddObject(OpenSeesAPI.TCL.TCLScript('set ok [analyze %d %f ]'%(Steps,Dt)))
            OData.AddObject(OpenSeesAPI.TCL.TCLScript('}'))

            OData.AddObject(OpenSeesAPI.TCL.TCLScript('if {$ok != 0} {'))
            OData.AddObject(OpenSeesAPI.TCL.TCLScript('puts "Trying KrylovNewton ... "'))
            OData.AddObject(OpenSeesAPI.Analysis.Test.EnergyIncr(Tol,1000,0))
            OData.AddObject(OpenSeesAPI.Analysis.Algorithm.KrylovNewton())
            OData.AddObject(OpenSeesAPI.TCL.TCLScript('set ok [analyze %d %f ]'%(Steps,Dt)))
            OData.AddObject(OpenSeesAPI.TCL.TCLScript('}'))
        SolutionAlgorithim(OData,Dt/5,1e-6,5)
        SolutionAlgorithim(OData,Dt/10,1e-5,10)
        SolutionAlgorithim(OData,Dt/20,1e-4,20)
        SolutionAlgorithim(OData,Dt/40,1e-5,40)

        OData.AddObject(OpenSeesAPI.Analysis.Test.EnergyIncr(1.0e-4, 1000, pFlag=0))
        OData.AddObject(OpenSeesAPI.Analysis.Algorithm.NewtonLineSearch())

        OData.AddObject(OpenSeesAPI.TCL.TCLScript('set step [expr $step+1]'))
        OData.AddObject(OpenSeesAPI.TCL.TCLScript('}'))

        OData.AddObject(OpenSeesAPI.TCL.TCLScript('if {$ok == 0} {puts "Analysis Success"} else { puts "Analysis Failed" }'))

    #endregion

    #region ########################## Close File ##########################

    OData.AddObject(OpenSeesAPI.TCL.CodeTitle('Close File'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('wipe al b l;'))
    OData.AddObject(OpenSeesAPI.TCL.TCLScript('puts "Models Run Complete";'))

    #endregion

    ##############################################################################
    ### Start Running OpenSees File
    ##############################################################################

    #region ########################## Run OpenSees Script ##########################
    OData.Executable.StartAnalysis(SuppressOutput=SupressOutput)

    #endregion

    #region ########################## Import Output Files ##########################
    DisplX = np.loadtxt(FileLocation+OutputFolder+Displacement_X_File_Name)[NoOfGravitySteps:,:]
    DisplY = np.loadtxt(FileLocation+OutputFolder+Displacement_Y_File_Name)[NoOfGravitySteps:,:]

    AccX = np.loadtxt(FileLocation+OutputFolder+Acceleration_X_File_Name)[NoOfGravitySteps:,:]
    AccY = np.loadtxt(FileLocation+OutputFolder+Acceleration_Y_File_Name)[NoOfGravitySteps:,:]

    ReacX = np.loadtxt(FileLocation+OutputFolder+Reaction_X_File_Name)[NoOfGravitySteps:,:]
    ReacY = np.loadtxt(FileLocation+OutputFolder+Reaction_Y_File_Name)[NoOfGravitySteps:,:]

    AllNodeDisp = np.loadtxt(FileLocation+OutputFolder+All_Node_Disp_File_Name)[NoOfGravitySteps:,:]

    AllColumnForces = np.loadtxt(FileLocation+OutputFolder+All_Column_Forces_File_Name)[NoOfGravitySteps:,:]
    AllBraceForces = np.loadtxt(FileLocation+OutputFolder+All_Braces_Forces_File_Name)[NoOfGravitySteps:,:]

    LogLines = open(FileLocation+OData.Executable.LogFileName,'r').readlines()
    #Get Whether Analysis is Successfull
    AnalysisSuccess = LogLines.__contains__('Analysis Success\n')
    GravitySuccess = LogLines.__contains__('Gravity Analysis Success\n')

    if T1 == None and T2 == None:
        #Get Period
        for line in LogLines:
            if line.startswith('T1 = '):
                T1 = float(line.split()[2])
            if line.startswith('T2 = '):
                T2 = float(line.split()[2])
            if line.startswith('T3 = '):
                T3 = float(line.split()[2])

    #Delete Output Files and Input Files
    try:
        os.remove(FileLocation+OutputFolder+Displacement_X_File_Name)
        os.remove(FileLocation+OutputFolder+Displacement_Y_File_Name)
        os.remove(FileLocation+OutputFolder+Acceleration_X_File_Name)
        os.remove(FileLocation+OutputFolder+Acceleration_Y_File_Name)
        os.remove(FileLocation+OutputFolder+Reaction_X_File_Name)
        os.remove(FileLocation+OutputFolder+Reaction_Y_File_Name)
        os.remove(FileLocation+OutputFolder+All_Column_Forces_File_Name)
        os.remove(FileLocation+OutputFolder+All_Braces_Forces_File_Name)
        os.remove(FileLocation+OutputFolder+All_Node_Disp_File_Name)

        OData.Executable.DeleteLogFile()
        # OData.Executable.DeleteTCLFile()
    except:
        pass

    #endregion

    #region ########################## Processing Output ##########################

    class Output():
        pass
    O = Output()

    #Saving Column and Brace Force Output
    ColumnBraceForceDictionaryList = []
    for i in range(len(ColumnSet)):
        temp = {}
        id = ColumnSet[i].id
        temp['id']=id
        temp['Fx']=AllColumnForces[:,1+(i*12)]
        temp['Fy']=AllColumnForces[:,2+(i*12)]
        temp['Fz']=AllColumnForces[:,3+(i*12)]
        temp['Mx']=AllColumnForces[:,4+(i*12)]
        temp['My']=AllColumnForces[:,5+(i*12)]
        temp['Mz']=AllColumnForces[:,6+(i*12)]
        ColumnBraceForceDictionaryList.append(temp)
    for i in range(len(BraceSet)):
        temp = {}
        id = BraceSet[i].id
        temp['id']=id
        temp['Fx']=AllBraceForces[:,1+(i*12)]
        temp['Fy']=AllBraceForces[:,2+(i*12)]
        temp['Fz']=AllBraceForces[:,3+(i*12)]
        temp['Mx']=AllBraceForces[:,4+(i*12)]
        temp['My']=AllBraceForces[:,5+(i*12)]
        temp['Mz']=AllBraceForces[:,6+(i*12)]
        ColumnBraceForceDictionaryList.append(temp)

    #Calculating ShearStoryForces
    FXStoryShear = []
    FYStoryShear = []
    for i in range(len(ZGrids)-1):
        Elements = []
        Elements.extend(map(lambda x: x.id if x._NodeI.GridZ == i else None, ColumnSet))
        Elements.extend(map(lambda x: x.id if x._NodeI.GridZ == i else None, BraceSet))
        Elements = list(filter(lambda x: x != None, Elements))
        FxShears = np.array(list(filter(lambda x: x != None, map(lambda x: x['Fx'] if Elements.__contains__(x['id']) else None, ColumnBraceForceDictionaryList))))
        FyShears = np.array(list(filter(lambda x: x != None, map(lambda x: x['Fy'] if Elements.__contains__(x['id']) else None, ColumnBraceForceDictionaryList))))

        FXStoryShear.append(np.sum(FxShears,0))
        FYStoryShear.append(np.sum(FyShears,0))


    if PushOver:
        O.t = np.arange(0,len(AccX[:,0]))
        O.agX = np.zeros(len(AccX[:,0]))
        O.agY = np.zeros(len(AccX[:,0]))
        O.aX = np.zeros(len(AccX[:,0]))
        O.aY = np.zeros(len(AccX[:,0]))
        O.fsX = -1*np.array(map(lambda x: sum(x),ReacX[:,1:]))
        O.fsY = -1*np.array(map(lambda x: sum(x),ReacY[:,1:]))
        O.uX = DisplX[:,1]/max(ZGrids)
        O.uY = DisplX[:,1]/max(ZGrids)
        O.OData = OData
        O.ColumnBraceForcesDictList = ColumnBraceForceDictionaryList
    else:
        DataPoints = len(GMDataX)
        O.t = AccX[0:DataPoints,0]
        O.agX = GMDataX[:]/g
        O.agY = GMDataY[:]/g
        O.aX = AccX[0:DataPoints,1]
        O.aY = AccY[0:DataPoints,1]
        O.fsX = -1*np.array(map(lambda x: sum(x),ReacX[0:DataPoints,1:]))
        O.fsY = -1*np.array(map(lambda x: sum(x),ReacY[0:DataPoints,1:]))
        O.uX = DisplX[0:DataPoints,1]/max(ZGrids)
        O.uY = DisplY[0:DataPoints,1]/max(ZGrids)
        O.OData = OData
        O.ColumnBraceForcesDictList = ColumnBraceForceDictionaryList

    O.NodesDispDict = {}
    for i in range(len(AllNodes)):
        O.NodesDispDict[AllNodes[i].id] = [AllNodeDisp[:,1+(i)*3],AllNodeDisp[:,2+(i)*3],AllNodeDisp[:,3+(i)*3]]

    O.HingeRotationDict = {}

    InterStoryDriftsX = []
    InterStoryDriftsY = []
    #Compute Max Interstory Drift
    for i in range(1,len(ZGrids)):
        if i != 1:
            RelDispX = np.array(O.NodesDispDict[OutputNodes[i].id][0])-np.array(O.NodesDispDict[OutputNodes[i-1].id][0])
            RelDispY = np.array(O.NodesDispDict[OutputNodes[i].id][1])-np.array(O.NodesDispDict[OutputNodes[i-1].id][1])
        else:
            RelDispX = np.array(O.NodesDispDict[OutputNodes[i].id][0])
            RelDispY = np.array(O.NodesDispDict[OutputNodes[i].id][1])
        InterStoryDriftsX.append(max(abs(RelDispX))/(ZGrids[i]-ZGrids[i-1]))
        InterStoryDriftsY.append(max(abs(RelDispY))/(ZGrids[i]-ZGrids[i-1]))

    class Output():
        def __init__(self):
            self.AnalysisSuccess = AnalysisSuccess
            self.GravitySuccess = GravitySuccess

            self.O = O
            self.T1 = T1
            self.T2 = T2

            self.InterStoryDriftX = InterStoryDriftsX
            self.InterStoryDriftY = InterStoryDriftsY
            self.MaxInterStoryDrift = max(InterStoryDriftsX+InterStoryDriftsY)
            self.FXStoryShear = FXStoryShear
            self.FYStoryShear = FYStoryShear

    #endregion

    return Output()


Output = TBI_BRB_A(GMData*386.4,GMData*386.4, Dt, T1=5.25, T2=1.48, PushOver=False, SupressOutput=False, Viewer=True, Animation=False, OpenSeesCommand='OpenSeesSP', TestingModeOff=False)

import matplotlib.pylab as plt
import numpy as np

plt.figure()
plt.title('TBI-BRB Structure')
plt.xlabel('Story Shear, kips')
plt.ylabel('Story')
plt.plot(map(lambda x: max(abs(x)), Output.FXStoryShear), range(len(Output.FXStoryShear)),'-',color='#000000', linewidth=1.5, label='X')
plt.plot(map(lambda x: max(abs(x)), Output.FYStoryShear), range(len(Output.FXStoryShear)),'--',color='#000000', linewidth=1.5, label='Y')
plt.legend()
plt.savefig('Figures/Test.png',dpi=600)

plt.figure()
plt.title('TBI-BRB Structure')
plt.xlabel('Interstory Drift, %')
plt.ylabel('Story')
plt.plot(np.array(Output.InterStoryDriftX)*100, range(len(Output.InterStoryDriftX)),'-',color='#000000', linewidth=1.5, label='X')
plt.plot(np.array(Output.InterStoryDriftY)*100, range(len(Output.InterStoryDriftY)),'--',color='#000000', linewidth=1.5, label='Y')
plt.legend()

plt.savefig('Figures/Test2.png',dpi=600)
plt.show()