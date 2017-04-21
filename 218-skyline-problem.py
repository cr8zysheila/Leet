# Very nice solution with heapq: 
# https://discuss.leetcode.com/topic/14987/108-ms-17-lines-body-explained
'''
from heapq import *

class Solution:
    def getSkyline(self, LRH):
        skyline = []
        i, n = 0, len(LRH)
        liveHR = []
        while i < n or liveHR:
            if not liveHR or i < n and LRH[i][0] <= -liveHR[0][1]:
                x = LRH[i][0]
                while i < n and LRH[i][0] == x:
                    heappush(liveHR, (-LRH[i][2], -LRH[i][1]))
                    i += 1
            else:
                x = -liveHR[0][1]
                while liveHR and -liveHR[0][1] <= x:
                    heappop(liveHR)
            height = len(liveHR) and -liveHR[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
        return skyline
'''

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(buildings) < 1:
            return buildings

        #turn each building into one skyline
        building_lines = []
        for building in buildings:
            if len(building) < 3:
                raise Exception('Input in wrong format')
            lines = [[building[0], building[2]], [building[1], 0]]
            building_lines.append(lines)

        return self.build_skyline(building_lines, 0, len(building_lines))

    # merge_sort like
    # input_lines = [[[s, h], [e, h]],  [[s, h], [e, h]],  ...]
    # return = [[x1, h], [x2, h], ...]
    def build_skyline(self, input_lines, left, right):

        if right - left == 1:
            return input_lines[left] 

        mid = left + (right -left)/2
        skyline_left = self.build_skyline(input_lines, left, mid)
        skyline_right = self.build_skyline(input_lines, mid, right)

        ''' merge: scan both lists to be merged in a merge-sort like
        way. Keep track the current height of the merged skylilne. Pay
        attention to the case where an endpoint from left list and 
        an endpoint from right list has the same x position.
        '''

        '''The following code has the potential to be optimized by 
        replacing the repeated mirrored code for left and right 
        branches with one uniformed code.
        '''
        result = []
        i, j, left_h, right_h, current_h = 0, 0, 0, 0, 0
        while i < len(skyline_left) and j < len(skyline_right):
            if skyline_left[i][0] < skyline_right[j][0]:
                left_h = skyline_left[i][1]
                if left_h > right_h or left_h == right_h == 0:
                    result.append([skyline_left[i][0],left_h])
                    current_h = left_h
                elif left_h < right_h and current_h != right_h:
                    result.append([skyline_left[i][0],right_h])
                    current_h = right_h
                i += 1
            elif skyline_left[i][0] > skyline_right[j][0]:
                right_h = skyline_right[j][1]
                if right_h > left_h or right_h == left_h == 0:
                    result.append([skyline_right[j][0],right_h])
                    current_h = right_h
                elif right_h < left_h and current_h != left_h:
                    result.append([skyline_right[j][0],left_h])
                    current_h = left_h
                j += 1
            else: # skyline_left[i][0] == skyline_right[j][0]
                left_h = skyline_left[i][1]
                right_h = skyline_right[j][1]
                if max(left_h, right_h) != current_h:
                    result.append([skyline_left[i][0], max(left_h, right_h)])
                    current_h = max(left_h, right_h)
                i += 1
                j += 1

        if i == len(skyline_left):
            result.extend(skyline_right[j:])
        elif j == len(skyline_right):
            result.extend(skyline_left[i:])

        return result


#buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
buildings = [[6765,184288,53874],[13769,607194,451649],[43325,568099,982005],[47356,933141,123943],[59810,561434,119381],[75382,594625,738524],[111895,617442,587304],[143767,869128,471633],[195676,285251,107127],[218793,772827,229219],[316837,802148,899966],[329669,790525,416754],[364886,882642,535852],[368825,651379,6209],[382318,992082,300642],[397203,478094,436894],[436174,442141,612149],[502967,704582,918199],[503084,561197,625737],[533311,958802,705998],[565945,674881,149834],[615397,704261,746064],[624917,909316,831007],[788731,924868,633726],[791965,912123,438310]]

print Solution().getSkyline(buildings)