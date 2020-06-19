import sys
import numpy as np

def sequence_alignment(d, seq1, seq2):

	# sequence alignment

	column = len(seq1)+1
	row = len(seq2)+1

	F = np.zeros([row, column], dtype=int) 

	# Adding zeros 
	for i in range(1,column):
		F[0][i] = i*d

	for i in range(1,row):
		F[i][0] = i*d

	for i in range(1,row):
		for j in range(1, column):
			value = 2
			
			if seq2[i-1] != seq1[j-1]:
				value = -2  

			F[i][j]	= max(F[i-1][j-1] + value, F[i-1][j] + d, F[i][j-1] + d)

	print (F)

	i = row-1
	j = column-1		

	alignment_seq1 = ""
	alignment_seq2 = ""

	while (i > 0 or j > 0):
		value = 2
		if seq2[i-1] != seq1[j-1]:
			value = -2  

		if (i>0 and j>0 and F[i][j] == F[i-1][j-1] + value):		
			alignment_seq1 = seq1[j-1] + alignment_seq1
			alignment_seq2 = seq2[i-1] + alignment_seq2
			i = i-1
			j = j-1

		elif (i>0 and F[i][j]==F[i-1][j]+d):
			alignment_seq1 = "-" + alignment_seq2	
			alignment_seq2 = seq2[i-1] + alignment_seq2
			i = i-1

		else:
			alignment_seq2 = "-" + alignment_seq2
			alignment_seq1 = seq1[j-1] + alignment_seq1
			j = j-1					
			
	print ()		
	print (alignment_seq1)
	print ()
	print (alignment_seq2)


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
	
	penalty = int(sys.argv[3])

	f1 = open(file1, "r")
	f2 = open(file2, "r")

	seq1 = get_sequence(f1)
	seq2 = get_sequence(f2)

	sequence_alignment(penalty, seq1, seq2)