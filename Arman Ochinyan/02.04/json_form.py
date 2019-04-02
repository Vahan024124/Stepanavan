#!/usr/bin/python3.5
import re
import ast
import sys
with open("db.py",'r') as js_text:

	str_text = js_text.read()

str_text = str_text.replace(" ", "")
str_text = str_text.replace("\n", "")
if str_text[0] != '{' or str_text[len(str_text)-1] !='}':
	print("Invalid j JSON")
	sys.exit()
temp = str_text[1:-2]
temp = temp.split(':') 

def check_sim(sim1,sim2,text):
	if text[0] == sim1 and text[-1] == sim2 and sim1 == '(' and sim2 == ')':
		return True
	elif text[0] == sim1 and text[-1] == sim2 and sim1 == '"' and sim2 == '"':
		
		return True

	
if temp[0].isdigit():
	a = False
	if check_sim('"','"',temp[1]):
		a = True
	elif temp[1].isdigit():
		a = True
	elif check_sim('(',')',temp[1]):
		a = True
	if a:
		print('Valid')	
	else:
		print('InValid')
elif isinstance(temp[0], str):

	if temp[0][0] == '"' and temp[0][-1] == '"':
		b = False
		if check_sim('"','"',temp[1]):
			b = True
		elif temp[1].isdigit():
			b = True
		elif check_sim('(',')',temp[1]):
			b = True
		if b:
			print('Valid')	
		else:
			print('InValid')
	elif check_sim('(',')',temp[1]):
		c = False
		if check_sim('"','"',temp[1]):
			c = True
		elif temp[1].isdigit():
			c = True
		elif check_sim('(',')',temp[1]):
			c = True
		if c:
			print('Valid')	
		else:
			print('InValid')
	else:
		print('InValid')
else:
	print('InValid')



