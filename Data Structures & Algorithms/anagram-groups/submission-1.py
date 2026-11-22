class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_item = defaultdict(list)
        for word in strs:
            key = tuple(sorted(Counter(word).items()))
            dict_item[key].append(word)
        output = list(dict_item.values())
        return output