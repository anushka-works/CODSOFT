def print_board(board):
    print("\nCurrent board:")
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")
def check_winner(board, player):
    win_patterns = [(0,1,2), (3,4,5), (6,7,8),
                  (0,3,6), (1,4,7), (2,5,8),
                  (0,4,8), (2,4,6)]
    return any(board[a]==board[b]==board[c]==player for a,b,c in win_patterns)
def minimax(board, is_maximizing):
    if check_winner(board, "O"): return 1
    if check_winner(board, "X"): return -1
    if " " not in board: return 0
    if is_maximizing:
        best = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = max(best, minimax(board, False))
                board[i] = " "
        return best
    else:
        best = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = min(best, minimax(board, True))
                board[i] = " "
        return best
def best_move(board):
    move = -1
    best_score = -float("inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move
def play():
    board = [" "]*9
    print("Welcome to Tic Tac Toe!")
    print("You're X,and the AI is O.")
    print_board(board)
    while True:
        try:
            user_input = int(input("Enter a position (1-9): ")) - 1
            if board[user_input] != " ":
                print("That position is taken.Please try again.")
                continue
        except:
            print("Invalid input.Please try again.")
            continue
        board[user_input] = "X"
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if " " not in board:
            print("It's a draw!")
            break
        print("AI's turn...")
        ai_move = best_move(board)
        board[ai_move] = "O"
        print_board(board)
        if check_winner(board, "O"):
            print("AI wins! Better luck next time!")
            break
        if " " not in board:
            print("It's a draw!")
            break
play()
