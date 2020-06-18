class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        for i in range(len(s)//2):
            s[i],s[n-1]=s[n-1],s[i]
            n-=1

        return s