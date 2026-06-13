class Solution():
    def groupAnagrams(self, words):
        result  = []
        new_list = []
        dummy = []
        dummy2 = []
        for item in words:
            new_list.append(list(item))
        for item in new_list:
            dummy.append(sorted(item))
        for i in dummy:
            dummy2.append(" ".join(i))
        dummy3 = sorted(dummy2)
        if "" .join(sorted(words)) == item in dummy3: 
            





test = Solution()   
print(test.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
