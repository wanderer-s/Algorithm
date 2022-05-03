class Solution:
  def findUnsortedSubarray(self, nums: List[int]) -> int:
    nums_length = len(nums)
    left = 0
    right = nums_length - 1
    
    while left < nums_length - 1 and nums[left] <= nums[left + 1]:
      left += 1
        
    if left == nums_length - 1:
      return 0
    
    while right > 0 and nums[right] >= nums[right - 1]:
      right -= 1
        
    min_num = min(nums[left:right + 1])
    max_num = max(nums[left:right + 1])
    
    while left > 0 and nums[left - 1] > min_num:
      left -= 1
    
    while right < nums_length - 1 and nums[right + 1] < max_num:
      right += 1
        
    return right - left + 1
    