"""
Author:			ARQUILITA, Jasper Ian Z.
Date:			May 13, 2016
Description:	A game of sudoku.
"""

#import functions and variables from other modules
from func import *
from board import *
import random

#prints the preset board using variables obtained in board.py
def createBoard():
	print()
	for a in range(0,14):
		if a == 0:
			for b in range(0,14):
				print(out_row[b], end = "")
			print()
		elif a == 1 or a == 5 or a == 9 or a == 13:
			for b in range(0,14):
				if b == 0:
					print(out_col[a], end = "")
				else:
					print("--", end = "")
			print()
		elif a == 2 or a == 3 or a == 4:
			for b in range(0,14):
				if b == 0:
					print(out_col[a], end = "")
				elif b == 2 or b == 3 or b == 4:
					print(" "+sq_val[a][b], end = "")
				elif b == 6 or b == 7 or b == 8:
					print(" "+sq_val[a][b], end = "")
				elif b == 10 or b == 11 or b == 12:
					print(" "+sq_val[a][b], end = "")
				else:
					print("--", end = "")
			print()
		elif a == 6 or a == 7 or a == 8:
			for b in range(0,14):
				if b == 0:
					print(out_col[a], end = "")
				elif b == 2 or b == 3 or b == 4:
					print(" "+sq_val[a][b], end = "")
				elif b == 6 or b == 7 or b == 8:
					print(" "+sq_val[a][b], end = "")
				elif b == 10 or b == 11 or b == 12:
					print(" "+sq_val[a][b], end = "")
				else:
					print("--", end = "")
			print()
		elif a == 10 or a == 11 or a == 12:
			for b in range(0,14):
				if b == 0:
					print(out_col[a], end = "")
				elif b == 2 or b == 3 or b == 4:
					print(" "+sq_val[a][b], end = "")
				elif b == 6 or b == 7 or b == 8:
					print(" "+sq_val[a][b], end = "")
				elif b == 10 or b == 11 or b == 12:
					print(" "+sq_val[a][b], end = "")
				else:
					print("--", end = "")
			print()

#initialize variables
i = "0"
sq = ""
ky = ""
ch = "0"
dif = "0"
rnd = 0
cont = 0
svch = "0"
numAns = ""
#ask username at start of game
user = getUser()
greet(user)
#main program - loops until user chooses 5 (Exit)
while ch != "5":
	#makes the user choose from the menu
	Menu(user)
	ch = input("Choice: ")
	if ch == "1":
		i = "0" #resets the variable
		#makes the user choose a difficulty
		dif = newAsk()
		#block of code only executes once after user chooses difficulty
		while dif != "1" or dif != "2" or dif != "3" or dif != "4":
			#executes if user chooses a difficulty (1,2,3)
			if dif == "1" or dif == "2" or dif == "3":
				#sets the files to be read according to difficulty
				if dif == "1":
					sq = "easy.txt"
					ky = "easykey.txt"
				elif dif == "2":
					sq = "med.txt"
					ky = "medkey.txt"
				elif dif == "3":
					sq = "hard.txt"
					ky = "hardkey.txt"
				#randomizes from 1 to 15 - chooses number of preset board
				rnd = random.randrange(0,14)
				#loads values according to difficulty and the random number
				sq_val = loadBoard(sq,rnd)
				ky_val = loadBoard(ky,rnd)
				GVN = genGiven(sq_val)
				#start of board game - only ends with two possibilities
				#1. user finishes game
				while sq_val != ky_val:
					#2. user exits game
					while i != "3":	
						#updates checking values, creates board, asks for an action (respectively)
						row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i = updnums(sq_val)					
						createBoard()
						actAsk()
						i = input("Enter Choice: ")
						#user chooses 1 to input an answer
						if i == "1":
							#Makes the user input a row and column
							inpRow = inputRow()
							inpCol = inputCol()
							inpXY = (inpRow, inpCol) #makes it an x,y pair inside a tuple
							#checks if row and column is an actual coordinate of the board
							if inpXY in XY:
								#checks if the row and column already contains a preset answer 
								if inpXY in GVN:
									print("Answer in specified coordinates is already given.")
								else:
									#makes user input an answer
									numAns = str(inputAns())
									#checks if number already exists as per sudoku rules
									#user unable to change answer for that coordinate for the reason below (inside print fxn)
									if checkAns(numAns,inpRow,inpCol,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
										print("Number already exists in the row, column, or square.")
									#user able to change answer
									else:
										sq_val[inpRow][inpCol] = numAns
										#checks if the user completed game
										#ignores and loops around if false
										if sq_val == ky_val:
											#adds the user to hall of fame and breaks to main menu if true	
											finGame(user)
											break
							else:
								print("Coordinates not valid.")
						#user chooses to save game
						elif i == "2":
							#converts the values and key of the current board into strings
							save = updSave(sq_val)
							keysave = updkeySave(ky_val)
							#writes the strings to their corresponding files	
							Save(save,keysave)
							print("\nGame Saved!")
						elif i == "3":
							#user chooses to give up, ends the current game
							gaveup(user)
						else:
							print("Choose a number from 1 to 3.")
					break	#breaks the choose action for current board
				break	#breaks to go to main menu
			elif dif == "4":
				#user backs, does not choose a difficulty
				break	#breaks to go to main menu
			else:
				#user inputs a wrong character
				print("Choose a number from 1 to 4.")
	elif ch == "2":
		#block of code executes only once
		while svch != "1" or svch != "2":
			#resets variables
			i = "0"			
			svch = "0"
			#yes or no
			svch = savedAsk()
			if svch == "1": #yes
				#same as game proper for new game
				rnd = random.randrange(0,1)
				sq_val = loadBoard("save.txt",rnd)
				ky_val = loadBoard("savekey.txt",rnd)
				GVN = genGiven(sq_val)
				while sq_val != ky_val:
					while i != "3":
						row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i = updnums(sq_val)						
						createBoard()
						actAsk()
						i = input("Enter Choice: ")
						if i == "1":
							inpRow = inputRow()
							inpCol = inputCol()
							inpXY = (inpRow, inpCol)
							if inpXY in XY: 
								if inpXY in GVN:
									print("Answer in specified coordinates is already given.")
								else:
									numAns = str(inputAns())
									if checkAns(numAns,inpRow,inpCol,row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, sqr_a, sqr_b, sqr_c, sqr_d, sqr_e, sqr_f, sqr_g, sqr_h, sqr_i):
										print("Number already exists in the row, column, or square.")
									else:
										sq_val[inpRow][inpCol] = numAns
										if sq_val == ky_val:	
											finGame(user)
											break
							else:
								print("Coordinates not valid.")
						elif i == "2":
							save = updSave(sq_val)
							keysave = updkeySave(ky_val)
							Save(save,keysave)
							print("\nGame Saved!")
						elif i == "3":
							gaveup(user)
						else:
							print("Choose a number from 1 to 3.")
					break #breaks the choose action
				break #breaks to main menu
			elif svch == "2": #no
				break #breaks to main menu
			else:
				print("Choose from 1 or 2")
	elif ch == "3":
		#reads the hof.txt file and prints the usernames inside
		viewHoF()
	elif ch == "4":
		#allows user to rechoose username, or if another person wants to play
		user = getUser()
		greet(user)
	elif ch == "5":
		#user exits game
		exit(user)
		break
	else:
		#user inputs invalid character
		print("Choose a number from 1 to 5.")
