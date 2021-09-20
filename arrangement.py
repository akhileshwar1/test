import heapq
import copy


def score_map(c_pr, s_pr):
    matrix = [[0]*len(s_pr) for _ in range(len(c_pr))]
    for i in range(len(c_pr)):

        # case for no corresponding mapping--score
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

    # output_format(matrix, copy_map, s)


c_pr = [[1, 2, 3], [4, 5, 1], [6, 3, 2]]
s_pr = [[1, 2], [2, 1], [3, 1], [2], [2], [3]]
c_s = [[1, 4, 6, 0, 0, 0], [6, 0, 0, 1, 2, 0], [0, 0, 2, 0, 0, 1]]
c_pr1 = [[1], [2]]
s_pr1 = [[2], [1]]
# matrix = score_map(c_pr, s_pr)
print(arrange(2, 2, 2, 10, c_pr1, s_pr1))