import sys
import numpy as np

def sequence_alignment(file, d, seq1, seq2):

	# Loading substitution F
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

	# sequence alignment

	column = len(seq1)+1
	row = len(seq2)+1

	F = np.zeros([row, column], dtype=int) 

	# Adding zeros 
	for i in range(1,column):
		F[0][i] = i*d

	for i in range(1,row):
		F[i][0] = i*d

	value = 2

	for i in range(1,row):
		for j in range(1, column):
			F[i][j]	= max(F[i-1][j-1] + s[r_c[seq2[i-1]]][r_c[seq1[j-1]]], F[i-1][j] + d, F[i][j-1] + d)

	print (F)

	i = row-1
	j = column-1		

	alignment_seq1 = ""
	alignment_seq2 = ""

	while (i > 0 or j > 0):

		if (i>0 and j>0 and F[i][j] == F[i-1][j-1] + s[r_c[seq2[i-1]]][r_c[seq1[j-1]]]):		
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


if __name__ == "__main__":
	filename = sys.argv[1]	
	penalty = int(sys.argv[2])
	
	file = open(filename, "r")

	seq1 = "AAG"
	seq2 = "AGC"	

	sequence_alignment(file, penalty, seq1, seq2)