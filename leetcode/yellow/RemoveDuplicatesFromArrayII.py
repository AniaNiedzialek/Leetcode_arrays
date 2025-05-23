from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 2
        
        for i in range(2, len(nums)):
            if nums[i] != nums[count - 2]:
                nums[count] = nums[i]
                count += 1
        print(nums)
        return count
    
    
solution = Solution()
nums = [1,1,1,2,2,3]
print(solution.removeDuplicates(nums))
solution = Solution()
nums = [0,0,1,1,1,1,2,3,3]
print(solution.removeDuplicates(nums))