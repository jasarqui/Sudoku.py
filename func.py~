"""
Module for most of the game's functions
"""
#import values from board.py
from board import *

#Function Definitions
#returns user's favored username
def getUser():
	print("\nEnter your desired username:")
	user = input("")
	return user
#prints a greeting
def greet(usn):
	print("\nHello,",usn+"!")
	print("Welcome to Sudoku!")
#prints the main menu
def Menu(usn):
	print("Choose an option below by entering its corresponding number.")
	print("[1] New Game")
	print("[2] Load Saved Game")
	print("[3] Hall of Fame")
	print("[4] Change Username")
	print("[5] Exit")
#prints a goodbye
def exit(usn):
	print("\nGoodbye,",usn+"!","\nThanks for playing!")
#prints a gave up message
def gaveup(usn):
	print("\n"+usn,"gave up.")
	print("Game exited to main menu.")	
#returns user's choice - load save game or not
def savedAsk():
	print("\nAre you sure you want to load saved game?")
	print("[1] Yes")
	print("[2] No")
	inp = input("Choice: ")
	return inp
#returns user's favored difficulty, or an exit
def newAsk():
	print("\nChoose a difficulty level.")
	print("[1] Easy")
	print("[2] Medium")
	print("[3] Hard")
	print("[4] Back")
	diff = input("Choice: ")
	return diff
#reads hof.txt and prints the usernames that lies within the file
def viewHoF():
	print("\nThe Hall of Fame")
	print("Here lies valiant few who finished the game!")
	hof = open("hof.txt","r")
	for line in hof:
		print(line[:-1])
	hof.close()
	print("\nSpecial hall of fame thanks to")
	print("www.puzzles.ca/sudoku.html")
	print()
#prints the action menu
def actAsk():
	print("[1] Input Answer")
	print("[2] Save Game")
	print("[3] Give Up")
#writes the strings converted to their corresponding files
def Save(save,keysave):
	fileSave = open("save.txt","w")
	fileSave.write(save)
	fileSave.close()
	keySave = open("savekey.txt","w")
	keySave.write(keysave)
	keySave.close()
#prints congrats, appends the username of the finisher to hof.txt
def finGame(usn):
	print("\nCongratulations,",usn+"!")
	print("You've been added to the Hall of Fame!")
	HoFAdd = open("hof.txt","a")
	HoFAdd.write(usn+"\n")
	HoFAdd.close()
#reads board values for preset and key, returns the line chosen by random number
def loadBoard(filename,x):
	brd = open(filename,"r")
	z = brd.readlines()
	brd.close()
	return updVal(z[x][:-1])
#splits the text recovered from the files and assigns them to their coordinates
#returns the dictionary where their coordinates were assigned to
def updVal(text):
	z = text.split(",")
	sq = {2:{2:z[0],3:z[1],4:z[2],6:z[9],7:z[10],8:z[11],10:z[18],11:z[19],12:z[20]}, 3:{2:z[3],3:z[4],4:z[5],6:z[12],7:z[13],8:z[14],10:z[21],11:z[22],12:z[23]}, 4:{2:z[6],3:z[7],4:z[8],6:z[15],7:z[16],8:z[17],10:z[24],11:z[25],12:z[26]}, 6:{2:z[27],3:z[28],4:z[29],6:z[36],7:z[37],8:z[38],10:z[45],11:z[46],12:z[47]}, 7:{2:z[30],3:z[31],4:z[32],6:z[39],7:z[40],8:z[41],10:z[48],11:z[49],12:z[50]}, 8:{2:z[33],3:z[34],4:z[35],6:z[42],7:z[43],8:z[44],10:z[51],11:z[52],12:z[53]}, 10:{2:z[54],3:z[55],4:z[56],6:z[63],7:z[64],8:z[65],10:z[72],11:z[73],12:z[74]}, 11:{2:z[57],3:z[58],4:z[59],6:z[66],7:z[67],8:z[68],10:z[75],11:z[76],12:z[77]}, 12:{2:z[60],3:z[61],4:z[62],6:z[69],7:z[70],8:z[71],10:z[78],11:z[79],12:z[80]}}
	return sq
