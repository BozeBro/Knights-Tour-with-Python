import time
import argparse
from selenium import webdriver
from ClassKnight import Knight
import RecDorff
parser = argparse.ArgumentParser(description='Knights Tour variables')
parser.add_argument('-x', '--posX', type=int, default=0, metavar='', help='x position of the knight')
parser.add_argument('-y', '--posY', type=int, default=0, metavar='', help='y position of the knight')
parser.add_argument('-c', '--cols', type=int, default=8, metavar='', help='Height of the board')
parser.add_argument('-r', '--rows', type=int, default=8, metavar='', help='Length of the board')
parser.add_argument('-n', '--n', type=int, default=None, metavar='', help='square length of board if assigned')
parser.add_argument('-a', '--algorithm', type=int, default=1,
                    metavar='', help='Backtracking=0, \n '
                                     'Warnsdorff Recursive Heuristic=1')
args = parser.parse_args()

driver = webdriver.Chrome()
URL = 'http://www.maths-resources.com/knights/'
driver.get(URL)
driver.fullscreen_window()

if args.n:
    args.cols = args.row = args.n
# n for if it is square. cols, rows give more control of size.


driver.find_element_by_id('autoMove').click()

driver.find_element_by_id('rankX').clear()
driver.find_element_by_id('rankX').send_keys(f'{args.rows}')

driver.find_element_by_id('rankY').clear()
driver.find_element_by_id('rankY').send_keys(f'{args.cols}')

driver.find_element_by_id('set').click()

onlineBoard = [[driver.find_element_by_id('c' + str(col) + 'x' + str(row))
                for row in range(args.rows)]
               for col in range(args.cols)]

# Store online boxes in a list that will correspond to ClassKnight.__board

if args.algorithm == 0:
    tour = Knight(args.rows, args.cols, args.n, scraper=onlineBoard)
    tour.kTour()
elif args.algorithm == 1:
    RecDorff.dorffer(args.posX, args.posY, args.cols, args.rows, oBoard=onlineBoard)
