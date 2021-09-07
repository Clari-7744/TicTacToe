import random
import tabulate

b = "\033[1m"
r = "\033[0m"
ttt_help = "How to play:\n*wip check back later*"


def y_n(text):
    """
    Simple input wrapper for yes or no input.
    """
    resp = input(text + " [y/n] " + b).lower() in ("y", "ye", "yes", "1")
    print(r)
    return resp


def make_board(a, b):
    """
    Builds a new board.
    """
    board = dict(zip("abc", (["", "", ""], ["", "", ""], ["", "", ""])))
    _next = random.choice((a, b))
    last = b if _next == a else a
    return board, _next, last


def print_board(board: dict):
    """
    Formats the given board dictionary with tabulate.
    """
    head = [f"{b}{n}{r}" for n in ["#", 1, 2, 3]]
    print(
        tabulate.tabulate(
            [head, *[[f"{b}{l.upper()}{r}", *ro] for l, ro in board.items()]],
            tablefmt="fancy_grid",
        )
    )


def get_p2_name(p1):
    """
    Gets Player 2's name and whether or not it should be an AI.
    """
    if y_n(
        "Would you like to play against an AI? (Will prompt for Player 2 if you don't say yes)"
    ):
        return "AI"

    def p2n():
        print("Player 2: Input your name")
        return input(f">>> {b}")

    u_b = p2n()
    while u_b == p1:
        print(f"{r}Players cannot have the same name!")
        u_b = p2n()
    return u_b


def startup(cont=False):
    """
    Initial prints and getting players' names.
    """
    if not cont:
        print(f"{r}Welcome to TicTacToe!")
        if y_n("Would you like to see the directions?"):
            print(ttt_help)
        else:
            print("Great! In that case, jump right in!")

    print(r, "\nPlayer 1: Input your name")
    user_a = input(f">>> {b}")
    print(f"{r}Player 1's name set to {b}{user_a}{r}")

    user_b = get_p2_name(user_a)
    print(f"{r}Player 2's name set to {b}{user_b}{r}")
    return user_a, user_b


def validate_text(board: dict, text):
    """
    Checks if the given input is a valid move.
    """
    if len(text) != 2:
        print("Wrong input length. Valid input format: `1a`, `a1` (not case-sensitive)")
        return False
    col, row = text if text[0].isdigit() else text[::-1]
    if col not in map(str, range(1, 4)):
        print("Column must be between 1 and 3!")
        return False
    if row not in "abc":
        print("Row must be A, B, or C!")
        return False
    col = int(col) - 1
    if board[row][col]:
        print("This space is already filled!")
        return False
    return row, col
