class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_list = {}
        t_list = {}
        for char in s:
            if char in s_list: s_list[char] += 1
            else: s_list[char] = 1
        for char in t:
            if char in t_list: t_list[char] += 1
            else: t_list[char] = 1
        for key in s_list:
            if key not in t_list or t_list[key] != s_list[key]:
                return False
        return True
        