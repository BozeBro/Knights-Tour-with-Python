class Knight:
    def __init__(self, n=8, x=0, y=0, scraper=None):
        self.n = n
        # square board size
        self.__board = [[0 for row in range(n)] for column in range(n)]
        self.x = x
        self.y = y
        # position of the knight
        self.__moves = ((2, 1), (1, 2), (-1, 2), (-2, 1),
                        (-2, -1), (-1, -2), (1, -2), (2, -1))
        # legal moves of the knight
        self.__onlineBoard = scraper
        # tells us if we are using Online.py

    def kTour(self):
        """
        The wrapper function that sees if tour is possible or tour
        """
        START = 1
        if self.__solver(self.x, self.y, START):
            self.__printBoard()
        else:
            # all possible moves have been tried
            print('Impossible Tour')

    def __printBoard(self):
        """
        Will print the board in a nice square format
        """
        for col in range(self.n):
            for row in range(self.n):
                print(self.__board[col][row], end=' ')
            print()

    def __solver(self, cur_x, cur_y, count):
        """
        Scans each available move to see if that movement is possible
        The heavy duty function that will solve the Knights Tour
        Iterates through the moves in a rigid order
        """
        self.__board[cur_y][cur_x] = count
        # mark square with amount of squares we have now seen
        if self.__onlineBoard:
            # Clicks the square if using Online.py
            self.__onlineBoard[cur_y][cur_x].click()

        for x, y in self.__moves:
            temp_x, temp_y = cur_x + x, cur_y + y

            if 0 <= temp_x < self.n and \
                    0 <= temp_y < self.n and \
                    self.__board[temp_y][temp_x] == 0:
                """
                if statement checks if a possible move is legal (Doesn't go off the board) or
                if the move has already been visited (board[y][x] = 0)
                """
                if self.__solver(temp_x, temp_y, count + 1):
                    """
                    Calls the function again at the new square
                    """
                    return True
                    # if true then the tour is completed and we are done

        if count == self.n ** 2:
            # the actual condition that will lead to the completion of the tour
            # ALl squares have been visited
            return True

        self.__board[cur_y][cur_x] = 0
        """
        The only time that the program reaches here is when all possible moves from a square
        have been tried and none of them worked 
        We have reached a dead end
        We are forced to go backwards (backtrack) to the previous square
        Make sure to reset the square, so it is like we never visited the square
        We will try the next move in __moves.
        """
        if self.__onlineBoard:
            self.__onlineBoard[cur_y][cur_x].click()
        return False


if __name__ == '__main__':
    tour = Knight(5, 3, 2)
    tour.kTour()
