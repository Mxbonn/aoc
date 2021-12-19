import math
from collections import defaultdict, Counter

import numpy as np
from aocd import data
from scipy.spatial import distance


def process(data):
    raw_scans = data.split('\n\n')
    scans = []
    scans_distance_maps = []
    scan_positions = {0: (0, 0, 0)}
    for scan in raw_scans:
        scan_coords = np.array([[int(x) for x in coord.split(',')] for coord in scan.splitlines()[1:]])
        scans.append(scan_coords)
        dist_map = coords_to_dist_map(scan_coords)
        scans_distance_maps.append(dist_map)

    beacons = scans[0]
    while len(scan_positions) < len(scans):
        for i in scan_positions.keys():
            for j in list(set(list(range(len(scans)))) - set(scan_positions.keys())):
                m1, m2 = scans_distance_maps[i], scans_distance_maps[j]
                match, m1_points, m2_points = match_scan_distances(m1, m2)
                if match:
                    source_points = np.hstack((scans[i][m1_points], np.ones((len(m1_points), 1), dtype=int)))
                    dest_points = np.hstack((scans[j][m2_points], np.ones((len(m1_points), 1), dtype=int)))
                    all_dest_points = np.hstack((scans[j], np.ones((len(scans[j]), 1), dtype=int)))
                    M, res, rank, s = np.linalg.lstsq(dest_points, source_points, rcond=None)
                    position = np.rint(M.T @ np.array([0, 0, 0, 1]).T).astype(int)[:3]
                    new_beacon_coords = np.rint(M.T @ all_dest_points.T).astype(int).T[:, :3]
                    scan_positions[j] = tuple(position)
                    scans[j] = new_beacon_coords
                    beacons = np.vstack((beacons, new_beacon_coords))
                    break
            else:
                continue
            break
    return beacons, scan_positions


def match_scan_distances(m1, m2):
    dists1 = np.unique(m1[np.triu_indices_from(m1, 1)])
    dists2 = np.unique(m2[np.triu_indices_from(m2, 1)])
    uniques, counts = np.unique(np.concatenate([dists1, dists2]), return_counts=True)
    if len(counts[counts > 1]) < math.comb(12, 2):
        return False, [], []
    m1_to_m2_mapping = defaultdict(list)
    for dist, c in zip(uniques, counts):
        if c > 1:
            m1_point = np.where(m1 == dist)
            m2_point = np.where(m2 == dist)
            m1_to_m2_mapping[m1_point[0][0]].append(m2_point[0][0])
            m1_to_m2_mapping[m1_point[0][0]].append(m2_point[0][1])
            m1_to_m2_mapping[m1_point[0][1]].append(m2_point[0][0])
            m1_to_m2_mapping[m1_point[0][1]].append(m2_point[0][1])
    m1_to_m2_mapping = {k: Counter(v).most_common(1)[0][0] for k, v in m1_to_m2_mapping.items()}
    return True, list(m1_to_m2_mapping.keys()), list(m1_to_m2_mapping.values())


def coords_to_dist_map(scan_coords):
    dist_map = distance.cdist(scan_coords, scan_coords, metric='euclidean')
    return dist_map


def part_one(data):
    beacons, _ = process(data)
    return len(np.unique(beacons, axis=0))


def part_two(data):
    _, scanners = process(data)
    coords = np.array([coord for coord in scanners.values()])
    return int(np.max(distance.cdist(coords, coords, metric='cblock')))


edata = """\
--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14
"""
elines = edata.splitlines()

if __name__ == '__main__':
    print(part_one(edata))
    print(part_one(data))
    print(part_two(edata))
    print(part_two(data))
