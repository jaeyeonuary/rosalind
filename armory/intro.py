'''
Bioinformatics Armory
Using existing bioinformatics tools (Biopython, NCBI Entrez)
rather than implementing algorithms from scratch
'''

#1 Introduction to the Bioinformatics Armory
'''
Introduction
- Biopython is a Python library for biological computation
- Bio.Seq module provides tools for working with biological sequences
- Supports DNA, RNA, and protein sequence analysis
'''
from Bio.Seq import Seq
file1 = open('C:\\python\\rosalind\\dataset\\rosalind_ini.txt', 'r')
seq1 = file1.read()
seq1_A = seq1.count("A")
seq1_C = seq1.count("C")
seq1_G = seq1.count("G")
seq1_T = seq1.count("T")

print(seq1_A, seq1_C, seq1_G, seq1_T)

#2 GenBank Introduction
'''
Introduction
- GenBank is NCBI's genetic sequence database containing all publicly available sequences
- Entrez is NCBI's search engine accessible via Biopython's Bio.Entrez module
- esearch() allows programmatic access to GenBank without manual web searching
- Useful for tracking research trends of specific organisms over time
'''
from Bio import Entrez
file2 = open('C:\\python\\rosalind\\dataset\\rosalind_gbk.txt', 'r')
data2 = file2.readlines()
spc = data2[0].strip()
start = data2[1].strip()
end = data2[2].strip()

Entrez.email = 'gjae9900@naver.com'
handle2 = Entrez.esearch(
    db = "nucleotide",
    term = f"{spc.strip()}[Organism]",
    datetype = "pdat",
    mindate = start,
    maxdate = end
)

record2 = Entrez.read(handle2)
print(record2['Count'])

#3 Data Formats
'''
Introduction
- GenBank assigns unique accession IDs to every submitted sequence
- efetch() retrieves actual sequence data using accession IDs
- SeqIO.parse() converts raw FASTA data into iterable SeqRecord objects
- SeqRecord contains sequence, ID, description and other metadata
'''
from Bio import Entrez
from Bio import SeqIO
file3 = open('C:\\python\\rosalind\\dataset\\rosalind_frmt.txt', 'r')
data3 = file3.read().split()
Entrez.email = 'gjae9900@naver.com'
handle3 = Entrez.efetch(
    db = "nucleotide",
    id = ','.join(data3),
    rettype = "fasta",
    retmode = "text"
)

record3 = list(SeqIO.parse(handle3, "fasta"))
short = None
min3 = float('inf')
for seq3 in record3:
    if len(seq3) < min3:
        min3 = len(seq3)
        short = seq3

print(short.format("fasta"))

#4 FASTQ format introduction
'''
Introduction
- FASTQ format contains both nucleotide sequence and quality scores per base
- FASTQ is commonly used in next-generation sequencing (NGS) outputs (e.g. Illumina)
- Converting FASTQ to FASTA is necessary when tools only accept FASTA format (e.g. BLAST)
- Biopython SeqIO.parse() can read FASTQ and convert to FASTA without external tools
'''
from Bio import SeqIO
file4 = open('C:\\python\\rosalind\\dataset\\rosalind_tfsq.txt', 'r')
data4 = SeqIO.parse(file4, "fastq")
for data in data4:
    print(data.format("fasta"))