class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                sum = nums[x] + nums[y]
                if sum == target:
                    result.append(x)
                    result.append(y)
                    return result
        return result
