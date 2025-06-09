

class Solution(object):
    def threesum2(self, nums: list[int]) -> list[int]:
        
        leftPtr  = 0
        rightPtr = 0

        results = []
        resultset = set()
        nums.sort()
        numsLen = len(nums)

        for curIndex in range(numsLen):
            if curIndex >= numsLen - 2:
                break
            
            leftPtr = curIndex + 1
            rightPtr = numsLen - 1
            skip = False # handle duplicate values

            # if curIndex > 0 and nums[curIndex - 1] == nums[curIndex]:
            #     skip = True
            
            while leftPtr < rightPtr:# and not skip:
                value = nums[curIndex] + nums[leftPtr] + nums[rightPtr]

                if value == 0:
                    if (nums[curIndex], nums[leftPtr], nums[rightPtr]) not in resultset:
                        results.append([nums[curIndex], nums[leftPtr], nums[rightPtr]])
                        resultset.add((nums[curIndex], nums[leftPtr], nums[rightPtr]))
                    
                    rightPtr -= 1
                    leftPtr += 1
                
                elif value > 0:
                    rightPtr -= 1
                elif value < 0:
                    leftPtr += 1
                
            
        return results

    def threesum(self, nums: list[int]) -> list[int]:

        nums.sort()
        returnValue = []
        currentIndex = 0
        leftPtr = 0
        rightPtr = 0
        numsLen = len(nums)
        
        while currentIndex < numsLen - 2:
            # while nums[currentIndex] == nums[currentIndex + 1]:
            #     currentIndex+=1

            # while currentIndex > 0 and nums[currentIndex - 1] == nums[currentIndex] and currentIndex < numsLen - 2:
            #     currentIndex += 1

            if currentIndex > 0 and nums[currentIndex] == nums[currentIndex - 1]:
                currentIndex += 1
                continue

            leftPtr = currentIndex + 1
            rightPtr = numsLen - 1

            while leftPtr < rightPtr:
                zero = nums[currentIndex] + nums[leftPtr] + nums[rightPtr]

                if 0 == zero:
                    returnValue.append([nums[currentIndex], nums[leftPtr], nums[rightPtr]])
                    while leftPtr < rightPtr and nums[leftPtr] == nums[leftPtr + 1]:
                        leftPtr += 1
                    while leftPtr < rightPtr and nums[rightPtr] == nums[rightPtr - 1]:
                        rightPtr -= 1
                    
                    rightPtr-=1
                    leftPtr+=1
                
                elif 0 > zero:
                    leftPtr+=1
                elif 0 < zero:
                    rightPtr-=1

            
            currentIndex+=1
        
        
        return returnValue
        







p = Solution()

input : list[int] = [-1,0,1,2,-1,-4]
actual_result = p.threesum(input)
print(actual_result)

input : list[int] = [0,1,1]
actual_result = p.threesum(input)
print(actual_result)

input : list[int] = [0,0,0]
actual_result = p.threesum(input)
print(actual_result)



