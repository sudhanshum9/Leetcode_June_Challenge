from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        p=Counter(nums)
        
        
        for i in p:

            if(p[i]==1):
                return i