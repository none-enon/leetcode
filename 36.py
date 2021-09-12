class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row=[[] for i  in range(len(board)) ]
        column=[[] for i  in range(len(board))]
        grid=[[] for i  in range(len(board))]

        for i in range(len(board)):

            for j in range(len(board[i])):
                if board[i][j]=='.':
                    continue
                if board[i][j] in column[j]:
                    return False
                if board[i][j] in row[i]:
                    return False
                k = i/3+(j/3)*3
                if board[i][j] in grid[k]:
                    return False
                row[i].append((board[i][j]))
                column[j].append(board[i][j])
                grid[k].append(board[i][j])
        return True
        
