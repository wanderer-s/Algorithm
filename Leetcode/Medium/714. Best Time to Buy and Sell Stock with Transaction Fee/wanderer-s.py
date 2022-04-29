class Solution:
  def maxProfit(self, prices: List[int], fee: int) -> int:
    cash_with_stock = - prices[0]
    cash_without_stock = 0
    
    for i in range(1, len(prices)):
      cash_with_stock = max(cash_with_stock, cash_without_stock - prices[i])
      cash_without_stock = max(cash_without_stock, cash_with_stock + prices[i] - fee)
    
    return cash_without_stock
