class Solution:
  def longestPalindrome(self, s: str) -> int:
    from collections import Counter
    s_count = Counter(s)
    length = 0

    for val in s_count.values():
      length += (val // 2 * 2)
      if length % 2 == 0 and val % 2 == 1:
          length +=1

    return length
  