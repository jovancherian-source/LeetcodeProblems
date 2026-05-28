class Solution:
    def addTwoNumbers(self, l1, l2):
        rl1 = []
        rl2 =[]
        while l1:
            rl1.append(l1.val)
            l1 = l1.next
        while l2:
            rl2.append(l2.val)
            l2 = l2.next
        ml1 =[]
        ml2 =[]
        for item in range(len(rl1)):            
            ml1.append(rl1[-(item+1)])
        for item in range(len(rl2)):
            ml2.append(rl2[-(item+1)])
        output = int("" .join(map(str, ml1))) + int("" .join(map(str, ml2)))
        final_output_1 = []
        for x in range(len(str(output))):
            final_output_1.append(str(output)[- (x + 1)])
        final_output = list(map(int, final_output_1))   
        real = ListNode()
        current = real
        for item in final_output:
            current.next = ListNode(item)
            current = current.next
        return real.next

#this code is accepted by leetcode and is efficent.