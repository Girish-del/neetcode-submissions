class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)
        # hashmap = {}
        # for i in range(n):
        #     remainder = target - nums[i] 
        #     if remainder in hashmap:
        #         return [hashmap[remainder], i]
        #     hashmap[nums[i]] = i
        # return 0


        n = len(nums)
        hashmap = {}
        for i in range(n):
            remainder = target - nums[i]
            if remainder in hashmap:
                return [hashmap[remainder], i]
            hashmap[nums[i]] = i
        return 0