#two sum leetcode problem

# nums = [2, 7, 11, 15]
# target = 9

# target_sum = [(i, j) for i in range(len(nums))
#               for j in range( i +1 ,len(nums))
#               if nums[i] + nums[j] == target]

# print(target_sum[0])
nums = [2,7,11,19,21]
target = 9

class Solution:
   def twoSum(self, nums, target):
       num_to_index = {}
       for index, num in enumerate(nums):
           complement = target - num
           if complement in num_to_index:
               return [num_to_index[complement], index]
           num_to_index[num] = index

s = Solution()
print(s.twoSum(nums, target))          


            

            
              
              
              
              