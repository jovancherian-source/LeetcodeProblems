class Solution():
    def isAnagram(self, r ,l ):
        r_r = list(r)
        l_l = list(l)
        if len(r_r) != len(l_l):
            return False
        ok_num = len(r_r) // 2
        first_word = r_r[ok_num: len(r_r)]
        second_word = l_l[0: ok_num]
        for i in range(len(second_word)):
            first_word.append(second_word[i])
        final_word = "".join(map(str,first_word))
        if final_word == l:
            return True
        else:
            return False


mum = Solution()
print(mum.isAnagram("racecar", "carrace"))


