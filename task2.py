import sys
from global_alignment import *
from create_data_and_align import *

if __name__ == '__main__':
	L = int(sys.argv[1])
	create_data(L)
	seq1 = read_fasta("./task2/seq2.fasta")
	seq2 = read_fasta("./task2/seq3.fasta")
	sub_vals = read_sub_matrix("./task2/sub.txt")
	gap_penalty = -500

	aligned_seq1, aligned_seq2, score = align_sequence(seq1, seq2, sub_vals, gap_penalty)
	save_results(aligned_seq1, aligned_seq2, score, './task2/result.txt')

       
        
