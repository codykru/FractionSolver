#!/usr/bin/python3

#NOTE: Written for Python3, will not work on previous versions. 
#Cody Krukauskas
#U80598349 
#Advanced Python 
#FractionSolver.py 

import re 
from fractions import Fraction

patt = "(.*.)/(.) *(.) *(.*.)/(.)"	   #works with or without spaces 

while(True):

	s = input("Enter Your Problem, or press enter to quit: ")
	if not s:
		print("Thanks for playing!")
		break				#end program

	try: 
		problem = re.findall(patt,s)[0]						#get the input from user, grab first element
		X = Fraction(int(problem[0]), int(problem[1]))		#create fractions 
		Y = Fraction(int(problem[3]), int(problem[4]))

		operator = problem[2]		#grab the operator 

		opDict = {"+": X+Y, "-": X-Y, "*": X*Y, "/": X/Y} 

		result = opDict[operator]

		print("{0} {1} {2} = {3}".format(X,operator,Y,result))			#print operation.


	except ValueError:
		print("Please enter two fractions, seperated by an operator")
		print("examples: -1/2 * 3/4  , 1/2 + -3/4 \n")	

	except KeyError: 
		print("Invalid Operator! Valid operators are: *, -, +, /")

	except IndexError: 
		print("Make sure you have entered exactly two fractions.")

