from collections import defaultdict
def printing(flat, stand, cb):
    """
    Prints the board in a nice, board-like way
    """
    for col in range(stand):
        for row in range(flat):
            print(cb[col][row], end=' ')
        print()
    print('\n')


def get_moves(rows, columns, dx, dy):
    """
    Obtains the legal moves for each square
    """
    moves = defaultdict(list)
    for i in range(rows):
        for j in range(columns):
            for x, y in zip(dx, dy):
                temp_x = j + x
                temp_y = i + y
                if 0 <= temp_x < rows and 0 <= temp_y < columns:
                    # Makes sure the moves are not greater than the amount of rows or columns
                    moves[(j, i)].append((x, y))
    return moves

if __name__ == "__main__":
    test = get_moves(8, 8, [-2, -1, 1, 2, -2, -1,  1,  2], [1,   2, 2, 1, -1, -2, -2, -1])
    print(test)