class Solution(object):
    def twoSum(self, nums:list[int], target:int) -> list[int]:

        if nums.__len__() <= 1:
            return []

        # seen : dict[int, int] = {}
        # index : int = 0
        seen = {}
        index = 0

        for value in nums:
            
            if (target - value) not in seen:
                seen[value]=index 
            else:
                return[seen[target - value], index]
            index+=1

        return[]


p = Solution()
result = p.twoSum([2,7,11,15],9)
print(result)
