#!/usr/bin/python
import sys
import matplotlib.pyplot as plt

def dot_matrix(windows, threshold, seq1, seq2):

	size1 = len(seq1)
	size2 = len(seq2)

	x_number_list = []
	y_number_list = []

	size1 = int(size1/windows)
	size2 = int(size2/windows)

	items = windows*(threshold/100)

	for i in range(size2):
		for j in range(size1):
			count = 0
			visited = [False]*windows

			for k in range(windows):
				v = 0
				for w in range(windows):

					if not visited[v] and seq2[i*windows + k] == seq1[j*windows + w]:
						count = count + 1
						visited[v] = True
						break

					v = v + 1	

			if count >= items:
				x_number_list.append(j+1)
				y_number_list.append(i+1)			


	plt.scatter(x_number_list, y_number_list, s=2)
	plt.title("Dot Matrix")
	plt.xlabel("seq1")
	plt.ylabel("seq2")
	plt.xlim(0, size1 + 1)
	plt.ylim(0, size2 + 1)
	plt.savefig('dox_matrix_'+str(windows_size) + '_'+ str(threshold)+'.png')
	plt.show()

def get_sequence(file):
	next(file)  
	seq = ""

	for linea in file: 
		if len(linea.strip())!=0:
			linea=linea.rstrip('\n')
			seq = seq + linea

	file.close()

	return seq

if __name__ == '__main__':
	
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	windows_size = int(sys.argv[3])
	threshold = int(sys.argv[4])

	f1 = open(file1, "r")
	f2 = open(file2, "r")

	seq1 = get_sequence(f1)
	seq2 = get_sequence(f2)

	#seq1 = "MSSSHSRCAQSAAVASPGKS"
	#seq2 = "MSSSHSRAGQSAAGAAPGGG"

	dot_matrix(windows_size, threshold, seq1, seq2)