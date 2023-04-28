WIDTH = 890
HEIGHT = 980
INFINITY = 999999

COLOR = {
    "BLACK": (255, 255, 255),
    "WHITE": (0, 0, 0),
}

INF = 9999999.99
MAP_POINTS = [(358, 164), (438, 74), (758, 366), (386, 329), (350, 37),
              (109, 339), (66, 590), (34, 700), (229, 599), (382, 650),
              (378, 698), (212, 692), (212, 663), (473, 709), (490, 622),
              (497, 539), (454, 530), (446, 469), (406, 467), (385, 480),
              (376, 357), (391, 362), (427, 335), (432, 372), (390, 387),
              (393, 430), (440, 423), (478, 454), (485, 407), (470, 361),
              (457, 330), (447, 306), (528, 395), (497, 276), (284, 119),
              (350, 174), (362, 146), (305, 86), (442, 170), (490, 187),
              (530, 263), (585, 380), (513, 495), (555, 514), (552, 540),
              (610, 562), (544, 576), (497, 577), (532, 630), (524, 663),
              (489, 654), (580, 680), (513, 716), (572, 727), (585, 646),
              (703, 691), (713, 662), (669, 755), (633, 451), (798, 581),
              (824, 597), (814, 640), (781, 734), (655, 371), (703, 420),
              (690, 441), (701, 459), (738, 497), (764, 475), (841, 549),
              (777, 542), (741, 551), (733, 582), (611, 544), (649, 575),
              (505, 527), (163, 697), (165, 668), (130, 666), (130, 624),
              (187, 625), (188, 663), (248, 696), (254, 646), (243, 748),
              (247, 772), (270, 749), (436, 702), (427, 746), (451, 705),
              (709, 568), (202, 241), (156, 235), (247, 181), (230, 169),
              (252, 80), (73, 274), (113, 274), (223, 48), (302, 137),
              (332, 115), (412, 159), (642, 309), (736, 227), (768, 268),
              (666, 333), (654, 300), (675, 322), (698, 345), (751, 290),
              (709, 375), (726, 361), (773, 402), (791, 389), (808, 397),
              (823, 408), (845, 383), (831, 370), (817, 357), (803, 344),
              (788, 332), (775, 376), (738, 347), (766, 315), (778, 299),
              (795, 306), (406, 178), (531, 180), (575, 145), (670, 232),
              (681, 221), (692, 237), (682, 246), (540, 192), (578, 161),
              (513, 158), (528, 145), (537, 138), (543, 130), (551, 123),
              (561, 114), (572, 125), (564, 135), (557, 143), (549, 153),
              (540, 160), (487, 131), (507, 115), (531, 101), (519, 132),
              (539, 116), (466, 104), (531, 49), (559, 23), (576, 41),
              (545, 64), (586, 53), (552, 77), (618, 32), (601, 16), (626, 43),
              (650, 18), (633, 54), (588, 94), (617, 88), (626, 110),
              (663, 83), (650, 67), (707, 15), (672, 92), (726, 45), (687, 97),
              (697, 107), (761, 54), (771, 67), (741, 95), (759, 209),
              (816, 262), (797, 282), (831, 276), (808, 301), (735, 183),
              (716, 198), (724, 168), (695, 195), (741, 156), (706, 148),
              (691, 163), (791, 136), (812, 162), (783, 186), (760, 170),
              (839, 239), (810, 117), (825, 137), (770, 113), (617, 737),
              (80, 701), (73, 713), (127, 722), (135, 700), (464, 769),
              (437, 764), (486, 773), (687, 771), (704, 758), (686, 653),
              (750, 679), (767, 579), (765, 595), (494, 508), (512, 509),
              (532, 506), (452, 507), (475, 475), (649, 557), (718, 548),
              (616, 278), (601, 261), (549, 204), (560, 197), (611, 253),
              (671, 485), (694, 562), (731, 610), (446, 723), (623, 719),
              (521, 676), (534, 680), (560, 640), (568, 619), (556, 656),
              (66, 726)]

