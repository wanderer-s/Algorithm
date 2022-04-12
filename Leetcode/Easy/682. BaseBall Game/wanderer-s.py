class Solution:
  def calPoints(self, ops: List[str]) -> int:
    record = [int(ops[0])]
    for i in range(1, len(ops)):
      record_idx = len(record) - 1
      ele = ops[i]
      if ele == "C":
        record.pop()
      elif ele == "D":
        double = int(record[record_idx]) * 2
        record.append(double)
      elif ele == "+":
        plus = int(record[record_idx]) + int(record[record_idx - 1])
        record.append(plus)
      else:
        record.append(int(ele))
      
    
    return sum(record)