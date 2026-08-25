class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for num in strs:
            sortedS = ''.join(sorted(num))
            hashmap[sortedS].append(num)
        return list(hashmap.values())
