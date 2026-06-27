import math
board = [" " for _ in range(9)]

HUMAN = "X"
AI = "O"
def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()
def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in win_positions:
        if all(board[pos] == player for pos in combo):
            return True

    return False

def is_draw():
    return " " not in board

def available_moves():
    return [i for i in range(9) if board[i] == " "]

def minimax(depth, is_maximizing, alpha, beta):

    if check_winner(AI):
        return 10 - depth

    if check_winner(HUMAN):
        return depth - 10

    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for move in available_moves():

            board[move] = AI

            score = minimax(depth + 1, False, alpha, beta)

            board[move] = " "

            best_score = max(best_score, score)

            alpha = max(alpha, score)

            if beta <= alpha:
                break

        return best_score

    else:
        best_score = math.inf

        for move in available_moves():

            board[move] = HUMAN

            score = minimax(depth + 1, True, alpha, beta)

            board[move] = " "

            best_score = min(best_score, score)

            beta = min(beta, score)

            if beta <= alpha:
                break

        return best_score

def ai_move():

    best_score = -math.inf
    best_move = None

    for move in available_moves():

        board[move] = AI

        score = minimax(0, False, -math.inf, math.inf)

        board[move] = " "

        if score > best_score:
            best_score = score
            best_move = move

    board[best_move] = AI

def human_move():

    while True:

        try:

            move = int(input("Enter position (1-9): ")) - 1

            if move not in range(9):
                print("Invalid position.")
                continue

            if board[move] != " ":
                print("Position already occupied.")
                continue

            board[move] = HUMAN
            break

        except ValueError:
            print("Please enter a number.")

def show_positions():

    print("Board Positions\n")

    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")
    print()

def main():

    print("=" * 35)
    print(" TIC TAC TOE AI ")
    print("=" * 35)

    show_positions()

    while True:

        print_board()

        human_move()

        if check_winner(HUMAN):
            print_board()
            print("🎉 Congratulations! You Win!")
            break

        if is_draw():
            print_board()
            print("🤝 It's a Draw!")
            break

        print("AI is thinking...\n")

        ai_move()

        if check_winner(AI):
            print_board()
            print("🤖 AI Wins!")
            break

        if is_draw():
            print_board()
            print("🤝 It's a Draw!")
            break


if __name__ == "__main__":
    main()