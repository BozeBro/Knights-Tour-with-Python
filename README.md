# OnlineKnightsTour
I used Python to automate the Knight's Tour on http://www.maths-resources.com/knights/.
# ClassKnight.py
Uses the Backtracking algorithm, which utilizes dynamic programming and depth first search. Its runtime is O(k^N) where k is a constant and N is the size of the board
# RecDorff.py
Uses the Warnsdorff Heuristic(a shortcut) to solve the Knights Tour. The heuristic chooses squares/moves that has the least possible moves available to the square. This shortcut works so well in this case because all squares that can be reached by a few amount of squares are traversed through first so any backtracking is significantly reduced.
# Online.py
This program imports RecDorff and ClassKnight and will either( depending on user choice) and uses selenium to automate the process of clicking the squares. This program works only with the Chrome webdriver. 
# WebDriver
The webdriver used in program uses Chrome's webdriver. If you want to use another web browser, make sure to download the webdriver online and store it in PATH, otherwise you will get a geckodriver error.

You can use RecDorff or ClassKnight independently of Online if you want to see the board in your terminal instead of online
