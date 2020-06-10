from selenium import webdriver
import time
# from WarnsdorffChess import Warner
from ClassKnight import Knight
from RecDorff import *

driver = webdriver.Chrome()
driver.get('http://www.maths-resources.com/knights/')
time.sleep(1)
driver.fullscreen_window()
time.sleep(1)

# wait for elements to pop on the screen. Random time to wait.

posX = 23
posY = 0
cols, rows = 25, 25
n = 25

# Store online boxes in a list that will correspond to ClassKnight.__board
driver.find_element_by_id('autoMove').click()

driver.find_element_by_id('rankX').clear()
driver.find_element_by_id('rankX').send_keys(f'{rows}')

driver.find_element_by_id('rankY').clear()
driver.find_element_by_id('rankY').send_keys(f'{cols}')

driver.find_element_by_id('set').click()

onlineBoard = [[driver.find_element_by_id('c' + str(col) + 'x' + str(row))
                for row in range(rows)]
               for col in range(cols)]


'''
tour = Knight(n, scraper=onlineBoard)
tour.kTour()
'''
# Warner(posX, posY, n=n, online=onlineBoard)
dorffer(posX, posY, cols, rows, oBoard=onlineBoard)

k = input('you done?')
driver.quit()
