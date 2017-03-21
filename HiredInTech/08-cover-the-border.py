''' HiredInTech solution '''
def cover_the_border(l, radars):
    # Example arguments:
    # l = 100
    # radars = [ [5, 10], [3, 25], [46, 99], [39, 40], [45, 50] ]
    if len(radars) < 1:
        return 0

    endpoints = []
    for end in radars:
        endpoints.append([end[0], 0])
        endpoints.append([end[1], 1])

    endpoints.sort(key = lambda endpoint: endpoint[0])
    open_count = 0
    last_open = 0
    covered = 0
    for endpoint in endpoints:
        if endpoint[1] == 0:
            open_count += 1
            if open_count == 1:
                last_open = endpoint[0]

        else:
            open_count -= 1
            if open_count == 0:
                covered += endpoint[0] - last_open

    return covered


''' My solution '''
def cover_the_border_my(l, radars):
    # Example arguments:
    # l = 100
    # radars = [ [5, 10], [3, 25], [46, 99], [39, 40], [45, 50] ]
    if len(radars) < 1:
        return 0

    radars.sort(key = lambda radar: radar[0])
    result = []
    result.append(radars[0])

    j = 0 # last in the result 
    for i in range(1, len(radars)):
        merged = [0, 0]
        if can_merge(result[j], radars[i], merged):
            result[j][0] = merged[0]
            result[j][1] = merged[1]
        else:
            result.append(radars[i])
            j += 1

    covered = 0
    for seg in result:
        covered += seg[1] - seg[0]

    return covered

# if seg L1 and seg L2 can merge. if true, merge segs into R
# L1[0] <= L2[0]
def can_merge(L1, L2, R):
    if L1[1] < L2[0]:
        return False
    else:
        R[0] = L1[0]
        R[1] = max(L1[1], L2[1])
        return True


radars = [ [5, 10], [3, 25], [46, 99], [39, 40], [45, 50] ]
print cover_the_border(100, radars)