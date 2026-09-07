class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett = set()
        n = len(nums)
        for num in nums:
            if num in sett:
                return True
            sett.add(num)
        return False
            