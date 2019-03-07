import sys
from global_alignment import *

if __name__ == '__main__':
	args = sys.argv
	filename1 = args[1]
	filename2 = args[2]
	sub_filename = args[3]
	gap_penalty = int(args[4])

	seq1 = read_fasta(filename1)
	seq2 = read_fasta(filename2)
	sub_vals = read_sub_matrix(sub_filename)

	aligned_seq1, aligned_seq2, score = align_sequence(seq1, seq2, sub_vals, gap_penalty)
	save_results(aligned_seq1, aligned_seq2, score, './task1/result.txt')

       
        
