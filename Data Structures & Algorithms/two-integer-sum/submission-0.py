class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen_nums:
                return [seen_nums[diff], i]
            else:
                seen_nums[num] = i
        
        return [-1,-1]