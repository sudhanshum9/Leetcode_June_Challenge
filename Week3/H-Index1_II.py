class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length=len(citations)
        
        for i,c in enumerate(citations):
            
            if c>= length-i:
                return length-i
            
        return 0