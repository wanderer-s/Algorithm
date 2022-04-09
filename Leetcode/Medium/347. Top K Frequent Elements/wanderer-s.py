from collections import Counter

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    if len(nums) == 1:
      return nums
      
    nums_counter = Counter(nums).most_common(k)
    result = []
    for counter_value in nums_counter:
      result.append(counter_value[0])
    
    return result