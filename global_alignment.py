import re

## Read Fasta format DNA sequence
def read_fasta(filename):
    ## Ignore all non-letter characters after the first line
    r = re.compile(r'[^a-zA-Z0-9]', re.MULTILINE)
    lines = []
    
    with open(filename, "r") as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()
            
    seq = ''
    for line in lines:
        if line.startswith(">"):
            continue
        else:
            line = r.sub('',  line)
            seq  += line
            
    return list(seq)


## Read the substitution weight matrix
def read_sub_matrix(filename):
    
    sub_vals = {}
    with open(filename) as fp:
        line = fp.readline()
        items = line.split()
        line = fp.readline()
        while line:
            cur_vals = {}
            cur_items = line.split()
            cur_name = cur_items[0]
            for i in range(len(items)):
                cur_vals[items[i]] = int(cur_items[i + 1])
            sub_vals[cur_name] = cur_vals
            line = fp.readline()
    
    return sub_vals

## Global alignment of two sequences with dynamic programming
## based on the input substitution weight matrix and gap penalty
def align_sequence(seq1, seq2, sub_vals, gap_penalty):
    ##  Consts for recording the operations in each step
    RIGHT = 1
    DIAG = 0
    DOWN = -1
    
    m = len(seq1)
    n = len(seq2)

    dp = [[0 for i in range(m)] for j in range(n)]
    ops = [[0 for i in range(m)] for j in range(n)]

    ## Initialization for the first pair in two sequences
    dp[0][0] = sub_vals[seq1[0]][seq2[0]]
    ops[0][0] = DIAG

    ## Initialize the first row
    for i in range(m):
        if i == 0:
            continue
        dp[0][i] = dp[0][i - 1] + gap_penalty
        ops[0][i] = RIGHT

    ## Initialize the first column
    for i in range(m):
        if i == 0:
            continue
        dp[i][0] = dp[i - 1][0] + gap_penalty
        ops[i][0] = DOWN

    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                continue
            right = dp[i][j - 1] + gap_penalty
            down = dp[i - 1][j] + gap_penalty
            diag = dp[i - 1][j - 1] + sub_vals[seq2[i]][seq1[j]]

            ## Take the corresponding operation with the largest dp value
            if diag >= right and diag >= down:
                dp[i][j] = diag
                ops[i][j] = DIAG
            if right >= diag and right >= down:
                dp[i][j] = right
                ops[i][j] = RIGHT
            if down >= diag and down >= right:
                dp[i][j] = down
                ops[i][j] = DOWN

    ## Backtrack the operations to obtain the aligned sequences, in a reversed manner
    aligned_s1 = ""
    aligned_s2 = ""
    row = n - 1
    col = m - 1
    while row >= 0 or col >= 0:
        op = ops[row][col]
        if op == DIAG:
            aligned_s1 += seq1[col]
            aligned_s2 += seq2[row]
            row -= 1
            col -= 1
        if op == RIGHT:
            aligned_s1 += seq1[col]
            aligned_s2 += "-"
            col -= 1
        if op == DOWN:
            aligned_s1 += "-"
            aligned_s2 += seq2[row]
            row -= 1

    ## Reverse the sequences to obtain the aligned sequences
    aligned_s1 = aligned_s1[::-1]
    aligned_s2 = aligned_s2[::-1]
    score = dp[n - 1][m - 1]
    print('The optimal alignment between given sequences has score ' + str(score) + '.')
    print(aligned_s1)
    print(aligned_s2)

    return aligned_s1, aligned_s2, score

def save_results(seq1, seq2, score, filename):
    f = open(filename, 'w')
    f.write('The optimal alignment between given sequences has score ' + str(score) + '.\n')
    f.write(seq1 + '\n')
    f.write(seq2 + '\n')
    f.close()
    return


