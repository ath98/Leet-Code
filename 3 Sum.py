
class Solution:
    def threeSum(self, nums):
        idxLst = []
        if len(nums) <=2:
            return[]
        else:
            nums.sort()
#             We need tripplets at a time so limiting the loop for 3 
        for i in range(0,len(nums)-2):
            beg = i+1
            end = len(nums)-1
            while beg<end:
                if nums[i]+nums[beg]+nums[end] == 0:
                    idxLst.append((nums[i],nums[beg],nums[end]))
                    beg+=1
                    end-=1
                elif nums[i]+nums[beg]+nums[end]>0:
                    end-=1
                elif nums[i]+nums[beg]+nums[end]<0:
                    beg+=1
        return set(idxLst)

obj = Solution()
obj.threeSum([-1,0,1,2,-1,-4])