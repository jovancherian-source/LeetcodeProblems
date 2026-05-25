class Solution:
    def twoSum(self, nums, target):
        for x in range(len(nums)):
            for i in range (len(nums)):
                if nums[x] + nums[i] == target and x != i:
                    return [x,i]
                

solution = Solution()
print(solution.twoSum([3,4,2], 6))


# this code is accepted by leetcode