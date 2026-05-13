#1 Perfect Matchings and RNA secondary structures based on RNA folding
'''
Introduction
- RNA is single-stranded and can fold into three-dimensional structures through intramolecular base pairing interactions.
- RNA folding forms secondary structures that determine biological function.
- Predicting the secondary structure of RNA helps infer protein function and identify potential biomarkers.
'''
import math # To calculate number of cases

with open('C:\\python\\rosalind\\dataset\\rosalind_pmch.txt', 'r') as file1:
    data = file1.read()
seq1 = data.split('>') # FASTA Format
rna1 = seq1[1].splitlines()
s1 = ''.join(rna1[1:])
'''
If an RNA has 2 adenine and 2 uracil, the matched pairs can be
(A1, U1) (A1, U2)
(A2, U1) (A2, U2)
= total 6 pairs
But, if A1 has matched with U1, U2 must be matched with A2
So in the same number of occurrences of 'A' as 'U' and 'C' as 'G',
the total number of perfect matchings is given by the following formula
'''

a = s1.count('A')
c = s1.count('C')

'''Each case is independent, so '*' was used.'''
result = math.factorial(a)*math.factorial(c)
print(result)

#2 Translating RNA into Protein
'''
Introduction
- Three continuous bases of RNA can be codon
- Combination of codon makes amino acid
- Combination of amino acid makes proteins
'''
with open ('C:\\python\\rosalind\\dataset\\rosalind_prot.txt', 'r') as file2:
    s2 = file2.read().strip()
codon_table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
} # from Rosalind

protein2 = [] # to store translated amino acid
for i in range(0, len(s2), 3): # interval = 3
    codon2 = s2[i:i+3] # read 3 nucleotides at a time
    amino2 = codon_table[codon2] # translate codon to amino acid
    if amino2 == 'Stop': # if read stop codon, translation must be stopped
        break
    protein2.append(amino2) # append amino acid to protein list
print(''.join(protein2)) # join amino acids into protein string

#3 Inferring mRNA from Protein
with open ('C:\\python\\rosalind\\dataset\\rosalind_mrna (2).txt', 'r') as file3:
    s3 = file3.read().strip()

aa_count = {} # count the number of codons encoding each amino acid
for codon3, aa3 in codon_table.items():
    if aa3 not in aa_count:
        aa_count[aa3] = 0
    aa_count[aa3] += 1 # increment codon count for each amino acid

result = 1 # initialize result for multiplication
for amino3 in s3:
    result = (result * aa_count[amino3]) % 1000000 # apply modulo to prevent overflow
result = (result * aa_count['Stop']) % 1000000

print(result)

#4 RNA Splicing
with open ('C:\\python\\rosalind\\dataset\\rosalind_splc.txt', 'r') as file4:
    s4 = file4.read()
data4 = s4.split('>')
name4 = data4[1].splitlines() # parse header line
dna4 = ''.join(name4[1:]) # extract DNA sequence

introns = [] # list to store intron sequences
for name4 in data4[2:]:
    lines4 = name4.splitlines()
    intron = ''.join(lines4[1:]) # extract intron sequence excluding header
    introns.append(intron) # add to introns

for intron in introns:
    dna4 = dna4.replace(intron, '') # remove introns from DNA sequence
rna4 = dna4.replace('T', 'U') # transcribe DNA to RNA by replacing T with U

protein4 = []
for i in range(0, len(rna4), 3):
    codon = rna4[i:i+3]
    amino4 = codon_table[codon] # translate codon to amino acid using codon table
    if amino4 == 'Stop':
        break
    protein4.append(amino4)
print(''.join(protein4)) # join amino acids into final protein string
