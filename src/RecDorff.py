import util

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
    dx = [-2, -1, 1, 2, -2, -1,  1,  2]
    dy = [1,   2, 2, 1, -1, -2, -2, -1]
    """
    The legal moves a knigh can make.
    Example: if knight moved dx[0] and dy[0], the knight moves 2 squares to the left and 1 square down
    The point (0, 0) is the top left corner so to move down, the y increases
    """
    moves = util.get_moves(horizon, vertical, dx, dy)
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

        in_line = []
        # priority queue.
        board[cur_y][cur_x] = count
        # Because we have traveled this square, mark it by the amount of squares we have now visited.
        # if this is the second square we have seen, then mark board[y][x] = 2
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
                    # Getting the amount of neighbors per neighbor of the current square
                    n2x = nx + mx
                    n2y = ny + my
                    if board[n2y][n2x] == 0:
                        # if statement makes sure the square has not been traversed yet
                        n_count += 1

                in_line.append((nx, ny, n_count))

        in_line.sort(key=lambda m: m[2])
        # Orders the list by fewest neighbors (move for x, move for y, amount of neighbros)
        for x, y, _ in in_line:
            # Will check each if it completes the Knights Tour(Visit all the squares once)
            if dorff(x, y, count + 1):
                return True
                
                # The recursive bulk of the function
                # It will iterate through the moves in in_line.
                # It will call the dorff() function again and will travel to a new square.
                

        if count == horizon * vertical:
            return True
            # This signifies that all squares have been traversed once.
        board[cur_y][cur_x] = 0
        """
        If not true then it must be false
        The only time the function will reach this part of the program is when
        in_line is out of moves for this square to try.
        In that case, we need to set this square back to zero 
        (because the square did not lead to the answer and we cannot go forward, only backward)
         and we must backtrack to the previous square
        Backtracking means that move is not successful and to try the next move in in_line.
        """
        if __name__ != "__main__":
            """
            Clicking will backtrack us to the previous square on the website we are scraping.
            """
            oBoard[cur_y][cur_x].click()
        return False

    if dorff():
        util.printing(horizon, vertical, board)
    else:
        # we reach False if we tried all possible moves and no sequence solves the tour
        # Easy example of failure is trying the knight's tour on a 3 x 3 board.
        print('Fail')


if __name__ == "__main__":
    dorffer(0, 0, 8, 8)
