import os
import csv
import sys
import time
import win32api
import win32con
from PIL import ImageOps
from PIL import ImageGrab
from random import randint
import coord as Coord
from coord import *

x_pad = 1085
y_pad = 527

per_adjust = 1.46

def left_click():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	print "click"
	
def mouse_pos(coord):
	win32api.SetCursorPos((x_pad + coord[0], y_pad + coord[1]))
	
def get_coords():
	x,y = win32api.GetCursorPos()
	x = x * per_adjust - x_pad
	y = y * per_adjust - y_pad
	print x,y
	
def random_coords(coord_set):
	x_start, y_start, x_end, y_end = coord_set
	x_pos = randint(x_start, x_end)
	y_pos = randint(y_start, y_end)
	return x_pos, y_pos
	
	
def get_play_area():
	TOP_LEFT_PIXELS = (62,50,45)
	GREY_BORDER = (0,0,0)
	SCREEN_WIDTH = 1200
	SCREEN_HEIGH = 900

	im = ImageGrab.grab()
	imageWidth, imHeight = im.size
	imageArray = im.getdata()

	for index, pixel in enumerate(imageArray):
		if pixel == TOP_LEFT_PIXELS:
			# getdata returns a flat array, so the below figures out
			# the 2d coords based on the index position.
			top = (index / imageWidth)
			left = (index % imageWidth)	
			x_pad = left - 1
			y_pad = top - 1
			return (x_pad, y_pad - 1, left + SCREEN_WIDTH, top + SCREEN_HEIGH) 

	raise Exception("Play area not in view. " 
			"Make sure the game is visible on screen!")
		
		
def choose_player():
	mouse_pos(random_coords(Coord.pvp[randint(0,5)]))
	left_click()
		
def find_state():
	'''
	Iterates through possible states and finds
	current state. With current state set, make
	next decision.
	
	Possible states: Battle, Loss, Win, Menu, 
	DailyWin, Mission.
	
	'''
	pass
		
		
def run():
	find_state()
	pass
		
def main():
	#get_play_area()
	#get_coords()
	#mouse_pos(random_coords(Coord.menu_mission))
	#box = get_play_area()
	#im = ImageGrab.grab(box)
	while True:
		run()
	
if __name__ == '__main__':
	main()