#!/usr/bin/python
import sys
import numpy as np

def substitution_matrix(file):
	next(file)  
	r_c = {}
	s = []
	i = 0

	for line in file: 
		if len(line.strip())!=0:
			line=line.rstrip('\n')

			r_c[line.split('\t')[0:1][0]] = i 
			i = i+1
			s.append(list(map(int,line.split('\t')[1:])))

	file.close()

	return r_c, s

def get_score(seq1, seq2):
	score = 0
	for i in range(len(seq1)):
		if seq1[i] == seq2[i]:
			print (s[r_c[seq2[i]]][r_c[seq1[i]]], end='', sep='')
			score = score + s[r_c[seq2[i]]][r_c[seq1[i]]]
		else:
			if seq1[i]=='-' or seq2[i]=='-':
				print ('(',d,')', end='', sep='')
				score = score + d
			else:
				print ('(',s[r_c[seq2[i]]][r_c[seq1[j]]] ,')', end='', sep='')		
				score = score + s[r_c[seq2[i]]][r_c[seq1[i]]]

		print ('+', end='', sep='')

	print("\b",end="") 		
	print ('=', score)					

def get_sequences(F, i, j):
	
	alignmented_seq1 = ""
	alignmented_seq2 = ""

	while (i > 0 or j > 0):

		if (i>0 and j>0 and F[i][j][1] == 'DIAG'):		
			alignmented_seq1 = seq1[j-1] + alignmented_seq1
			alignmented_seq2 = seq2[i-1] + alignmented_seq2
			i = i-1
			j = j-1

		elif (i>0 and F[i][j][1]=='UP'):
			alignmented_seq1 = "-" + alignmented_seq2	
			alignmented_seq2 = seq2[i-1] + alignmented_seq2
			i = i-1

		else:
			alignmented_seq2 = "-" + alignmented_seq2
			alignmented_seq1 = seq1[j-1] + alignmented_seq1
			j = j-1	   
			
	print ()		
	print (alignmented_seq1)
	print (alignmented_seq2)	
	get_score(alignmented_seq1, alignmented_seq2)


def global_alignment(F, i, j):

	number_roads = []

	diag = F[i-1][j-1][0] + s[r_c[seq2[i-1]]][r_c[seq1[j-1]]]
	up = F[i-1][j][0] + d
	left = F[i][j-1][0] + d

	F[i][j][0]	= max(diag, up, left)
	
	if F[i][j][0]==diag:
		#F[i][j][1] = 'DIAG'			
		number_roads.append('DIAG')

	if F[i][j][0]==up:	
		#F[i][j][1] = 'UP'
		number_roads.append('UP')
	
	if F[i][j][0]==left:	
		#F[i][j][1] = 'LEFT'
		number_roads.append('LEFT')
	
	for n in range(len(number_roads)):
		F[i][j][1] = number_roads[n]
		if i==row-1 and j==column-1:
			print ()
			print (F)
			get_sequences(F, i, j)
			return

		elif j<column-1:
			global_alignment(F, i ,j+1)	
		else:	
			global_alignment(F, i+1 ,1)							


if __name__ == "__main__":

	filename = sys.argv[1]	
	d = int(sys.argv[2])
	
	file = open(filename, "r")

	#Loading substitution matrix
	r_c, s = substitution_matrix(file)	

	seq1 = "AAG"
	seq2 = "AGC"	

	#identicalMatch = 1
	#mismatch = -1

	# zeros column and row at the beginning of matrix F
	column = len(seq1)+1
	row = len(seq2)+1

	F = np.zeros([row, column], dtype='i,O') 

	# Adding zeros 
	for i in range(1,column):
		F[0][i][0] = i*d
		F[0][i][1] = 'LEFT'

	for i in range(1,row):
		F[i][0][0] = i*d
		F[i][0][1] = 'UP'

	global_alignment(F, 1, 1)	