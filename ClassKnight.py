class Knight:
    def __init__(self, n=8, x=0, y=0, scraper=None):
        self.n = n
        self.__board = [[0 for row in range(n)] for column in range(n)]
        self.x = x
        self.y = y
        self.__moves = ((2, 1), (1, 2), (-1, 2), (-2, 1),
                        (-2, -1), (-1, -2), (1, -2), (2, -1))
        self.__onlineBoard = scraper
        # (x,y) The starting point on the board
        # n: The dimensions of the square board

    def kTour(self):
        """
        The wrapper function that sees if tour is possible or tour
        """
        if self.__solver(self.x, self.y, 1):
            self.__printBoard()
        else:
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
        """
        self.__board[cur_y][cur_x] = count
        if self.__onlineBoard:
            self.__onlineBoard[cur_y][cur_x].click()

        for x, y in self.__moves:
            temp_x, temp_y = cur_x + x, cur_y + y

            if 0 <= temp_x < self.n and \
                    0 <= temp_y < self.n and \
                    self.__board[temp_y][temp_x] == 0:
                if self.__solver(temp_x, temp_y, count + 1):
                    return True

        if count == self.n ** 2:
            return True

        self.__board[cur_y][cur_x] = 0
        if self.__onlineBoard:
            self.__onlineBoard[cur_y][cur_x].click()
        return False


if __name__ == '__main__':
    tour = Knight(5, 3, 2)
    tour.kTour()
