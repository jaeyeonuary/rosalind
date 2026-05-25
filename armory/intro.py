'''
Bioinformatics Armory
Using existing bioinformatics tools (Biopython, NCBI Entrez)
rather than implementing algorithms from scratch
'''

#1 Introduction to the Bioinformatics Armory
# background: Biopython is a Python library for biological computation
#             Bio.Seq module provides tools for working with biological sequences
#             Supports DNA, RNA, and protein sequence analysis
# purpose: Count the number of each nucleotide (A, C, G, T) in a given DNA string
#          using Biopython as an introduction to the library
# approach: Read the DNA sequence and apply count() for each nucleotide
# result: Four integers separated by spaces representing counts of A, C, G, T respectively

from Bio.Seq import Seq

with open('C:\\python\\rosalind\\dataset\\rosalind_ini.txt', 'r') as file1:
    seq1 = file1.read().strip()

print(seq1.count("A"), seq1.count("C"), seq1.count("G"), seq1.count("T"))


#2 GenBank Introduction
# background: GenBank is NCBI's genetic sequence database containing all publicly available sequences
#             Entrez is NCBI's search engine accessible via Biopython's Bio.Entrez module
#             esearch() allows programmatic access to GenBank without manual web searching
#             Useful for tracking research trends of specific organisms over time
# purpose: Count the number of GenBank nucleotide entries for a given genus
#          published between two specified dates
# approach: Use Entrez.esearch() with organism name and date range filters,
#           then read the 'Count' field from the returned record
# result: An integer representing the number of matching GenBank entries

from Bio import Entrez

with open('C:\\python\\rosalind\\dataset\\rosalind_gbk.txt', 'r') as file2:
    data2 = file2.readlines()

spc = data2[0].strip()
start = data2[1].strip()
end = data2[2].strip()

Entrez.email = 'gjae9900@naver.com'
handle2 = Entrez.esearch(
    db="nucleotide",
    term=f"{spc}[Organism]",
    datetype="pdat",
    mindate=start,
    maxdate=end
)

record2 = Entrez.read(handle2)
print(record2['Count'])


#3 Data Formats
# background: GenBank assigns unique accession IDs to every submitted sequence
#             efetch() retrieves actual sequence data using accession IDs
#             SeqIO.parse() converts raw FASTA data into iterable SeqRecord objects
#             SeqRecord contains sequence, ID, description and other metadata
# purpose: Retrieve DNA sequences from GenBank using accession IDs
#          and return the shortest sequence in FASTA format
# approach: Fetch all sequences at once using comma-joined IDs,
#           parse with SeqIO, then find the shortest by comparing sequence lengths
# result: The shortest sequence among the retrieved records in FASTA format

from Bio import Entrez, SeqIO

with open('C:\\python\\rosalind\\dataset\\rosalind_frmt.txt', 'r') as file3:
    data3 = file3.read().split()

Entrez.email = 'gjae9900@naver.com'
handle3 = Entrez.efetch(
    db="nucleotide",
    id=','.join(data3),  # fetch all IDs in a single request
    rettype="fasta",
    retmode="text"
)

record3 = list(SeqIO.parse(handle3, "fasta"))
short = None
min3 = float('inf')
for seq3 in record3:
    if len(seq3) < min3:
        min3 = len(seq3)
        short = seq3

print(short.format("fasta"))


#4 FASTQ Format Introduction
# background: FASTQ format contains both nucleotide sequence and quality scores per base
#             Quality scores indicate the confidence of each base call during sequencing
#             FASTQ is commonly used in next-generation sequencing (NGS) outputs (e.g. Illumina)
#             Converting FASTQ to FASTA is necessary when tools only accept FASTA format (e.g. BLAST)
# purpose: Convert a FASTQ file to FASTA format by discarding quality score information
# approach: Use SeqIO.parse() with "fastq" format to read records,
#           then output each record in FASTA format using record.format()
# result: FASTA records corresponding to the input FASTQ sequences

from Bio import SeqIO

with open('C:\\python\\rosalind\\dataset\\rosalind_tfsq.txt', 'r') as file4:
    for data in SeqIO.parse(file4, "fastq"):
        print(data.format("fasta"))