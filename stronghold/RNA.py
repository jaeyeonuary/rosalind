#1 Perfect Matchings and RNA Secondary Structures
# background: RNA is single-stranded and can fold into three-dimensional structures
#             through intramolecular base pairing interactions (A-U, C-G)
#             RNA folding forms secondary structures that determine biological function
#             Predicting secondary structures helps infer protein function and identify potential biomarkers
# purpose: Calculate the total number of perfect matchings of base pair edges in the bonding graph of an RNA string
# approach: Count occurrences of A and C, then multiply their factorials
#           since each A must pair with exactly one U (and vice versa), giving a! * c! total matchings
# result: Total number of possible perfect matchings as an integer

import math

with open('C:\\python\\rosalind\\dataset\\rosalind_pmch.txt', 'r') as file1:
    data = file1.read()
seq1 = data.split('>')  # FASTA format
rna1 = seq1[1].splitlines()
s1 = ''.join(rna1[1:])

# If A1 pairs with U1, then A2 must pair with U2 — choices reduce by 1 each time, giving n! total
a = s1.count('A')
c = s1.count('C')

# Each pairing type is independent, so multiply the two factorials
result = math.factorial(a) * math.factorial(c)
print(result)


#2 Translating RNA into Protein
# background: During translation, ribosomes read mRNA in triplets called codons
#             Each codon encodes a specific amino acid based on the genetic code
#             Translation begins at AUG (start codon) and ends at UAA, UAG, or UGA (stop codons)
# purpose: Translate a given RNA string into its corresponding protein string
# approach: Read RNA in 3-nucleotide intervals, look up each codon in the codon table,
#           and stop translation when a stop codon is encountered
# result: A protein string composed of single-letter amino acid codes

with open('C:\\python\\rosalind\\dataset\\rosalind_prot.txt', 'r') as file2:
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
}  # source: Rosalind RNA codon table

protein2 = []  # to store translated amino acids
for i in range(0, len(s2), 3):  # read 3 nucleotides at a time
    codon2 = s2[i:i+3]
    amino2 = codon_table[codon2]  # translate codon to amino acid
    if amino2 == 'Stop':          # stop translation at stop codon
        break
    protein2.append(amino2)
print(''.join(protein2))          # join amino acids into protein string


#3 Inferring mRNA from Protein
# background: Due to the degeneracy of the genetic code, most amino acids are encoded
#             by multiple codons (e.g. Leucine has 6 codons, Methionine has only 1)
#             This means the same protein can be translated from different mRNA sequences
# purpose: Calculate the total number of distinct mRNA strings that could encode a given protein,
#          modulo 1,000,000 to handle large numbers
# approach: Count the number of codons for each amino acid, then multiply the counts
#           for each amino acid in the protein string, including stop codons (3 options)
#           Apply modulo at each step to prevent integer overflow
# result: Total number of possible mRNA strings modulo 1,000,000

with open('C:\\python\\rosalind\\dataset\\rosalind_mrna.txt', 'r') as file3:
    s3 = file3.read().strip()

aa_count = {}  # count the number of codons encoding each amino acid
for codon3, aa3 in codon_table.items():
    if aa3 not in aa_count:
        aa_count[aa3] = 0
    aa_count[aa3] += 1  # increment codon count for each amino acid

result = 1  # initialize result for multiplication
for amino3 in s3:
    result = (result * aa_count[amino3]) % 1000000  # apply modulo to prevent overflow
result = (result * aa_count['Stop']) % 1000000       # multiply by number of stop codons
print(result)


#4 RNA Splicing
# background: Pre-mRNA contains both exons (coding regions) and introns (non-coding regions)
#             During RNA splicing, introns are removed and exons are joined to form mature mRNA
#             This mature mRNA is then translated into a protein
# purpose: Remove intron sequences from a DNA string and translate the remaining exons into a protein
# approach: Parse FASTA input to extract the DNA sequence and intron sequences,
#           remove each intron using replace(), transcribe DNA to RNA, then translate to protein
# result: A protein string translated from the spliced mRNA sequence

with open('C:\\python\\rosalind\\dataset\\rosalind_splc.txt', 'r') as file4:
    s4 = file4.read()
data4 = s4.split('>')
name4 = data4[1].splitlines()  # parse header line
dna4 = ''.join(name4[1:])      # extract DNA sequence

introns = []  # list to store intron sequences
for block in data4[2:]:
    lines4 = block.splitlines()
    intron = ''.join(lines4[1:])  # extract intron sequence excluding header
    introns.append(intron)

for intron in introns:
    dna4 = dna4.replace(intron, '')  # remove introns from DNA sequence
rna4 = dna4.replace('T', 'U')       # transcribe DNA to RNA by replacing T with U

protein4 = []
for i in range(0, len(rna4), 3):
    codon = rna4[i:i+3]
    amino4 = codon_table[codon]  # translate codon to amino acid using codon table
    if amino4 == 'Stop':
        break
    protein4.append(amino4)
print(''.join(protein4))         # join amino acids into final protein string