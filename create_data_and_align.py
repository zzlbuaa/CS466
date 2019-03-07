import random
import time

## Save a sequence to a Fasta format file 
def save_seq(seq, name):
    seq = ''.join(seq)
    f = open(name + '.fasta', 'w')
    f.write('>' + name + '\n')
    f.write(str(seq))
    f.close()

def random_change_seq(seq, L):
	return

def create_data(L):
    SWAP = 0
    DEL = 1
    random.seed(time.time())
    num2seq = {1 : 'A', 2 : 'T', 3 : 'C', 4 : 'G'}
    seq1 = []
    
    ## Create a random DNA sequence of lenth L 
    for i in range(L):
        seq1.append(num2seq[random.randint(1, 4)])
    
    ## Make (L/10) random changes (mutate or delete) to seq1 to get seq2
    seq2 = list(seq1)
    for i in range(L // 10):
        operation = random.randint(0, 1)
        pos1 = random.randint(0, len(seq2) - 1)
        if operation == SWAP:
            pos2 = random.randint(0, len(seq2) - 1)
            while pos2 == pos1:
                pos2 = random.randint(0, len(seq2) - 1)
            tmp = seq2[pos1]
            seq2[pos1] = seq2[pos2]
            seq2[pos2] = tmp
        if operation == DEL:
            del seq2[pos1]

    ## Make (L/10) random changes (mutate or delete) to seq1 to get seq3
    seq3 = list(seq1)
    for i in range(L // 10):
        operation = random.randint(0, 1)
        pos1 = random.randint(0, len(seq3) - 1)
        if operation == SWAP:
            pos2 = random.randint(0, len(seq3) - 1)
            while pos2 == pos1:
                pos2 = random.randint(0, len(seq3) - 1)
            tmp = seq3[pos1]
            seq3[pos1] = seq3[pos2]
            seq3[pos2] = tmp
        if operation == DEL:
            del seq3[pos1]
            
    save_seq(seq2, './task2/seq2')
    save_seq(seq3, './task2/seq3')
    
    
    return
            
    
    
