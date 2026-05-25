# Rosalind Bioinformatics Problem Solutions

Solutions to bioinformatics problems from [Rosalind](https://rosalind.info/), implemented in Python.  
Each solution includes biological background, purpose, approach, and clean code.

---

## Problem List

### Stronghold
Algorithms implemented from scratch to solve core bioinformatics problems.

#### [basic_DNA.py](stronghold/basic_DNA.py) — DNA sequence analysis fundamentals
| # | Description | Key Concepts |
|---|-------------|--------------|
| 1 | Counting DNA Nucleotides | String manipulation |
| 2 | Transcribing DNA into RNA | Transcription, String replacement |
| 3 | Complementing a Strand of DNA | Reverse complement |
| 4 | Rabbits and Recurrence Relations | Dynamic programming |
| 5 | Mortal Fibonacci Rabbits | Dynamic programming |
| 6 | Finding a Motif in DNA | String search, Sliding window |
| 7 | Locating Restriction Sites | Palindrome detection |
| 8 | Computing GC Content | FASTA parsing |

#### [long_DNA.py](stronghold/long_DNA.py) — Graph-based DNA assembly
| # | Description | Key Concepts |
|---|-------------|--------------|
| 9 | Overlap Graphs | Graph theory, Suffix-prefix matching |
| 10 | Genome Assembly as Shortest Superstring | Greedy algorithm |

#### [RNA.py](stronghold/RNA.py) — RNA structure and protein translation
| # | Description | Key Concepts |
|---|-------------|--------------|
| 1 | Perfect Matchings and RNA Secondary Structures | Combinatorics, Factorial |
| 2 | Translating RNA into Protein | Codon table, Translation |
| 3 | Inferring mRNA from Protein | Modular arithmetic |
| 4 | RNA Splicing | Intron/Exon, Translation |

### Armory
Solving bioinformatics problems using existing tools (Biopython, NCBI Entrez).

#### [intro.py](armory/intro.py) — Introduction to Biopython and NCBI tools
| # | Description | Key Concepts |
|---|-------------|--------------|
| 1 | Introduction to the Bioinformatics Armory | Biopython, Bio.Seq |
| 2 | GenBank Introduction | NCBI Entrez, esearch() |
| 3 | Data Formats | efetch(), SeqIO, FASTA |
| 4 | FASTQ Format Introduction | FASTQ, NGS, Format conversion |

---

## Biological Background

This repository covers core concepts in bioinformatics:

- **Central Dogma**: DNA → RNA → Protein
- **RNA Secondary Structure**: Perfect matching and RNA folding
- **Genome Assembly**: Reconstructing sequences from overlapping fragments
- **RNA Splicing**: Removing introns and joining exons for translation
- **Database Access**: Retrieving sequences from NCBI GenBank programmatically

---

## How to Run

1. Clone the repository
```bash
git clone https://github.com/jaeyeonuary/rosalind.git
```

2. Download input dataset from [Rosalind](https://rosalind.info/) and place it in `dataset/`

3. Run each solution
```bash
python stronghold/dna.py
python armory/gbk.py
```

---

## Tech Stack

- **Language**: Python 3.12
- **Libraries**: `math`, `collections`, `Biopython`

---

## Progress

- [x] Bioinformatics Stronghold (14/35)
- [x] Bioinformatics Armory (4/30)

### File Structure
```
rosalind/
├── stronghold/
│   ├── basic_DNA.py    # Problems 1-8: DNA sequence analysis
│   ├── long_DNA.py     # Problems 9-10: Graph-based DNA assembly
│   └── RNA.py          # Problems 1-4: RNA structure and translation
└── armory/
    └── intro.py        # Problems 1-4: Biopython and NCBI tools
```