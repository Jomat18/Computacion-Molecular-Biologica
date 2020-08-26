#!/usr/bin/python
import sys
import numpy as np

def save_result(F):
	f = open(result_file, "w")

	f.write('            ')
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

def get_sequences(F, i, j, alignmented_seq1 = "", alignmented_seq2 = ""):

	if F[i][j][0]==0:
		print ()		
		print (alignmented_seq1)
		print (alignmented_seq2)	
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


def local_alignment(F, i, j):

	value = identicalMatch
	if seq2[i-1] != seq1[j-1]:
		value = mismatch  

	directions = ''	

	diag = F[i-1][j-1][0] + value
	up = F[i-1][j][0] + d
	left = F[i][j-1][0] + d

	F[i][j][0]	= max(diag, up, left, 0)
	
	if F[i][j][0]==diag:
		directions = directions + 'D'
		#F[i][j][1] = 'D'	

	if F[i][j][0]==up:	
		directions = directions + 'U'
		#F[i][j][1] = 'U'
	
	if F[i][j][0]==left:
		directions = directions + 'L'	
		#F[i][j][1] = 'L'

	F[i][j][1] = directions
		
	if i==row-1 and j==column-1:
		save_result(F)

		major = -1000
		s_i = 0
		s_j = 0 
		for r in range(1,row):
			for c in range(1, column):
				if F[r][c][0]>=major:
					s_i = i
					s_j = j
					i = r
					j = c
					major = F[r][c][0]

		get_sequences(F, i, j)
		get_sequences(F, s_i, s_j)
		return

	if j<column-1:
		local_alignment(F, i ,j+1)	
	else:	
		local_alignment(F, i+1 ,1)


if __name__ == "__main__":

	d = int(sys.argv[1])

	result_file = "resultado.txt"
	
	identicalMatch = 1
	mismatch = -1	

	seq1 = "TGACTGAG"
	seq2 = "ATACTGGG"
	

	# zeros column and row at the beginning of matrix F
	column = len(seq1)+1
	row = len(seq2)+1

	F = np.zeros([row, column], dtype='i,O') 

	local_alignment(F, 1, 1)	