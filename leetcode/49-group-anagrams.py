class Solution(object):
    def groupAnagrams(self, strs: str) -> list[str]:
        map : dict = dict() #Hashmap to hold anagrams

        for s in strs:
            v = ''.join(sorted(s))# Sort string in acending order
            map.setdefault(v,[])# [v:str: l:list[str]]
            map[v].append(s)# Add string to hashmap based on sorted string
        
        x : list[str] = list(map.values())

        return x

strs = ["eat","tea","tan","ate","nat","bat"]

p = Solution()
v = p.groupAnagrams(strs)
print(v)
