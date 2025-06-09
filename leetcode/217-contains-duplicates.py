class Solution(object):
    def containsDuplicate(self, nums: list[int]) -> bool:

        if 1 >= len(nums):
            return False

        hashmap : list = []

        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap.append(num)

        return False

p = Solution()
input = [1,2,3,1]
x = p.containsDuplicate(input)
print(x)

input = [1,2,3,4]
x = p.containsDuplicate(input)
print(x)

input = [1,1,1,3,3,4,3,2,4,2]
x = p.containsDuplicate(input)
print(x)


