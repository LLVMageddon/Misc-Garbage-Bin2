class Solution(object):
    def maxProfit(self, prices: list[int]) -> int:
        lowestPrice = prices[0]
        profit = 0

        for x in prices[1:]:
            if x < lowestPrice:
                lowestPrice = x
            else:
                if (x - lowestPrice) > profit:
                    profit = (x - lowestPrice)
              
        return profit



p = Solution()
data: list[int] = [7, 1, 5, 3, 6, 4]
i = p.maxProfit(data)
print(i)
data: list[int] = [7,6,4,3,1]
i = p.maxProfit(data)
print(i)
data: list[int] = [1,2]
i = p.maxProfit(data)
print(i)
data: list[int] = [2,4,1]
i = p.maxProfit(data)
print(i)
i = p.maxProfit(data)
print(i)
