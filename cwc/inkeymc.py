from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import curses
from datetime import datetime

def init(): 
	# change 192.168.1.13 to 127.0.0.1 or your ip
	mc = Minecraft.create("127.0.0.1", 4711)
	x, y, z = mc.player.getPos()  
	return mc
	
def block(mx,x,y,z,m):
	#mc.player.setPos(0, 0, 0)
	x, y, z = mc.player.getPos()
	mc.postToChat("block")  
	mc.setBlock(x+1, y, z+1,m)
	
	
mc = init()
# get the curses screen window
screen = curses.initscr()
# turn off input echoing
curses.noecho()
# respond to keys immediately (don't wait for enter)
curses.cbreak()
# map arrow keys to special values
screen.keypad(True)
 
try:
	while True:
		x1, y1, z1 = mc.player.getPos()
		char = screen.getch()
		if char == ord('q'):
			break
		elif char == curses.KEY_RIGHT:
			block(mc,x1,y1,z1,8)
            # print doesn't work with curses, use addstr instead
			x = x + 1
			screen.addstr(0, 0, 'right')
		elif char == curses.KEY_LEFT:
			screen.addstr(0, 0, 'left ')       
		elif char == curses.KEY_UP:
			screen.addstr(0, 0, 'up   ')       
		elif char == curses.KEY_DOWN:
			screen.addstr(0, 0, 'down ')
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
