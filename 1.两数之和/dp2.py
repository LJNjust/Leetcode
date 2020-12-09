class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = dict()
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target - num], i]
            num_dict[num]=i

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([3,3], 6))