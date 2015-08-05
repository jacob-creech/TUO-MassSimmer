import os
import csv
import sys
import time
import win32api
import win32con
from PIL import ImageOps
from PIL import ImageGrab

def get_play_area():
	TOP_LEFT_PIXELS = (192,190,167)
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
			if (im.getpixel((left + 1, top + 1)) == GREY_BORDER and
				im.getpixel((left + 2, top + 2)) == GREY_BORDER):
				top += 5
				left += 5
				
				return (left, top, left + SCREEN_WIDTH, top + SCREEN_HEIGH) 

	raise Exception("Play area not in view. " 
			"Make sure the game is visible on screen!")
		
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
	get_play_area()
	while True:
		run()
	
if __name__ == '__main__':
	main()