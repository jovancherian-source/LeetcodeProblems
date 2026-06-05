class Solution():
    def containsDuplicate(self, nums):
        dups = set()
        final_output =[]
        for i in nums:
            if i in dups:
                final_output.append(i)
            else:      
                dups.add(i)
            if len(final_output) > 0:
                return True
        return False


solution = Solution()
print(solution.containsDuplicate([1,3]))

#this code is accepted by leetcode and is very efficient.