PATHS = [((358, 164), (350, 174)), ((358, 164), (362, 146)),
         ((358, 164), (406, 178)), ((738, 347), (758, 366)),
         ((758, 366), (775, 376)), ((775, 376), (803, 344)),
         ((788, 332), (758, 366)), ((466, 104), (438, 74)),
         ((642, 309), (654, 300)), ((666, 333), (675, 322)),
         ((406, 178), (442, 170)), ((561, 114), (572, 125)),
         ((561, 114), (551, 123)), ((551, 123), (543, 130)),
         ((543, 130), (537, 138)), ((537, 138), (528, 145)),
         ((528, 145), (540, 160)), ((537, 138), (549, 153)),
         ((543, 130), (557, 143)), ((551, 123), (564, 135)),
         ((572, 125), (564, 135)), ((564, 135), (557, 143)),
         ((557, 143), (549, 153)), ((549, 153), (540, 160)),
         ((223, 48), (252, 80)), ((252, 80), (230, 169)),
         ((230, 169), (247, 181)), ((247, 181), (284, 119)),
         ((284, 119), (305, 86)), ((305, 86), (350, 37)),
         ((305, 86), (332, 115)), ((284, 119), (302, 137)),
         ((302, 137), (350, 174)), ((332, 115), (362, 146)),
         ((362, 146), (412, 159)), ((412, 159), (442, 170)),
         ((442, 170), (490, 187)), ((412, 159), (406, 178)),
         ((350, 174), (497, 276)), ((497, 276), (530, 263)),
         ((530, 263), (490, 187)), ((247, 181), (202, 241)),
         ((202, 241), (156, 235)), ((156, 235), (73, 274)),
         ((73, 274), (113, 274)), ((202, 241), (109, 339)),
         ((109, 339), (66, 590)), ((66, 590), (229, 599)),
         ((66, 590), (34, 700)),
         ((34, 700), (80, 701)), ((80, 701), (135, 700)),
         ((135, 700), (127, 722)), ((127, 722), (73, 713)),
         ((73, 713), (80, 701)), ((73, 713), (66, 726)),
         ((66, 726), (34, 700)), ((135, 700), (163, 697)),
         ((163, 697), (165, 668)), ((165, 668), (130, 666)),
         ((130, 666), (130, 624)), ((130, 624), (187, 625)),
         ((187, 625), (188, 663)), ((188, 663), (165, 668)),
         ((188, 663), (212, 663)), ((212, 663), (212, 692)),
         ((212, 692), (163, 697)), ((212, 692), (248, 696)),
         ((248, 696), (254, 646)), ((243, 748), (248, 696)),
         ((243, 748), (247, 772)), ((243, 748), (270, 749)),
         ((248, 696), (378, 698)), ((378, 698), (382, 650)),
         ((378, 698), (382, 650)), ((382, 650), (229, 599)),
         ((382, 650), (490, 622)), ((490, 622), (497, 577)),
         ((497, 577), (497, 539)), ((497, 539), (454, 530)),
         ((454, 530), (385, 480)), ((385, 480), (406, 467)),
         ((406, 467), (393, 430)), ((393, 430), (390, 387)),
         ((391, 362), (390, 387)), ((391, 362), (376, 357)),
         ((385, 480), (376, 357)), ((376, 357), (386, 329)),
         ((386, 329), (447, 306)), ((447, 306), (457, 330)),
         ((457, 330), (427, 335)), ((427, 335), (432, 372)),
         ((432, 372), (390, 387)), ((391, 362), (427, 335)),
         ((432, 372), (470, 361)), ((470, 361), (457, 330)),
         ((470, 361), (485, 407)), ((432, 372), (440, 423)),
         ((440, 423), (393, 430)), ((440, 423), (485, 407)),
         ((440, 423), (446, 469)), ((406, 467), (446, 469)),
         ((446, 469), (478, 454)), ((478, 454), (485, 407)),
         ((485, 407), (528, 395)), ((528, 395), (497, 276)),
         ((446, 469), (454, 530)), ((454, 530), (475, 475)),
         ((494, 508), (505, 527)), ((505, 527), (512, 509)),
         ((512, 509), (532, 506)), ((513, 495), (532, 506)),
         ((513, 495), (528, 395)), ((528, 395), (585, 380)),
         ((585, 380), (530, 263)), ((585, 380), (555, 514)),
         ((555, 514), (532, 506)), ((555, 514), (552, 540)),
         ((552, 540), (505, 527)), ((552, 540), (544, 576)),
         ((544, 576), (497, 577)), ((544, 576), (532, 630)),
         ((532, 630), (490, 622)), ((490, 622), (489, 654)),
         ((489, 654), (524, 663)), ((524, 663), (532, 630)),
         ((489, 654), (473, 709)), ((473, 709), (451, 705)),
         ((451, 705), (446, 723)), ((451, 705), (436, 702)),
         ((436, 702), (378, 698)), ((427, 746), (436, 702)),
         ((473, 709), (513, 716)), ((513, 716), (521, 676)),
         ((521, 676), (524, 663)), ((521, 676), (534, 680)),
         ((473, 709), (464, 769)), ((464, 769), (437, 764)),
         ((464, 769), (486, 773)), ((513, 716), (572, 727)),
         ((572, 727), (617, 737)), ((617, 737), (623, 719)),
         ((572, 727), (580, 680)), ((580, 680), (524, 663)),
         ((580, 680), (585, 646)), ((585, 646), (560, 640)),
         ((560, 640), (556, 656)), ((560, 640), (532, 630)),
         ((560, 640), (568, 619)), ((585, 646), (703, 691)),
         ((703, 691), (713, 662)), ((713, 662), (686, 653)),
         ((713, 662), (750, 679)), ((703, 691), (669, 755)),
         ((669, 755), (617, 737)), ((669, 755), (687, 771)),
         ((687, 771), (704, 758)), ((703, 691), (781, 734)),
         ((814, 640), (781, 734)), ((814, 640), (824, 597)),
         ((814, 640), (731, 610)), ((731, 610), (713, 662)),
         ((731, 610), (649, 575)), ((649, 575), (649, 557)),
         ((649, 557), (611, 544)), ((611, 544), (610, 562)),
         ((610, 562), (552, 540)), ((610, 562), (585, 646)),
         ((610, 562), (649, 575)), ((733, 582), (765, 595)),
         ((765, 595), (767, 579)), ((741, 551), (767, 579)),
         ((741, 551), (798, 581)), ((824, 597), (841, 549)),
         ((841, 549), (777, 542)), ((633, 451), (611, 544)),
         ((633, 451), (585, 380)), ((633, 451), (741, 551)),
         ((741, 551), (733, 582)), ((733, 582), (709, 568)),
         ((709, 568), (718, 548)), ((709, 568), (694, 562)),
         ((671, 485), (701, 459)), ((701, 459), (690, 441)),
         ((690, 441), (703, 420)), ((701, 459), (738, 497)),
         ((738, 497), (764, 475)), ((764, 475), (703, 420)),
         ((703, 420), (655, 371)), ((490, 187), (655, 371)),
         ((655, 371), (633, 451)), ((350, 37), (490, 187)),
         ((709, 375), (666, 333)), ((666, 333), (642, 309)),
         ((642, 309), (616, 278)), ((616, 278), (601, 261)),
         ((601, 261), (611, 253)), ((611, 253), (560, 197)),
         ((560, 197), (549, 204)), ((549, 204), (601, 261)),
         ((549, 204), (540, 192)), ((540, 192), (531, 180)),
         ((540, 192), (578, 161)), ((531, 180), (575, 145)),
         ((575, 145), (670, 232)), ((670, 232), (681, 221)),
         ((681, 221), (692, 237)), ((692, 237), (682, 246)),
         ((682, 246), (670, 232)), ((531, 180), (513, 158)),
         ((513, 158), (528, 145)), ((487, 131), (513, 158)),
         ((487, 131), (507, 115)), ((507, 115), (519, 132)),
         ((519, 132), (539, 116)), ((507, 115), (531, 101)),
         ((487, 131), (466, 104)), ((466, 104), (531, 49)),
         ((531, 49), (559, 23)), ((531, 49), (545, 64)), ((545, 64), (576,
                                                                      41)),
         ((559, 23), (576, 41)), ((576, 41), (601, 16)), ((601, 16), (618,
                                                                      32)),
         ((618, 32), (586, 53)), ((586, 53), (576, 41)), ((552, 77), (586,
                                                                      53)),
         ((618, 32), (626, 43)), ((626, 43), (650, 18)), ((626, 43), (633,
                                                                      54)),
         ((633, 54), (588, 94)), ((633, 54), (650, 67)), ((650, 67), (617,
                                                                      88)),
         ((650, 67), (663, 83)), ((650, 67), (707, 15)), ((663, 83), (626,
                                                                      110)),
         ((663, 83), (672, 92)), ((672, 92), (726, 45)), ((672, 92), (687,
                                                                      97)),
         ((687, 97), (697, 107)), ((697, 107), (761, 54)),
         ((761, 54), (771, 67)), ((771, 67), (741, 95)),
         ((825, 137), (812, 162)), ((812, 162), (791, 136)),
         ((791, 136), (810, 117)), ((791, 136), (770, 113)),
         ((691, 163), (706, 148)), ((706, 148), (724, 168)),
         ((724, 168), (741, 156)), ((741, 156), (760, 170)),
         ((760, 170), (735, 183)), ((724, 168), (735, 183)),
         ((724, 168), (695, 195)), ((716, 198), (736, 227)),
         ((736, 227), (759, 209)), ((759, 209), (735, 183)),
         ((735, 183), (716, 198)), ((760, 170), (783, 186)),
         ((783, 186), (759, 209)), ((759, 209), (816, 262)),
         ((816, 262), (839, 239)), ((839, 239), (783, 186)),
         ((736, 227), (768, 268)), ((736, 227), (654, 300)),
         ((654, 300), (675, 322)), ((675, 322), (698, 345)),
         ((698, 345), (751, 290)), ((816, 262), (797, 282)),
         ((831, 276), (808, 301)), ((795, 306), (778, 299)),
         ((778, 299), (766, 315)), ((766, 315), (788, 332)),
         ((788, 332), (803, 344)), ((803, 344), (817, 357)),
         ((817, 357), (831, 370)), ((831, 370), (845, 383)),
         ((845, 383), (823, 408)), ((823, 408), (808, 397)),
         ((808, 397), (831, 370)), ((808, 397), (791, 389)),
         ((791, 389), (817, 357)), ((791, 389), (773, 402)),
         ((773, 402), (726, 361)), ((726, 361), (738, 347)),
         ((738, 347), (766, 315))]

