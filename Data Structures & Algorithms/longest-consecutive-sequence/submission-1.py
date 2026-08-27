class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in sett:
                count = 1
                current = num

                while current + 1 in sett:
                    current += 1
                    count += 1
                
                longest = max(longest, count)
        return longest
