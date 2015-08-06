import os
import csv
import sys
import time
import win32api
import win32con
import array
from PIL import ImageOps
from PIL import ImageGrab
from random import randint
from random import uniform
import coord as Coord
from coord import *
from numpy import *

x_pad = 1085
y_pad = 527
win = 0
lose = 0
quit = False


per_adjust = 1.46

def left_click():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	
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

def count_nonblack_pil(img):
	img = ImageOps.grayscale(img)
	a = array(img.getcolors())
	a = a.sum()
	return a
	
def convert_box(box):
	x,y,x_end,y_end = box
	box = (x+x_pad, y+y_pad, x_end+x_pad, y_end+y_pad)
	return box
	
def get_state(box):
	im = ImageGrab.grab(convert_box(box))
	return count_nonblack_pil(im)
		
def choose_player():
	mouse_pos(random_coords(Coord.pvp[randint(0,5)]))
	left_click()

def battle():
	if get_state(Coord.battle_auto) != 33235:
		mouse_pos(random_coords(Coord.battle_auto))
		left_click()
		time.sleep(uniform(.5,2.0))
	mouse_pos(random_coords(Coord.battle_skip))
	left_click()
	
def end_battle():
	mouse_pos(random_coords(Coord.battle_end))
	left_click()

def end_daily_win():
	mouse_pos(random_coords(Coord.state_daily_win))
	left_click()
	
def end_stam():
	mouse_pos(random_coords(Coord.state_stam_out))
	left_click()
	
def resume():
	mouse_pos(random_coords(Coord.menu_mission))
	left_click()
	time.sleep(4)
	mouse_pos(random_coords(Coord.menu_battle))
	
def go_to_menu():
	mouse_pos(random_coords(Coord.state_invalid))
	left_click()
	time.sleep(2)
	resume()

def find_state():
	'''
	Iterates through possible states and finds
	current state. With current state set, make
	next decision.
	
	Possible states: Battle, Loss, Win, Menu, 
	DailyWin, Mission.
	
	'''
	global win, lose, quit
	print "pvp:    " + str(get_state(Coord.state_pvp)) + ", " + "7221"
	print "battle: " + str(get_state(Coord.state_battle)) + ", " + "4700"
	print "win:    " + str(get_state(Coord.state_win)) + ", " + "1597"
	print "lose:   " + str(get_state(Coord.state_lose)) + ", " + "18695"
	print
	if get_state(Coord.state_pvp) == 7221:
		choose_player()
	elif get_state(Coord.state_battle) == 4700:
		battle()
	elif get_state(Coord.state_win) == 513:
		win = win + 1
		print "Wins : " + str(win)
		print "Loses: " + str(lose)
		print "%    : " + str(((win * 1.0 /(win+lose)) * 100.0))
		end_battle()
	elif get_state(Coord.state_lose) == 18695:
		lose = lose + 1
		print "Wins : " + str(win)
		print "Loses: " + str(lose)
		print "%    : " + str(((win * 1.0 /(win+lose)) * 100.0))
		end_battle()
	elif get_state(Coord.state_daily_win) == 31261:
		end_daily_win()
	elif get_state(Coord.state_stam_out) == 23211:
		end_stam()
		time.sleep(randint(3600, 7200))
		resume()
	elif get_state(Coord.state_invalid) == 25685:
		go_to_menu()
	else:
		print "no state found"
		quit = True
		
		
		
def run():
	find_state()
	time.sleep(uniform(.5,2.0))
		
def main():
	global quit
	#get_play_area()
	#get_coords()
	#mouse_pos(random_coords(Coord.menu_mission))
	box = get_play_area()
	#box = convert_box(Coord.state_invalid)
	#im = ImageGrab.grab(box)
	#im.save(os.getcwd() + '\\Snap__' + str(int(time.time())) + '.png', 'PNG')
	#print count_nonblack_pil(im)
	while not quit:
		run()
	im = ImageGrab.grab(box)
	im.save(os.getcwd() + '\\Snap__' + str(int(time.time())) + '.png', 'PNG')
	
if __name__ == '__main__':
	main()