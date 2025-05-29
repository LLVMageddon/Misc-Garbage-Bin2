class Solution(object):
    def topKFrequent(self, nums : list[int], k : int) -> list[int]:

        map = dict()
        return_list : list[int] = []
        count : int = 0

        for x in nums:
            map[x] = 1 + map.get(x,0)

        map2 : dict = sorted(map.items(),key=lambda x: x[1])

        for xx in reversed(map2):
            return_list.append(xx[0])
            count+=1
            if count == k:
                return return_list

        return 0








nums = [1,1,1,2,2,3,3]
k = 2
# nums = [-1,-1]
# k = 1

p = Solution()
val = p.topKFrequent(nums, k)

print(val)
