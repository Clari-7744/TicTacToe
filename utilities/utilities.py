import random
import tabulate

bold = "\033[1m"
r = "\033[0m"
heads = bold + "\033[95m\033[91m"
os = bold + "\033[96m"
xs = bold + "\033[92m"
ttt_help = "How to play:\n*wip check back later*"


def y_n(text):
    """
    Simple input wrapper for yes or no input.
    """
    resp = input(text + " [y/n] " + bold).lower() in ("y", "ye", "yes", "1")
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


def fmt_head(head: list):
    return [f"{heads}{str(n).upper()}{r}" for n in head]


def fmt_row(row: list):
    return [f"{xs if s == 'X' else os}{s}{r}" for s in row]


def print_board(board: dict):
    """
    Formats the given board dictionary with tabulate.
    """
    head = fmt_head("#123")
    rows = [[*fmt_head([l]), *fmt_row(ro)] for l, ro in board.items()]
    print(
        tabulate.tabulate(
            [head, *rows],
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
        return input(f">>> {bold}")

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
    user_a = input(f">>> {bold}")
    print(f"{r}Player 1's name set to {bold}{user_a}{r}")

    user_b = get_p2_name(user_a)
    print(f"{r}Player 2's name set to {bold}{user_b}{r}")
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
