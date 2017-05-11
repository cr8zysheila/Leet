class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        neighbors = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        count = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    #count
                    count += 1

                    #sink
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        grid[x][y] = 0
                        for m, n in neighbors:
                            if (0 <= x+m < len(grid)) and (0 <= y+n < len(grid[0])) and (
                            grid[x+m][y+n] == 1 ):
                                stack.append((x+m, y+n))
                                print x+m, y+n
                                print i, j 


        return count

grid = [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]

print Solution().numIslands(grid)