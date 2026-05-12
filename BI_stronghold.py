#1 Counting DNA nt
#
# Solution
# s1 = open('C:\\Users\\gjae9\\Downloads\\rosalind_dna.txt', 'r')
# seq1 = s_name,.read()
# print(seq.count('A'), seq.count('C'), seq.count('G'), seq.count('T'))

#2 Transcribing DNA to RNA
#
# Solution
# s2 = open('C:\\Users\\gjae9\\Downloads\\rosalind_rna.txt', 'r')
# seq2 = s2.read()
# rna = seq2.replace('T', 'U')
# print(rna)

#3 The Secondary and Tertiary Structures of DNA
#
# Solution
# s3 = open('C:\\Users\\gjae9\\Downloads\\rosalind_revc (1).txt', 'r')
# s3_seq = s3.read()
# trans = s3_seq.maketrans('ATCG', 'TAGC') *make change of letter to unicode
# seq3 = s3_seq.translate(trans) *translate s3_seq text
# print(seq3[::-1])

#4 Finding a Motif in DNA
#
# Solution
# file1 = open('C:\\Users\\gjae9\\Downloads\\rosalind_subs.txt', 'r')
# data1 = file1.read()
# line = data1.splitlines()
# s4 = line[0]
# t_name = line[1]
# pos = 0
# while pos < len(s4):
#     pos = s4.find(t_name, pos)
#     if pos == -1: #when t_name is not found in s4
#         break
#     print(pos + 1)
#     pos += 1 #start the next string

#5 Locating Restriction Sites
#
# Solution
# file2 = open('C:\\Users\\gjae9\\Downloads\\rosalind_revp (1).txt', 'r')
# data2 = file2.read()
# line2 = data2.splitlines()
# s5 = ''.join(line2[1:])
# def reverse(s5):
#     table = str.maketrans('ATGC', 'TACG')
#     return s5.translate(table)[::-1]
# def palindrome(s5):
#     return s5 == reverse(s5)
# for length in range(4, 13):
#     for i in range(len(s5) - length + 1): #sub should be short than s5
#         sub = s5[i:i+length]
#         if palindrome(sub):
#             print(i+1, length)

#6 Rabbits and Recurrence Relations
#
# Solutions
# def fib(n, k):
#     f = [0, 1, 1]
#     for i in range(3, n+1):
#         f.append(f[i-1]+f[i-2]*k)
#     return f[n]
    
# n, k = input().split()
# n, k = int(n), int(k)
# print(fib(n, k))

#7 Mortal Fibonacci Rabbits
#
# Solutions
# def fib_mortal(n, m):
#     ages = [0] * m
#     ages[0] = 1

#     for month in range(n-1):
#         newborns = sum(ages[1:])
#         ages = [newborns] + ages[:-1]
#     return sum(ages)

# n, m = input().split()
# n, m = int(n), int(m)
# print(fib_mortal(n, m))

#8 Computing GC Content
#
# Solutions
# file8 = open('C:\\Users\\gjae9\\Downloads\\rosalind_gc (3).txt', 'r')
# data8 = file8.read()
# gene8 = data8.split('>')
# max_gene = ''
# max_gc = 0
# for gene in gene9[1:]:
#     lines8 = gene.splitlines()
#     name = lines8[0]
#     seq = ''.join(lines8[1:])
#     gc = (seq.count('G') + seq.count('C')) / len(seq) * 100

#     if gc > max_gc :
#         max_gc = gc
#         max_gene = name

# print(max_gene)
# print(max_gc)

#9 Overlap Graphs
#
# Solutions
# file9 = open('C:\\Users\\gjae9\\Downloads\\rosalind_grph.txt', 'r')
# data9 = file9.read()
# gene9 = data9.split('>')
# genes = {}
# for gene in gene9[1:]:
#     lines9 = gene.splitlines()
#     name = lines9[0]
#     seq = ''.join(lines9[1:])
#     genes[name] = seq

# for s_name, s_seq in genes.items():
#     for t_name, t_seq in genes.items():
#         if s_name != t_name:
#             if s_seq[-3:] == t_seq[:3]:
#                 print(s_name, t_name)

#10 Genome Assembly as Shortest Superstring
#
# Solutions
file10 = open('C:\\Users\\gjae9\\Downloads\\rosalind_long.txt', 'r')
data10 = file10.read()
gene10 = data10.split('>')

fragments = []
for gene in gene10[1:]:
    line10 = gene.splitlines()
    seq = ''.join(line10[1:])
    fragments.append(seq)

def overlap(s, t):
    max_len = min(len(s), len(t))
    for length in range(max_len, 0, -1):
        if s[-length:] == t[:length]:
            return length
    return 0

while len(fragments) > 1:
    best_overlap = 0
    best_i, best_j = None, None
    
    for i in range(len(fragments)):
        for j in range(len(fragments)):
            if i != j:
                ov = overlap(fragments[i], fragments[j])
                if ov > best_overlap:
                    best_overlap = ov
                    best_i, best_j = i, j
    s = fragments[best_i]
    t = fragments[best_j]
    merged = s + t[best_overlap:]
    if best_i > best_j:
        fragments.pop(best_i)
        fragments.pop(best_j)
    else:
        fragments.pop(best_j)
        fragments.pop(best_i)
    fragments.append(merged)    

print(fragments[0])