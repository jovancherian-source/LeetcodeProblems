class Solution:
    def addTwoNumbers(self, l1, l2):
        ml1 =[]
        ml2 =[]
        for item in range(len(list(l1))):            
            ml1.append(l1[-(item+1)])
        for item in range(len(list(l2))):
            ml2.append(l2[-(item+1)])
        output = int("" .join(map(str, ml1))) + int("" .join(map(str, ml2)))
        final_output_1 = []
        for x in range(len(str(output))):
            final_output_1.append(str(output)[- (x + 1)])
        final_output = list(map(int, final_output_1))    
        return final_output

am = Solution()
print(am.addTwoNumbers([2,4,3], [5,6,4]))
print("hi_ there") 
# this code is not yet accepted by leetcode, but it works for the test cases provided
# this is a test form a windows machine
