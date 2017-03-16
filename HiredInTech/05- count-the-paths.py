'''
Without cells being occupied, there are totally (n-1 + m-1)!/((n-1)!(m-1)!) paths

Start from the bottom left, fill a 2D array A from left to right and 
from bottom to top. A[i][j] is the total number of paths form grid[n-1][0]
to grid[i][j]. If a cell is occupied, A[i][j] is 0. Outside boundery is 0
'''
def count_the_paths(grid):
    # Write your solution here
    N = len(grid)
    M = len(grid[0])

    #if starting or ending cell is occupied, return 0
    if grid[N-1][0] != '0' or grid[0][M-1] != '0':
        return 0

    row = [0] * M
    A = [row[:] for i in range(0, N)]
    
    #decreasing loop, step is -1
    for i in range(N-1, -1, -1):
        for j in range(0, M):
            # initialize the left bottom to 1

            if i == N-1 and j == 0:
                A[i][j] = 1
            elif grid[i][j] == '1':
                A[i][j] = 0
            else:
                right = 0
                below = 0
                if j-1 >= 0:
                    right = A[i][j-1]
                if i+1 < N:
                    below = A[i+1][j]

                A[i][j] = right + below

    
    return A[0][M-1]

a = ["001", "000", "000"]
print count_the_paths(a)



