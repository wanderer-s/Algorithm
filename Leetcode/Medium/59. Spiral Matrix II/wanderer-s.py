class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix, reverse_num = [[n * n]], n ** 2

        while reverse_num > 1:
            reverse_num, pre_num = reverse_num - len(matrix), reverse_num
            matrix = [[*range(reverse_num, pre_num)]] + [list(z) for z in zip(*reversed(matrix))]
        return matrix
