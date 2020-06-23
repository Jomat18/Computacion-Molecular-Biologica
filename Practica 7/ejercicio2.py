#!/usr/bin/python
import sys
import numpy as np

def local_alignment(d, seq1, seq2):

	for i in range(1,row):
		for j in range(1, column):
			value = identicalMatch
			
			if seq2[i-1] != seq1[j-1]:
				value = mismatch  

			F[i][j]	= max(F[i-1][j-1] + value, F[i-1][j] + d, F[i][j-1] + d, 0)


	print ()
	print (F)		

	mayor = -1000
	i = 0
	j = 0
	for r in range(1,row):
		for c in range(1, column):
			if F[r][c]>mayor:
				i = r
				j = c
				mayor = F[r][c]

	alignmented_seq1 = ""
	alignmented_seq2 = ""

	# sequences alignment
	while (i > 0 or j > 0):

		value = identicalMatch
		if seq2[i-1] != seq1[j-1]:
			value = mismatch  

		if (i>0 and j>0 and F[i][j] == F[i-1][j-1] + value):		
			alignmented_seq1 = seq1[j-1] + alignmented_seq1
			alignmented_seq2 = seq2[i-1] + alignmented_seq2
			i = i-1
			j = j-1

		elif (i>0 and F[i][j]==F[i-1][j]+d):
			alignmented_seq1 = "-" + alignmented_seq2	
			alignmented_seq2 = seq2[i-1] + alignmented_seq2
			i = i-1

		else:
			alignmented_seq2 = "-" + alignmented_seq2
			alignmented_seq1 = seq1[j-1] + alignmented_seq1
			j = j-1	

		if F[i][j]==0:
			break	


	print ()		
	print (alignmented_seq1)
	print ()
	print (alignmented_seq2)			


def get_sequence(file):
	next(file)  
	seq = ""

	for linea in file: 
		if len(linea.strip())!=0:
			linea=linea.rstrip('\n')
			seq = seq + linea

	file.close()

	return seq		


if __name__ == "__main__":

	file1 = sys.argv[1]
	file2 = sys.argv[2]	
	
	d = int(sys.argv[3])

	identicalMatch = 2
	mismatch = -2

	f1 = open(file1, "r")
	f2 = open(file2, "r")

	seq1 = get_sequence(f1)
	seq2 = get_sequence(f2)

	column = len(seq1)+1
	row = len(seq2)+1

	F = np.zeros([row, column], dtype=int) 

	local_alignment(d, seq1, seq2)	