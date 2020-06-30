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
			print (s[r_c[seq2[i]]][r_c[seq1[i]]], end='', sep='')
			score = score + s[r_c[seq2[i]]][r_c[seq1[i]]]
		else:
			if seq1[i]=='-' or seq2[i]=='-':
				print ('(',d,')', end='', sep='')
				score = score + d
			else:
				print ('(',s[r_c[seq2[i]]][r_c[seq1[i]]] ,')', end='', sep='')		
				score = score + s[r_c[seq2[i]]][r_c[seq1[i]]]

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

	diag = F[i-1][j-1][0] + s[r_c[seq2[i-1]]][r_c[seq1[j-1]]]
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

	filename = sys.argv[1]	
	d = int(sys.argv[2])
	result_file = "resultado.txt"
	
	file = open(filename, "r")

	#Loading substitution matrix
	r_c, s = substitution_matrix(file)	

	#seq1 = "AAG"
	#seq2 = "AGC"	

	seq1 = "AAAC"
	seq2 = "AGC"	

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

	#sys.getrecursionlimit()		
	global_alignment(F, 1, 1)	