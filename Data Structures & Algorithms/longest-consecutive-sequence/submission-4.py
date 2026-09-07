class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Sorting 
        # Using set

        store = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in store:
                length = 1

                while (num + length) in store:
                    length += 1
                longest = max(longest, length)
        return longest