n = int(input())
segments = []
for i in range(n):
    segments.append(tuple(map(int, input().split())))
#print('segments: ',segments)
if n == 0 and not all(segments):
    print(0)
    exit()
overlaps = []
coordinate1 = None
coordinate2 = None
for segment in segments:
    intersections = 0
    for cmp in segments:
        if cmp == segment:
            continue
        if segment[0] < cmp[0]:
            if segment[-1] > cmp[0]:
                intersections += 1
                coordinate1 = cmp[0]
                coordinate2 = segment[-1]
                if (coordinate1, coordinate2) not in overlaps:
                    overlaps.append((coordinate1, coordinate2))
                
        elif segment[0] > cmp[0]:
            if cmp[-1] > segment[0]:
                intersections += 1
                coordinate1 = segment[0]
                coordinate2 = cmp[-1]
                if (coordinate1, coordinate2) not in overlaps:
                    overlaps.append((coordinate1, coordinate2))

        else:
            coordinate1 = segment[0]
            if cmp[-1] > segment[-1]:
                coordinate2 = cmp[-1]
            else:
                coordinate2 = segment[-1]
            if (coordinate1, coordinate2) not in overlaps:
                overlaps.append((coordinate1, coordinate2))
#print('overlaps: ',overlaps)
intersection_dict = {}
for c in overlaps:
    intersection_dict[c[0]] = []
    intersection_dict[c[-1]] = []
    for segment in segments:
        if c[0] in range(segment[0], segment[-1] + 1):
            intersection_dict[c[0]].append(segment)
        if c[-1] in range(segment[0], segment[-1] + 1):
            intersection_dict[c[-1]].append(segment)
    
if len(intersection_dict) == 0:
    print(len(segments))
    exit()
    
non_intersection_list = []
for segment in segments:
    non_intersect = True
    for v in intersection_dict.values():
        if segment in v:
            non_intersect = False
            break
    if non_intersect:
        non_intersection_list.append(segment)
#print('intersection_dict: ',intersection_dict)
signed = []
m = []
repeats = []
while intersection_dict:
    longk = list(intersection_dict.keys())[0]
    longv = list(intersection_dict.values())[0]
    for k, v in intersection_dict.items():
        print('for loop')
        if k not in m:
            for seg in v:
                if seg in signed:
                    #repeats += 1
                    v.remove(seg)
                if len(v) == 0:
                    repeats.append(k)
            if len(v) >= len(longv):
                longv = v
                longk = k
    
    if longk not in m and longk not in repeats:
        m.append(longk)
    for key in repeats:
        print('repeats key: ',key)
        del intersection_dict[key]
    print('repeats: ', repeats)
        
    for seg in longv:
        #if seg not in signed:
        signed.append(seg)
    print('signed: ', signed)
    print('m: ', m)
    print('loop intersection_dict: ',intersection_dict)
    if longk not in repeats:
        del intersection_dict[longk]
    repeats.clear()
    
#print('non_intersection_list: ',non_intersection_list)
for non_intersect_segment in non_intersection_list:
    #print('non_intersect_segment: ',non_intersect_segment)
    m.append(non_intersect_segment[0])
print('final signed: ',signed)
print('final segments: ',segments)
print('final signed == segments: ', signed == segments)
print(len(m))
for i in m:
    print(i, end = ' ')
