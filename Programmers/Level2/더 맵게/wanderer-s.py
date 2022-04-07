import heapq

def solution(scoville, K):
  heapq.heapify(scoville)
  
  cnt = 0
  while scoville[0] < K:
    try:
      first_minimum = heapq.heappop(scoville)
      second_minimum = heapq.heappop(scoville)

      new_scoville_value = first_minimum + second_minimum * 2

      heapq.heappush(scoville, new_scoville_value)
    except IndexError:
      return -1
    
    cnt += 1
  
  return cnt
  
