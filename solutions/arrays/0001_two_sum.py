# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dictA = {}

        for i in range(len(nums)):
            if target - nums[i] in dictA.keys():
                result = [dictA[target - nums[i]], i]
                return result
                break
            else:
                dictA.update({nums[i]: i})