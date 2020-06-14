from collections import defaultdict


def dorffer(posX=0, posY=0, vertical=8, horizon=8, oBoard=None, n=None):
    """
    Wrapper that sets up the variables for dorff()
    """
    if n:
        """kwarg to easily have a square board. 
        vertical and horizon gives more control of board hieght and length 
        Example: (vertical=5, horizon=8)
        """
        vertical = horizon = n
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    """
    The legal moves a knigh can make.
    Example: if knight moved dx[0] and dy[0], the knight moves 2 squares to the left and 1 square down
    The point (0, 0) is the top left corner so to move down, the y increases
    """
    moves = get_moves(horizon, vertical, dx, dy)
    board = [[0 for i in range(horizon)] for j in range(vertical)]
    

    def dorff(cur_x=posX, cur_y=posY, count=1):
        """
        The function doing the Warnsdorff Algorithm.
        The idea of this algorithm is to play the moves which will have the least possible options.
        The available squares that a knight can go to from its current square are called neighbors
        Example: If a knight is on square 1 and has the neighbors square 2 and square 3, 
        but square 2 has 4 neighbors and square 3 has 2 neighbors.
        The algorithm will move the knight to square 3 because it has the fewest amount of neighbors
        """
        
        inline = []  
        # priority queue. Orders possible moves by fewest neighbors
        board[cur_y][cur_x] = count
        if __name__ != "__main__":
            """
            if __name__ != "__main__", then we are using this function in Online.py/ on the web.
            We do not want this click method used outside of Online.py
            """
            oBoard[cur_y][cur_x].click()
        for x, y in moves[(cur_x, cur_y)]:
            # Getting each neighbor of current square
            nx = cur_x + x
            ny = cur_y + y
            if board[ny][nx] == 0:
                
                n_count = 0
                for mx, my in moves[(nx, ny)]:
                    # Getting the amount of neighboring square per neighboring square of the current square
                    ex = nx + mx
                    ey = ny + my
                    if board[ey][ex] == 0:
                        n_count += 1

                inline.append((nx, ny, n_count))
        inline.sort(key=lambda m: m[2])

        for x, y, c in inline:
            if board[y][x] == 0:
                if dorff(x, y, count + 1):
                    return True

        if count == horizon * vertical:
            return True
        board[cur_y][cur_x] = 0
        if __name__ != "__main__":
            oBoard[cur_y][cur_x].click()
        return False

    if dorff():
        print('success')
        printing(horizon, vertical, board)
    else:
        print('Fail')


def printing(flat, stand, cb):
    """
    Prints the board in a nice, board-like way
    """
    for col in range(stand):
        for row in range(flat):
            print(cb[col][row], end=' ')
        print()
    print('\n')


def get_moves(horizon, vertical, dx, dy):
    """
    Obtains the legal moves for each square
    """
    moves = defaultdict(list)
    for i in range(horizon):
        for j in range(vertical):
            for x, y in zip(dx, dy):
                temp_x = j + x
                temp_y = i + y
                if 0 <= temp_x < horizon and 0 <= temp_y < vertical:
                    moves[(j, i)].append((x, y))
    return moves


if __name__ == "__main__":
    dorffer(0, 0, 8, 8)
