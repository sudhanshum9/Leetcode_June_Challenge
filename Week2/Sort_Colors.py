class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def mergesort(nums):
            if(len(nums)>1):
                mid=len(nums)//2
                lefthalf=nums[:mid]
                righthalf = nums[mid:]

                mergesort(lefthalf)
                mergesort(righthalf)

                i=0
                j=0
                k=0

                while i<len(lefthalf) and j< len(righthalf):
            
                    if lefthalf[i]<righthalf[j] :
                        nums[k]=lefthalf[i]
                        i+=1
                        k+=1
                    else:
                        nums[k]=righthalf[j]
                        j+=1
                        k+=1

            
                while i<len(lefthalf):

                    nums[k]=lefthalf[i]
                    i+=1
                    k+=1

            
                while j<len(righthalf):

                    nums[k]=righthalf[j]
                    j+=1
                    k+=1

            return nums
        mergesort(nums)
                    
            