#allows user to input their chosen row
#returns corresponding number for chosen row
def inputRow():
	#loops until a return is encountered
	while True:
		row = input("Cell Row: ")
		if row == "A" or row == "a":
			return 2
		elif row == "B" or row == "b":
			return 3
		elif row == "C" or row == "c":
			return 4
		elif row == "D" or row == "d":
			return 6
		elif row == "E" or row == "e":
			return 7
		elif row == "F" or row == "f":
			return 8
		elif row == "G" or row == "g":
			return 10
		elif row == "H" or row == "h":
			return 11
		elif row == "I" or row == "i":
			return 12
		else:
			print("Enter a row from A to I.")
#allows user to input their chosen column
#returns corresponding number for chosen column
def inputCol():
	#loops until a return is encountered
	while True:	
		col = input("Input Column: ")
		if col == "1":
			return 2
		elif col == "2":
			return 3
		elif col == "3":
			return 4
		elif col == "4":
			return 6
		elif col == "5":
			return 7
		elif col == "6":
			return 8
		elif col == "7":
			return 10
		elif col == "8":
			return 11
		elif col == "9":
			return 12
		else:
			print("Enter a column from 1 to 9.")
#allows user to choose their favored answer for that coordinate
#returns their answer
def inputAns():
	#loops until a return is encountered
	while True:
		ans = input("Input Answer: ")
		if ans == "1" or ans == "2" or ans == "3" or ans == "4" or ans == "5" or ans == "6" or ans == "7" or ans == "8" or ans == "9":
			return ans
		else:
			print("Enter a number from 1 to 9.")
#generates the values given for that preset board
#returns the list of x,y tuples given
def genGiven(val):
	GVN = []
	for x in range(2,5):
		for y in range(2,5):
			if val[x][y] not in str(range(1,10)):	  
				GVN.append((x,y))
			else:
				GVN = GVN
		for y in range(6,9):
			if val[x][y] not in str(range(1,10)):
				GVN.append((x,y))
			else:
				GVN = GVN
		for y in range(10,13):
			if val[x][y] not in str(range(1,10)):
				GVN.append((x,y))
			else:
				GVN = GVN
	for x in range(6,9):
		for y in range(2,5):
			if val[x][y] not in str(range(1,10)):
				GVN.append((x,y))
			else:
				GVN = GVN
		for y in range(6,9):
			if val[x][y] not in str(range(1,10)):
				GVN.append((x,y))
			else:
				GVN = GVN
		for y in range(10,13):
			if val[x][y] not in str(range(1,10)):
				GVN.append((x,y))
			else:
				GVN = GVN
	for x in range(10,13):
		for y in range(2,5):
			if val[x][y] not in str(range(1,10)):
				GVN.append((x,y))
			else:
				GVN = GVN
		for y in range(6,9):
			if val[x][y] not in str(range(1,10)):
				GVN.append((x,y))
			else:
				GVN = GVN
		for y in range(10,13):
			if val[x][y] not in str(range(1,10)):
				GVN.append((x,y))
			else:
				GVN = GVN
	return GVN
