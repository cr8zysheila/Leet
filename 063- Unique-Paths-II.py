class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        N, M = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] != 0 or obstacleGrid[N-1][M-1] != 0:
        	return 0

        # This can be a 2D tabel(see HiredIntech 05), but it's optimaize
        # into a 1D array
        numPaths = [0] * M

        for i in range(0, N):
        	for j in range(0, M):
        		if i == 0 and j == 0 and obstacleGrid[0][0] == 0:
        			numPaths[j] = 1
        		elif obstacleGrid[i][j] != 0:
        			numPaths[j] = 0
        		else:
        			if j - 1 >= 0:
        				numPaths[j] += numPaths[j-1]

        return numPaths[M-1]

A = [[0, 0, 0],[0, 1, 0], [0, 0, 0]]

print Solution().uniquePathsWithObstacles(A)
