import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.array
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        shuffled = self.array[:]
        for i in range(0, len(shuffled)):
            chosen = random.randrange(i, len(shuffled))
            if i != chosen:
                shuffled[i], shuffled[chosen] = shuffled[chosen], shuffled[i]

        return shuffled

obj = Solution([1, 2, 3])
print obj.reset()
print obj.shuffle()
