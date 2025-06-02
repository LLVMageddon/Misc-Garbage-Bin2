class Solution(object):
    def lengthOfLongestSubstring2(self, s : str) -> int:
        # BRUTE FORCE
        max_len :int = 0
        string_len : int = len(s)
        map : dict = dict()

        for char in range(string_len):
            cur_len :int = 0
            map : dict = dict()

            for char_index in range(char, string_len):
                if s[char_index] in map:
                    break
                # map.append(s[char_index],None)
                map[s[char_index]] = None
                cur_len += 1
            
            max_len = max(max_len, cur_len)

        return max_len
    


    def lengthOfLongestSubstring (self, s : str) -> int:
        
        max_len : int = 0
        string_len : int = len(s)
        map : dict = dict()
        left_ptr = 0

        for right_ptr in range(string_len):
            if s[right_ptr] in map and map[s[right_ptr]] >= left_ptr:
                # print("h")# remove from map
                left_ptr = map[s[right_ptr]] + 1
            # else:
            map[s[right_ptr]] = right_ptr
            max_len = max(max_len, right_ptr - left_ptr + 1)

        return max_len



p = Solution()
s = "abcabcbb"
i = p.lengthOfLongestSubstring(s)
print(i)
s = "bbbbb"
i = p.lengthOfLongestSubstring(s)
print(i)
s = "pwwkew"
i = p.lengthOfLongestSubstring(s)
print(i)

# Why is this even a medium question?