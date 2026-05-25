#1 Counting DNA Nucleotides
# background: DNA is composed of four nucleobases: adenine(A), cytosine(C), guanine(G), and thymine(T)
#             The composition of these bases determines the genetic information encoded in the DNA
# purpose: Count the number of each nucleotide in a given DNA string
# approach: Read the DNA sequence and apply count() for each nucleotide
# result: Four integers separated by spaces representing counts of A, C, G, T respectively
with open('C:\\python\\rosalind\\dataset\\rosalind_dna.txt', 'r') as s1:
    seq1 = s1.read()
print(seq1.count('A'), seq1.count('C'), seq1.count('G'), seq1.count('T'))


#2 Transcribing DNA to RNA
# background: During transcription, DNA is converted to mRNA by RNA polymerase
#             Thymine(T) in DNA is replaced by Uracil(U) in RNA
# purpose: Simulate the transcription process by converting a DNA string to an RNA string
# approach: Replace all occurrences of 'T' with 'U' using replace()
# result: An RNA string corresponding to the given DNA string
with open('C:\\python\\rosalind\\dataset\\rosalind_rna.txt', 'r') as s2:
    seq2 = s2.read()
rna = seq2.replace('T', 'U')
print(rna)


#3 Complementing a Strand of DNA
# background: DNA is double-stranded, and each base pairs with its complement (A-T, C-G)
#             The reverse complement represents the opposite strand read in 5' to 3' direction
# purpose: Find the reverse complement of a given DNA string
# approach: Use maketrans() and translate() for simultaneous base substitution, then reverse with slicing
# result: The reverse complement string of the input DNA
with open('C:\\python\\rosalind\\dataset\\rosalind_revc.txt', 'r') as s3:
    s3_seq = s3.read()
trans = str.maketrans('ATCG', 'TAGC')
seq3 = s3_seq.translate(trans)
print(seq3[::-1])


#4 Finding a Motif in DNA
# background: A motif is a recurring sequence pattern that may indicate a functional region in DNA
#             Identifying motif locations is essential for understanding gene regulation
# purpose: Find all positions where a substring (motif) appears in a DNA string
# approach: Use find() with a sliding window to detect all occurrences including overlapping ones
# result: All 1-based positions where the motif appears in the DNA string
with open('C:\\python\\rosalind\\dataset\\rosalind_subs.txt', 'r') as file4:
    data4 = file4.read()
line = data4.splitlines()
s4 = line[0]
t_name = line[1]
pos = 0
while pos < len(s4):
    pos = s4.find(t_name, pos)
    if pos == -1:  # when t_name is not found in s4
        break
    print(pos + 1)
    pos += 1  # move one position to detect overlapping occurrences


#5 Locating Restriction Sites
# background: Restriction sites are palindromic DNA sequences recognized by restriction enzymes
#             A reverse palindrome reads the same on both strands in the 5' to 3' direction
# purpose: Identify all reverse palindromes of length 4 to 12 in a DNA string
# approach: Extract all substrings and check if each equals its reverse complement
# result: Position and length of every reverse palindrome found in the sequence
with open('C:\\python\\rosalind\\dataset\\rosalind_revp.txt', 'r') as file5:
    data5 = file5.read()
line5 = data5.splitlines()
s5 = ''.join(line5[1:])

def reverse_complement(s):
    table = str.maketrans('ATGC', 'TACG')
    return s.translate(table)[::-1]

def is_palindrome(s):
    return s == reverse_complement(s)

for length in range(4, 13):
    for i in range(len(s5) - length + 1):  # ensure substring stays within bounds
        sub = s5[i:i+length]
        if is_palindrome(sub):
            print(i+1, length)


#6 Rabbits and Recurrence Relations
# background: Population growth can be modeled using recurrence relations
#             Each pair of mature rabbits produces k pairs of offspring per generation
# purpose: Calculate the total number of rabbit pairs after n months given reproduction rate k
# approach: Use dynamic programming with a modified Fibonacci recurrence: F(n) = F(n-1) + F(n-2)*k
# result: Total number of rabbit pairs after n months
def fib(n, k):
    f = [0, 1, 1]
    for i in range(3, n+1):
        f.append(f[i-1] + f[i-2] * k)
    return f[n]

n, k = input().split()
n, k = int(n), int(k)
print(fib(n, k))


#7 Mortal Fibonacci Rabbits
# background: In reality, organisms have a finite lifespan
#             Rabbits that have lived for m months die, affecting total population size
# purpose: Calculate the number of rabbit pairs after n months when each rabbit lives for m months
# approach: Track rabbits by age group using a list; shift ages each month and remove those that exceed lifespan
# result: Total number of surviving rabbit pairs after n months
def fib_mortal(n, m):
    ages = [0] * m
    ages[0] = 1  # initialize with one newborn pair

    for month in range(n-1):
        newborns = sum(ages[1:])  # only mature rabbits reproduce
        ages = [newborns] + ages[:-1]  # age all rabbits by one month, oldest die
    return sum(ages)

n, m = input().split()
n, m = int(n), int(m)
print(fib_mortal(n, m))


#8 Computing GC Content
# background: GC content is the percentage of guanine and cytosine in a DNA sequence
#             Higher GC content indicates greater thermal stability of the DNA double helix
# purpose: Identify the DNA sequence with the highest GC content among multiple FASTA records
# approach: Parse FASTA format, calculate GC percentage for each sequence, track the maximum
# result: ID and GC content percentage of the sequence with the highest GC content
with open('C:\\python\\rosalind\\dataset\\rosalind_gc.txt', 'r') as file8:
    data8 = file8.read()
gene8 = data8.split('>')
max_gene = ''
max_gc = 0
for gene in gene8[1:]:
    lines8 = gene.splitlines()
    name = lines8[0]
    seq = ''.join(lines8[1:])
    gc = (seq.count('G') + seq.count('C')) / len(seq) * 100
    if gc > max_gc:
        max_gc = gc
        max_gene = name

print(max_gene)
print(max_gc)