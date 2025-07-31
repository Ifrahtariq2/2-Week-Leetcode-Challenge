class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        hm = {}
        for i in range(len(nums)):
            temp = target - nums[i] 
            if temp in hm:
                ans.append(i)
                ans.append(hm[temp])
            else:
                hm[nums[i]] = i
            

        return ans





        


        