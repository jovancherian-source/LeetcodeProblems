class Solution:
    def groupAnagrams(self, words):
        groups = {}
        for word in words:
            key = "".join(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())
            


test = Solution()   
print(test.groupAnagrams(["act","pots","tops","cat","stop","hat"]))


## this code is accepted by leetcode 