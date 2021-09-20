import heapq
import copy


def score_map(c_pr, s_pr):
    matrix = [[0]*len(s_pr) for _ in range(len(c_pr))]
    for i in range(len(c_pr)):

        # added catch clause for no corresponding mapping--score
        for count, k in enumerate(c_pr[i]):
            # breakpoint()
            try:
                student_pr = s_pr[k-1]
                index = student_pr.index(i+1)
                pr = (index+1)+(count+1)

            except ValueError:
                print("no corresponding mapping")
                pr = 0+(count+1)
            matrix[i][k-1] = pr
        matrix[i] = [x if x != 0 else 100 for x in matrix[i]]
    print(matrix)
    return matrix


def arrange(m, n, s, t, c_pr, s_pr):
    # create the priority score map.
    map = score_map(c_pr, s_pr)

    # change map into tuple form
    for i in range(len(map)):
        for index, item in enumerate(map[i]):
            map[i][index] = (item, index+1)

    matrix = [[(0, 0)]*len(c_pr) for _ in range(s)]
    # heapify
    for x in range(len(map)):
        heapq.heapify(map[x])

    # create a copy for future use.
    refresh = copy.deepcopy(map)

    for i in range(s):

        for j in range(len(c_pr)):
            # check if it is already in the row/column.
            # breakpoint()
            student = heapq.heappop(map[j])
            while((student[1] in [tuple[1] for tuple in matrix[i]])
                  or (student[1] in [row[j][1] for row in matrix])):
                student = heapq.heappop(map[j])
            matrix[i][j] = student

        # refresh the heaps.
        multi_refresh = copy.deepcopy(refresh)
        for i in range(len(map)):
            map[i] = multi_refresh[i]

    return matrix


c_pr = [[1, 2, 3], [4, 5, 1], [6, 3, 2]]
s_pr = [[1, 2], [2, 1], [3, 1], [2], [2], [3]]
c_s = [[1, 4, 6, 0, 0, 0], [6, 0, 0, 1, 2, 0], [0, 0, 2, 0, 0, 1]]
c_pr1 = [[1], [2]]
s_pr1 = [[2], [1]]
c_pr2 = [[1, 2], [2, 1]]
s_pr2 = [[1, 2], [1, 2]]
# matrix = score_map(c_pr, s_pr)
print(arrange(3, 6, 3, 3, c_pr, s_pr))


# SAMPLES
# 1. For c_pr and s_pr:
#    score_map= [[2, 4, 5, 100, 100, 100], [5, 100, 100, 2, 3, 100], [100, 3, 3, 100, 100, 2]]
#    output= [[(2, 1), (2, 4), (2, 6)], [(4, 2), (3, 5), (3, 3)], [(5, 3), (5, 1), (3, 2)]]

# 2. For c_pr1 and s_pr1:
#     score_map=[[1, 100], [100, 1]]
#     output=[[(1, 1), (1, 2)], [(100, 2), (100, 1)]]

# 3. For c_pr2 and s_pr2:
#     score_map=[[2, 3], [4, 3]]
#     output= [[(2, 1), (3, 2)], [(3, 2), (4, 1)]]
