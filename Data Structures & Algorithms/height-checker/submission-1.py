class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [0]*101
        n = len(heights)
        for h in heights:
            count[h] +=1
        expected = []
        for h in range(1,101):
            num = count[h]
            for _ in range(num):
                expected.append(h)
        output = 0
        for i in range(n):
            if expected[i] != heights[i]: 
                output +=1

        return output
