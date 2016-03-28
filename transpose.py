import subprocess
import msvcrt
import time
from colorama import Fore, Back, Style
from colorama import init

init()

notes_ex_d = ["do","do#","re","re#","mi","fa","fa#","sol","sol#","la","la#","si"]
notes_ex_b = ["do","reb","re","mib","mi","fa","solb","sol","lab","la","sib","si"]
notes_le_d = ["a","a#","b","c","c#","d","d#","e","f","f#","g","g#"]
notes_le_b = ["a","bb","b","c","db","d","eb","e","f","gb","g","ab"]
sharp_flat_le = ["a#","bb","c#","db","d#","eb","f#","gb","g#","ab"]
sharp_flat_ex = ["la#","sib","do#","reb","re#","mib","fa#","solb","sol#","lab"]

f = open("input.txt","r")
song = f.read().lower()

def sharpFlat(direction):
	global song
	subprocess.call("cls",shell=True)
	print("\tTRANSPOSE MUSIC!!\n\n")
	start = -1
	stop = -2
	verse = -2
	data1 = sharp_flat_le
	data2 = sharp_flat_ex
	if(direction == -1):
		start = 0
		stop = 1
		verse = 2
	for i,k in zip(data1[start::verse], data1[stop::verse]):
		replaceSingles(i,k)
	for i,k in zip(data2[start::verse], data2[stop::verse]):
		replaceSingles(i,k)
	print(song)
def replaceSingles(_from, to):
	global song
	song = song.replace(" "  + _from + " " , " "  + to + " ")
	song = song.replace(" "  + _from + "\n", " "  + to + "\n")
	song = song.replace("\n" + _from + " " , "\n" + to + " ")
	song = song.replace(" "  + _from + "-" , " "  + to + "-")
	song = song.replace(" "  + _from + "m" , " "  + to + "m")
	song = song.replace("\n" + _from + "-" , "\n" + to + "-")
	song = song.replace("\n" + _from + "m" , "\n" + to + "m")
	song = song.replace("\n" + _from + "sus" , "\n" + to + "sus")
	song = song.replace(" "  + _from + "sus" , " " + to + "sus")
	song = song.replace("\n" + _from + "4" , "\n" + to + "4")
	song = song.replace(" "  + _from + "4" , " " + to + "4")
	song = song.replace("\n" + _from + "7" , "\n" + to + "7")
	song = song.replace(" "  + _from + "7" , " " + to + "7")

	
	
def replaceNotes(idx, offset, arr):
	global song
	repl_idx = idx + offset
	if(offset > 0 ):
		if (repl_idx == len(arr)):
			repl_idx = 0
			to = arr[repl_idx].upper()
		else:
			to = arr[repl_idx]
	else:
		if (repl_idx == -1):
			repl_idx = len(arr)-1
			to = arr[repl_idx].upper()
		else:
			to = arr[repl_idx]
	_from = arr[idx]
	replaceSingles(_from, to)
 
def compute(offset):
	global notes_ex_d
	global song
	subprocess.call("cls",shell=True)
	print("\tTRANSPOSE MUSIC!!\n\n")
	
	if(offset < 0 ):
		mylist = enumerate(notes_ex_d)
	else:
		mylist = reversed(list(enumerate(notes_ex_d)))
	
	for idx, note in mylist:	
		replaceNotes(idx, offset, notes_ex_d)
		replaceNotes(idx, offset, notes_ex_b)
		replaceNotes(idx, offset, notes_le_d)
		replaceNotes(idx, offset, notes_le_b)
	song = song.lower()
	print(song)

compute(0)

done = False
while not done:
	key = ord(msvcrt.getch())
	if key == 27: #esc
		done = True
	elif key == 72: #up arrow
		compute(1)
	elif key == 80: #down arrow
		compute(-1)
	elif key == 77: #right arrow
		sharpFlat(1)
	elif key == 75: #left arrow
		sharpFlat(-1)
