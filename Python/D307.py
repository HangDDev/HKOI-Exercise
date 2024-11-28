# https://judge.hkoi.org/task/D307

board = []
for i in range(3):
    board.append(input().strip())

def check():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ".":
            return f"{board[i][0]} wins"
    
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != ".":
            return f"{board[0][i]} wins"

    if board[0][0] == board[1][1] == board[2][2] != '.':
        return f"{board[0][0]} wins"
    if board[0][2] == board[1][1] == board[2][0] != '.':
        return f"{board[0][2]} wins"

    for row in board:
        if '.' in row:
            return "Not ended"
    
    return "Draw"

result = check()
print(result)
