"""
Backtracking is a brute force algorithm that utilizes dynammic programming to be faster
than pure brute force. It tries legal, possible moves at random when it reaches a dead - end,
it will backtrack to the previous and try another move. The function will never choose that move again
from that square since all possible combination from the move led to a dead end.

Example of Backtracking:
You are stuck in a maze and trying to get out. You go down a certain path but it leads to a dead end.
You backtrack to before you entered the path and then,
You mark that path with a rock so you do not go down that path again, because you know it will not lead
to the exit.

Example of Brute Force:
You have 10 coins, 2 quarters, 2 pennies, 4 dimes, and 2 nickels. Find what combination leads to 7 cents
In Brute Force, you find all possible combinations of the coins.
Then you see which combination led to 7 cents which is 1 nickel and 2 pennies.
"""


class Knight:
    def __init__(self, rows=8, columns=8, n=8, x=0, y=0, scraper=None):
        self.n = n
        if self.n:
            self.rows = self.columns = self.n
        else:
            self.rows = rows
            self.columns = columns

        # square board size
        self.__board = [[0 for row in range(self.rows)] for column in range(self.columns)]
        self.x = x
        self.y = y
        # position of the knight
        self.__MOVES = ((2, 1), (1, 2), (-1, 2), (-2, 1),
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
        for col in range(self.columns):
            for row in range(self.rows):
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

        for x, y in self.__MOVES:
            temp_x, temp_y = cur_x + x, cur_y + y

            if 0 <= temp_x < self.rows and \
                    0 <= temp_y < self.columns and \
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

        if count == self.rows * self.columns:
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
