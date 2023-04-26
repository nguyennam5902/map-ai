WIDTH = 852
HEIGHT = 780

COLOR = {
    "BLACK": (255, 255, 255),
    "WHITE": (0, 0, 0),
}

INF = 9999999.99
MAP_POINTS = [(350, 37), (109, 339), (66, 590), (34, 700), (229, 599),
              (382, 650), (378, 698), (212, 692), (212, 663), (473, 709),
              (490, 622), (497, 539), (454, 530), (446, 469), (406, 467),
              (385, 480), (376, 357), (391, 362), (427, 335), (432, 372),
              (390, 387), (393, 430), (440, 423), (478, 454), (485, 407),
              (470, 361), (457, 330), (447, 306), (528, 395), (497, 276),
              (284, 119), (350, 174), (362, 146), (305, 86), (442, 170),
              (490, 187), (530, 263), (585, 380), (513, 495), (555, 514),
              (552, 540), (610, 562), (544, 576), (497, 577), (532, 630),
              (524, 663), (489, 654), (580, 680), (513, 716), (572, 727),
              (585, 646), (703, 691), (713, 662), (669, 755), (633, 451),
              (798, 581), (824, 597), (814, 640), (781, 734), (655, 371),
              (703, 420), (690, 441), (701, 459), (738, 497), (764, 475),
              (841, 549), (777, 542), (741, 551), (733, 582), (611, 544),
              (649, 575), (505, 527), (163, 697), (165, 668), (130, 666),
              (130, 624), (187, 625), (188, 663), (248, 696), (254, 646),
              (243, 748), (247, 772), (270, 749), (436, 702), (427, 746),
              (451, 705), (709, 568), (202, 241), (156, 235), (247, 181),
              (230, 169), (252, 80), (73, 274), (113, 274), (223, 48),
              (302, 137), (332, 115), (412, 159), (642, 309), (736, 227),
              (768, 268), (666, 333), (654, 300), (675, 322), (698, 345),
              (751, 290), (709, 375), (726, 361), (773, 402), (791, 389),
              (808, 397), (823, 408), (845, 383), (831, 370), (817, 357),
              (803, 344), (788, 332), (775, 376), (738, 347), (766, 315),
              (778, 299), (795, 306), (406, 178), (531, 180), (575, 145),
              (670, 232), (681, 221), (692, 237), (682, 246), (540, 192),
              (578, 161), (513, 158), (528, 145), (537, 138), (543, 130),
              (551, 123), (561, 114), (572, 125), (564, 135), (557, 143),
              (549, 153), (540, 160), (487, 131), (507, 115), (531, 101),
              (519, 132), (539, 116), (466, 104), (531, 49), (559, 23),
              (576, 41), (545, 64), (586, 53), (552, 77), (618, 32), (601, 16),
              (626, 43), (650, 18), (633, 54), (588, 94), (617, 88),
              (626, 110),
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
# PATHS = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (3, 6), (6, 7), (7, 8),
#          (0, 36), (36, 37), (37, 38), (37, 52), (39, 38), (40, 39), (40, 41),
#          (41, 42), (42, 43), (43, 44), (44, 50), (50, 49), (49, 52), (52, 51),
#          (51, 50), (50, 46), (46, 47), (47, 48), (48, 49), (45, 46), (45, 44),
#          (44, 67), (67, 68), (68, 70), (70, 1), (70, 69), (69, 68), (69, 72),
#          (69, 72), (75, 2), (75, 72), (75, 72), (75, 73), (73, 72), (73, 74),
#          (74, 67), (67, 66), (66, 65), (65, 64), (66, 71), (71, 58), (58, 59),
#          (59, 60), (59, 60), (61, 60), (62, 60), (62, 53), (53, 54), (54, 55),
#          (55, 56), (56, 57), (57, 58), (53, 36), (59, 16), (16, 15), (14, 15),
#          (17, 15), (13, 14), (13, 17), (17, 18), (18, 22), (22, 23), (23, 64),
#          (23, 63), (63, 16), (24, 22), (24, 74), (24, 25), (25, 26), (26, 27),
#          (27, 28), (27, 29), (5, 8), (8, 30), (30, 35), (35, 34), (34, 33),
#          (33, 32), (32, 31), (31, 30), (29, 75), (29, 6), (5, 9), (10, 9),
#          (10, 11), (11, 17), (18, 19), (19, 20), (20, 21), (11, 12)]
PATHS = []
POINTS = [
    (886, 558),
    (767, 540),
    (643, 540),
    (618, 557),
    (598, 534),
    (545, 481),
    (552, 438),
    (524, 394),
    (553, 301),
    (551, 203),
    (482, 220),
    (410, 217),
    (360, 217),
    (332, 193),
    (248, 153),
    (227, 130),
    (115, 145),
    (45, 136),
    (14, 131),
]
# road's width to show on map
ROAD_WIDTH = 5

# point's circle diameter to show on map
POINT_DIAMETER = 8

# distance to consider a position is near to a road
MIN_DIST_ROAD = 20

# distance to consider a position is near to another position
MIN_DIST_POINT = 20