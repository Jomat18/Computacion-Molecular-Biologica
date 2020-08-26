#!/usr/bin/python
import sys
import numpy as np

def save_result(F):
	f = open(result_file, "w")

	f.write('              ')
	for i in range(column-1):
		f.write(seq1[i]+'        ')

	f.write('\n')	

	seq2_t = ' '+ seq2

	for r in range(row):
		f.write(seq2_t[r])
		for c in range(column):			
			f.write(' ( '+ '{}'.format(F[r][c][0])+' '+'{}'.format(F[r][c][1])+') ')

		f.write('\n')
	f.close()	

	f = open(result_file, "r")
	print(f.read())


def get_score(seq1, seq2):
	score = 0
	for i in range(len(seq1)):
		if seq1[i] == seq2[i]:
			print (identicalMatch, end='', sep='')
			score = score + identicalMatch
		else:
			if seq1[i]=='-' or seq2[i]=='-':
				print ('(',d,')', end='', sep='')
				score = score + d
			else:
				print ('(',mismatch ,')', end='', sep='')		
				score = score + mismatch

		print ('+', end='', sep='')

	print("\b",end="") 		
	print ('=', score)	
 
			
def get_sequences(F, i, j, alignmented_seq1 = "", alignmented_seq2 = ""):

	if F[i][j][1]==0:
		print (alignmented_seq1)
		print (alignmented_seq2)
		get_score(alignmented_seq1, alignmented_seq2)
		print ()	
		return
			
	if len(F[i][j][1])>1:
		directions = F[i][j][1]
		for n in range(len(directions)):	
			F[i][j][1] = directions[n]
			get_sequences(F, i, j, alignmented_seq1, alignmented_seq2)			

	else:	
		
		if F[i][j][1] == 'D':		
			alignmented_seq1 = seq1[j-1] + alignmented_seq1
			alignmented_seq2 = seq2[i-1] + alignmented_seq2
			i = i-1
			j = j-1

		elif F[i][j][1]=='U':
			alignmented_seq1 = "-" + alignmented_seq2	
			alignmented_seq2 = seq2[i-1] + alignmented_seq2
			i = i-1

		else:
			alignmented_seq2 = "-" + alignmented_seq2
			alignmented_seq1 = seq1[j-1] + alignmented_seq1
			j = j-1

		get_sequences(F, i, j, alignmented_seq1, alignmented_seq2)			


def global_alignment(F, i, j):

	directions = ''

	value = identicalMatch
	if seq2[i-1] != seq1[j-1]:
		value = mismatch  

	diag = F[i-1][j-1][0] + value
	up = F[i-1][j][0] + d
	left = F[i][j-1][0] + d

	F[i][j][0]	= max(diag, up, left)
	
	if F[i][j][0]==left:	
		directions = directions + 'L'

	if F[i][j][0]==diag:
		directions = directions + 'D'

	if F[i][j][0]==up:	
		directions = directions + 'U'	
	
	F[i][j][1] = directions

	if i==row-1 and j==column-1:
		save_result(F)
		get_sequences(F, i, j)
		return

	elif j<column-1:
		global_alignment(F, i ,j+1)	
	else:	
		global_alignment(F, i+1 ,1)							


if __name__ == "__main__":

	d = int(sys.argv[1])
	result_file = "resultado.txt"

	identicalMatch = 1
	mismatch = -1

	#seq1 = "AAG"
	#seq2 = "AGC"	

	seq1 = "ATCG"	
	seq2 = "TTCG"

	# zeros column and row at the beginning of matrix F
	column = len(seq1)+1
	row = len(seq2)+1

	F = np.zeros([row, column], dtype='i,O') 

	# Adding zeros 
	for i in range(1,column):
		F[0][i][0] = i*d
		F[0][i][1] = 'L'

	for i in range(1,row):
		F[i][0][0] = i*d
		F[i][0][1] = 'U'

	global_alignment(F, 1, 1)	