ROADS = [((781, 733), (813, 640)), ((813, 640), (822, 599)),
         ((822, 599), (840, 551)), ((840, 551), (837, 533)),
         ((837, 533), (756, 476)), ((756, 476), (701, 420)),
         ((701, 420), (653, 374)), ((653, 374), (631, 450)),
         ((631, 450), (656, 490)), ((656, 490), (742, 551)),
         ((742, 551), (822, 599)), ((631, 450), (608, 560)),
         ((608, 560), (732, 612)), ((732, 612), (813, 640)),
         ((631, 450), (586, 380)), ((586, 380), (530, 262)),
         ((530, 262), (490, 181)), ((490, 181), (653, 374)),
         ((490, 181), (366, 147)), ((366, 147), (345, 176)),
         ((345, 176), (405, 222)), ((405, 222), (479, 251)),
         ((479, 251), (494, 278)), ((494, 278), (530, 262)),
         ((494, 278), (531, 395)), ((531, 395), (586, 380)),
         ((531, 395), (485, 409)), ((586, 380), (555, 516)),
         ((555, 516), (551, 541)), ((551, 541), (608, 560)),
         ((555, 516), (512, 492)), ((512, 492), (531, 395)),
         ((551, 541), (504, 529)), ((551, 541), (544, 574)),
         ((544, 574), (497, 576)), ((497, 576), (489, 622)),
         ((489, 622), (440, 648)), ((440, 648), (380, 647)),
         ((380, 647), (298, 635)), ((298, 635), (258, 619)),
         ((258, 619), (226, 598)), ((226, 598), (74, 587)),
         ((345, 176), (285, 122)), ((285, 122), (255, 185)),
         ((255, 185), (150, 308)), ((150, 308), (110, 352)),
         ((110, 352), (74, 587)), ((781, 733), (700, 690)),
         ((700, 690), (653, 666)), ((653, 666), (586, 651)),
         ((586, 651), (608, 560)), ((586, 651), (532, 630)),
         ((532, 630), (489, 622)), ((544, 574), (532, 630)),
         ((700, 690), (714, 661)), ((714, 661), (732, 612)),
         ((781, 733), (839, 745)), ((781, 733), (765, 769)),
         ((700, 690), (671, 750)), ((671, 750), (570, 727)),
         ((570, 727), (586, 651)), ((532, 630), (514, 711)),
         ((514, 711), (570, 727)), ((514, 711), (474, 706)),
         ((474, 706), (489, 622)), ((474, 706), (379, 690)),
         ((379, 690), (380, 647)), ((379, 690), (374, 761)),
         ((474, 706), (463, 763)), ((379, 690), (248, 691)),
         ((248, 691), (254, 653)), ((248, 691), (208, 690)),
         ((208, 690), (209, 766)), ((208, 690), (136, 695)),
         ((136, 695), (81, 701)), ((81, 701), (35, 699)),
         ((35, 699), (74, 587)), ((81, 701), (69, 722)), ((69, 722), (35,
                                                                      699)),
         ((69, 722), (72, 750)), ((72, 750), (66, 767)),
         ((285, 122), (306, 87)), ((306, 87), (354, 44)),
         ((354, 44), (402, 90)), ((402, 90), (490, 181)),
         ((306, 87), (366, 147)), ((354, 44), (305, 4)), ((305, 4), (306, 87))]

POINTS = [
    (781, 733),
    (700, 690),
    (653, 666),
    (586, 651),
    (532, 630),
    (489, 622),
    (440, 648),
    (380, 647),
    (379, 690),
    (248, 691),
    (208, 690),
    (136, 695),
    (81, 701),
]
# road's width to show on map
ROAD_WIDTH = 5

# point's circle diameter to show on map
POINT_DIAMETER = 8

# distance to consider a position is near to a road
MIN_DIST_ROAD = 20

# distance to consider a position is near to another position
MIN_DIST_POINT = 20

# Cirlce point's radius
POINT_RADIUS = 5