import subprocess
import msvcrt
import time
from colorama import Fore, Back, Style
from colorama import init
numStatus = 4
status = 0

def initStatus():
	global status
	if status  == 0:
		print("Welcome, press enter to start or esc to exit")
	
	elif status  == 1:
		print("status {}".format(status))
	elif status  == 2:
		print("status {}".format(status))
	elif status  == 3:
		print("Process finished, press enter to close the application")

def manageEnter():
	global status
	print("enter")
	if(status + 1 < numStatus): #exit just if status = numStatus - 1 
		status += 1
		initStatus()
		return False
	else:
		return True
	
def manageEsc():
	global status
	print("esc")
	if(status > 0):	#exit just if status = 0
		status -= 1
		initStatus()
		return False
	else:
		return True
	
def manageSpacebar():
	global status
	print("space")
	return False
	
def manageDownArrow():
	global status
	print("down")
	return False
	
def manageUpArrow():
	global status
	print("up")
	return False
	
def manageLeftArrow():
	global status
	print("left")
	return False
	
def manageRightArrow():
	global status
	print("right")
	return False

subprocess.call("cls",shell=True)
print("\tTRANSPOSE MUSIC!!\n\n")
initStatus()
	
done = False
while not done:
	key = ord(msvcrt.getch())
	subprocess.call("cls",shell=True)
	print("\tTRANSPOSE MUSIC!!\n\n")
	if key == 27: #esc
		done = manageEsc()
	elif key == 72: #up arrow
		done = manageUpArrow()
	elif key == 80: #down arrow
		done = manageDownArrow()
	elif key == 77: #right arrow
		done = manageRightArrow()
	elif key == 75: #left arrow
		done = manageLeftArrow()
	elif key == 13: #enter
		done = manageEnter()
	elif key == 32: #spacebar
		done = manageSpacebar()
