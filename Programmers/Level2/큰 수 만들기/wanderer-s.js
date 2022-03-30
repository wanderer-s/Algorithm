function solution(number, k) {
  let biggestNumArr = []
  
  for(const num of number) {
    while ( k > 0 && biggestNumArr && biggestNumArr[biggestNumArr.length - 1] < num) {
      k--
      biggestNumArr.pop()
    }
    
    biggestNumArr.push(num)
  }

  return biggestNumArr.slice(0, biggestNumArr.length - k).join('')
}
