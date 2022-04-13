class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        if m == 0 or n == 0:
            return

        for iM in range(m):
            for iN in range(n):
                sum_neighbors = sum([board[i][j] % 2 for i in range(iM - 1, iM + 2) for j in range(iN - 1, iN + 2) if 0 <= i < m and 0 <= j < n]) - board[iM][iN]
                if board[iM][iN] == 0 and sum_neighbors == 3:
                    board[iM][iN] = 2
                if board[iM][iN] == 1 and (sum_neighbors < 2 or sum_neighbors > 3):
                    board[iM][iN] = 3

        for iM in range(m):
            for iN in range(n):
                if board[iM][iN] == 2:
                    board[iM][iN] = 1
                if board[iM][iN] == 3:
                    board[iM][iN] = 0
