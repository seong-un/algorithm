def solution(board, skill):
    answer = 0
    sum_board = [[0] * (len(board[0]) + 1) for i in range(len(board) + 1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        sum_board[r1][c1] += degree if type == 2 else -degree
        sum_board[r1][c2 + 1] += -degree if type == 2 else degree
        sum_board[r2 + 1][c1] += -degree if type == 2 else degree
        sum_board[r2 + 1][c2 + 1] += degree if type == 2 else -degree
    
    for i in range(len(sum_board) - 1):
        for j in range(len(sum_board[0]) - 1):
            sum_board[i][j + 1] += sum_board[i][j]
    
    for i in range(len(sum_board) - 1):
        for j in range(len(sum_board[0]) - 1):
            sum_board[i + 1][j] += sum_board[i][j]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + sum_board[i][j] > 0:
                answer += 1
    return answer