#checks row, column, and square of coordinate if user inputted answer already exists
#true if exists, false if not
def checkAns(x, y, z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
	if y == 2:
		if x in row_a:
			return True
		else:
			if checkCol(x,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
				return True
			else:
				if checkSQ(x,y,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
					return True
				else:
					return False
	elif y == 3:
		if x in row_b:
			return True
		else:
			if checkCol(x,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
				return True
			else:
				if checkSQ(x,y,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
					return True
				else:
						return False
	elif y == 4:
		if x in row_c:
			return True
		else:
			if checkCol(x,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
				return True
			else:
				if checkSQ(x,y,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
					return True
				else:
						return False
	elif y == 6:
		if x in row_d:
			return True
		else:
			if checkCol(x,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
				return True
			else:
				if checkSQ(x,y,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
					return True
				else:
					return False
	elif y == 7:
		if x in row_e:
			return True
		else:
			if checkCol(x,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
				return True
			else:
				if checkSQ(x,y,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
					return True
				else:
					return False
	elif y == 8:
		if x in row_f:
			return True
		else:
			if checkCol(x,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
				return True
			else:
				if checkSQ(x,y,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
					return True
				else:
					return False
	elif y == 10:
		if x in row_g:
			return True
		else:
			if checkCol(x,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
				return True
			else:
				if checkSQ(x,y,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
					return True
				else:
					return False
	elif y == 11:
		if x in row_h:
			return True
		else:
			if checkCol(x,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
				return True
			else:
				if checkSQ(x,y,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
					return True
				else:
					return False
	elif y == 12:
		if x in row_i:
			return True
		else:
			if checkCol(x,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
				return True
			else:
				if checkSQ(x,y,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
					return True
				else:
					return False
	else: 
		return False
#checks if user inputted answer already exists in its corresponding column
#returns true if exists, false if not
def checkCol(x,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
	if z == 2:
		if x in col_1:
			return True
		else:
			return False
	elif z == 3:
		if x in col_2:
			return True
		else:
			return False
	elif z == 4:
		if x in col_3:
			return True
		else:
			return False
	elif z == 6:
		if x in col_4:
			return True
		else:
			return False
	elif z == 7:
		if x in col_5:
			return True
		else:
			return False
	elif z == 8:
		if x in col_6:
			return True
		else:
			return False
	elif z == 10:
		if x in col_7:
			return True
		else:
			return False
	elif z == 11:
		if x in col_8:
			return True
		else:
			return False
	elif z == 12:
		if x in col_9:
			return True
		else:
			return False
	else:
		return False
#checks if user inputted value already exists in its corresponding square
#returns true if exists, false if not
def checkSQ(x,y,z,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
	if (y in range(2,5)) and (z in range(2,5)):
		if x in sqr_a:
			return True
		else:
			return False
	elif (y in range(2,5)) and (z in range(6,9)):
		if x in sqr_b:
			return True
		else:
			return False
	elif (y in range(2,5)) and (z in range(10,13)):
		if x in sqr_c:
			return True
		else:
			return False	
	elif (y in range(6,9)) and (z in range(2,5)):
		if x in sqr_d:
			return True
		else:
			return False
	elif (y in range(6,9)) and (z in range(6,9)):
		if x in sqr_e:
			return True
		else:
			return False
	elif (y in range(6,9)) and (z in range(10,13)):
		if x in sqr_f:
			return True
		else:
			return False
	elif (y in range(10,13)) and (z in range(2,5)):
		if x in sqr_g:
			return True
		else:
			return False
	elif (y in range(10,13)) and (z in range(6,9)):
		if x in sqr_h:
			return True
		else:
			return False
	elif (y in range(10,13)) and (z in range(10,13)):
		if x in sqr_i:
			return True
		else:
			return False
	else:
		return False
#converts the value of the current board to a string to be written in a file
def updSave(sq_val):
	return sq_val[2][2]+","+sq_val[2][3]+","+sq_val[2][4]+","+sq_val[3][2]+","+sq_val[3][3]+","+sq_val[3][4]+","+sq_val[4][2]+","+sq_val[4][3]+","+sq_val[4][4]+","+sq_val[2][6]+","+sq_val[2][7]+","+sq_val[2][8]+","+sq_val[3][6]+","+sq_val[3][7]+","+sq_val[3][8]+","+sq_val[4][6]+","+sq_val[4][7]+","+sq_val[4][8]+","+sq_val[2][10]+","+sq_val[2][11]+","+sq_val[2][12]+","+sq_val[3][10]+","+sq_val[3][11]+","+sq_val[3][12]+","+sq_val[4][10]+","+sq_val[4][11]+","+sq_val[4][12]+","+sq_val[6][2]+","+sq_val[6][3]+","+sq_val[6][4]+","+sq_val[7][2]+","+sq_val[7][3]+","+sq_val[7][4]+","+sq_val[8][2]+","+sq_val[8][3]+","+sq_val[8][4]+","+sq_val[6][6]+","+sq_val[6][7]+","+sq_val[6][8]+","+sq_val[7][6]+","+sq_val[7][7]+","+sq_val[7][8]+","+sq_val[8][6]+","+sq_val[8][7]+","+sq_val[8][8]+","+sq_val[6][10]+","+sq_val[6][11]+","+sq_val[6][12]+","+sq_val[7][10]+","+sq_val[7][11]+","+sq_val[7][12]+","+sq_val[8][10]+","+sq_val[8][11]+","+sq_val[8][12]+","+sq_val[10][2]+","+sq_val[10][3]+","+sq_val[10][4]+","+sq_val[11][2]+","+sq_val[11][3]+","+sq_val[11][4]+","+sq_val[12][2]+","+sq_val[12][3]+","+sq_val[12][4]+","+sq_val[10][6]+","+sq_val[10][7]+","+sq_val[10][8]+","+sq_val[11][6]+","+sq_val[11][7]+","+sq_val[11][8]+","+sq_val[12][6]+","+sq_val[12][7]+","+sq_val[12][8]+","+sq_val[10][10]+","+sq_val[10][11]+","+sq_val[10][12]+","+sq_val[11][10]+","+sq_val[11][11]+","+sq_val[11][12]+","+sq_val[12][10]+","+sq_val[12][11]+","+sq_val[12][12]+"\n"
#converts the key values of the current board to a string to be written in a file
def updkeySave(ky_val):
	return ky_val[2][2]+","+ky_val[2][3]+","+ky_val[2][4]+","+ky_val[3][2]+","+ky_val[3][3]+","+ky_val[3][4]+","+ky_val[4][2]+","+ky_val[4][3]+","+ky_val[4][4]+","+ky_val[2][6]+","+ky_val[2][7]+","+ky_val[2][8]+","+ky_val[3][6]+","+ky_val[3][7]+","+ky_val[3][8]+","+ky_val[4][6]+","+ky_val[4][7]+","+ky_val[4][8]+","+ky_val[2][10]+","+ky_val[2][11]+","+ky_val[2][12]+","+ky_val[3][10]+","+ky_val[3][11]+","+ky_val[3][12]+","+ky_val[4][10]+","+ky_val[4][11]+","+ky_val[4][12]+","+ky_val[6][2]+","+ky_val[6][3]+","+ky_val[6][4]+","+ky_val[7][2]+","+ky_val[7][3]+","+ky_val[7][4]+","+ky_val[8][2]+","+ky_val[8][3]+","+ky_val[8][4]+","+ky_val[6][6]+","+ky_val[6][7]+","+ky_val[6][8]+","+ky_val[7][6]+","+ky_val[7][7]+","+ky_val[7][8]+","+ky_val[8][6]+","+ky_val[8][7]+","+ky_val[8][8]+","+ky_val[6][10]+","+ky_val[6][11]+","+ky_val[6][12]+","+ky_val[7][10]+","+ky_val[7][11]+","+ky_val[7][12]+","+ky_val[8][10]+","+ky_val[8][11]+","+ky_val[8][12]+","+ky_val[10][2]+","+ky_val[10][3]+","+ky_val[10][4]+","+ky_val[11][2]+","+ky_val[11][3]+","+ky_val[11][4]+","+ky_val[12][2]+","+ky_val[12][3]+","+ky_val[12][4]+","+ky_val[10][6]+","+ky_val[10][7]+","+ky_val[10][8]+","+ky_val[11][6]+","+ky_val[11][7]+","+ky_val[11][8]+","+ky_val[12][6]+","+ky_val[12][7]+","+ky_val[12][8]+","+ky_val[10][10]+","+ky_val[10][11]+","+ky_val[10][12]+","+ky_val[11][10]+","+ky_val[11][11]+","+ky_val[11][12]+","+ky_val[12][10]+","+ky_val[12][11]+","+ky_val[12][12]+"\n"
#returns a list to update numbers for checking row, column, and square for a multiple assignment statement
def updnums(sq_val):
	return [sq_val[2][2],sq_val[2][3],sq_val[2][4],sq_val[2][6],sq_val[2][7],sq_val[2][8],sq_val[2][10],sq_val[2][11],sq_val[2][12]], [sq_val[3][2],sq_val[3][3],sq_val[3][4],sq_val[3][6],sq_val[3][7],sq_val[3][8],sq_val[3][10],sq_val[3][11],sq_val[3][12]], [sq_val[4][2],sq_val[4][3],sq_val[4][4],sq_val[4][6],sq_val[4][7],sq_val[4][8],sq_val[4][10],sq_val[4][11],sq_val[4][12]], [sq_val[6][2],sq_val[6][3],sq_val[6][4],sq_val[6][6],sq_val[6][7],sq_val[6][8],sq_val[6][10],sq_val[6][11],sq_val[6][12]], [sq_val[7][2],sq_val[7][3],sq_val[7][4],sq_val[7][6],sq_val[7][7],sq_val[7][8],sq_val[7][10],sq_val[7][11],sq_val[7][12]], [sq_val[8][2],sq_val[8][3],sq_val[8][4],sq_val[8][6],sq_val[8][7],sq_val[8][8],sq_val[8][10],sq_val[8][11],sq_val[8][12]], [sq_val[10][2],sq_val[10][3],sq_val[10][4],sq_val[10][6],sq_val[10][7],sq_val[10][8],sq_val[10][10],sq_val[10][11],sq_val[10][12]], [sq_val[11][2],sq_val[11][3],sq_val[11][4],sq_val[11][6],sq_val[11][7],sq_val[11][8],sq_val[11][10],sq_val[11][11],sq_val[11][12]], [sq_val[12][2],sq_val[12][3],sq_val[12][4],sq_val[12][6],sq_val[12][7],sq_val[12][8],sq_val[12][10],sq_val[12][11],sq_val[12][12]], [sq_val[2][2],sq_val[3][2],sq_val[4][2],sq_val[6][2],sq_val[7][2],sq_val[8][2],sq_val[10][2],sq_val[11][2],sq_val[12][2]], [sq_val[2][3],sq_val[3][3],sq_val[4][3],sq_val[6][3],sq_val[7][3],sq_val[8][3],sq_val[10][3],sq_val[11][3],sq_val[12][3]], [sq_val[2][4],sq_val[3][4],sq_val[4][4],sq_val[6][4],sq_val[7][4],sq_val[8][4],sq_val[10][4],sq_val[11][4],sq_val[12][4]], [sq_val[2][6],sq_val[3][6],sq_val[4][6],sq_val[6][6],sq_val[7][6],sq_val[8][6],sq_val[10][6],sq_val[11][6],sq_val[12][6]], [sq_val[2][7],sq_val[3][7],sq_val[4][7],sq_val[6][7],sq_val[7][7],sq_val[8][7],sq_val[10][7],sq_val[11][7],sq_val[12][7]], [sq_val[2][8],sq_val[3][8],sq_val[4][8],sq_val[6][8],sq_val[7][8],sq_val[8][8],sq_val[10][8],sq_val[11][8],sq_val[12][8]], [sq_val[2][10],sq_val[3][10],sq_val[4][10],sq_val[6][10],sq_val[7][10],sq_val[8][10],sq_val[10][10],sq_val[11][10],sq_val[12][10]], [sq_val[2][11],sq_val[3][11],sq_val[4][11],sq_val[6][11],sq_val[7][11],sq_val[8][11],sq_val[10][11],sq_val[11][11],sq_val[12][11]], [sq_val[2][12],sq_val[3][12],sq_val[4][12],sq_val[6][12],sq_val[7][12],sq_val[8][12],sq_val[10][12],sq_val[11][12],sq_val[12][12]], [sq_val[2][2],sq_val[2][3],sq_val[2][4],sq_val[3][2],sq_val[3][3],sq_val[3][4],sq_val[4][2],sq_val[4][3],sq_val[4][4]], [sq_val[2][6],sq_val[2][7],sq_val[2][8],sq_val[3][6],sq_val[3][7],sq_val[3][8],sq_val[4][6],sq_val[4][7],sq_val[4][8]], [sq_val[2][10],sq_val[2][11],sq_val[2][12],sq_val[3][10],sq_val[3][11],sq_val[3][12],sq_val[4][10],sq_val[4][11],sq_val[4][12]], [sq_val[6][2],sq_val[6][3],sq_val[6][4],sq_val[7][2],sq_val[7][3],sq_val[7][4],sq_val[8][2],sq_val[8][3],sq_val[8][4]], [sq_val[6][6],sq_val[6][7],sq_val[6][8],sq_val[7][6],sq_val[7][7],sq_val[7][8],sq_val[8][6],sq_val[8][7],sq_val[8][8]], [sq_val[6][10],sq_val[6][11],sq_val[6][12],sq_val[7][10],sq_val[7][11],sq_val[7][12],sq_val[8][10],sq_val[8][11],sq_val[8][12]], [sq_val[10][2],sq_val[10][3],sq_val[10][4],sq_val[11][2],sq_val[11][3],sq_val[11][4],sq_val[12][2],sq_val[12][3],sq_val[12][4]], [sq_val[10][6],sq_val[10][7],sq_val[10][8],sq_val[11][6],sq_val[11][7],sq_val[11][8],sq_val[12][6],sq_val[12][7],sq_val[12][8]], [sq_val[10][10],sq_val[10][11],sq_val[10][12],sq_val[11][10],sq_val[11][11],sq_val[11][12],sq_val[12][10],sq_val[12][11],sq_val[12][12]]
