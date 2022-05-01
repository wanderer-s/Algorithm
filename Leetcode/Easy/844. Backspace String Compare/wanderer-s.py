class Solution:
  def backspaceCompare(self, s: str, t: str) -> bool:
    s_result = []
    t_result = []
    
    for char in s:
      if s_result and char == '#':
        s_result.pop()
      elif char !='#':
        s_result.append(char)
      
    for char in t:
      if t_result and char == '#':
        t_result.pop()
      elif char !='#':
        t_result.append(char)
        
    s_result = ''.join(s_result)
    t_result = ''.join(t_result)
    
    return s_result == t_result
    