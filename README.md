# Rosalind Bioinformatics Problem Solutions

Solutions to bioinformatics problems from [Rosalind](https://rosalind.info/), implemented in Python.  
Each solution includes biological background, algorithmic approach, and clean code.

---

## Problem List

### Stronghold
| # | Description | Key Concepts |
|---|-------------|--------------|
| 1 | [Counting DNA Nucleotides](stronghold/dna.py) | String manipulation |
| 2 | [Transcribing DNA into RNA](stronghold/rna.py) | String replacement |
| 3 | [Complementing a Strand of DNA](stronghold/revc.py) | Reverse complement |
| 4 | [Rabbits and Recurrence Relations](stronghold/fib.py) | Dynamic programming |
| 5 | [Mortal Fibonacci Rabbits](stronghold/fibd.py) | Dynamic programming |
| 6 | [Computing GC Content](stronghold/gc.py) | FASTA parsing |
| 7 | [Finding a Motif in DNA](stronghold/subs.py) | String search |
| 8 | [Locating Restriction Sites](stronghold/revp.py) | Palindrome detection |
| 9 | [Perfect Matchings](stronghold/pmch.py) | Combinatorics, Factorial |
| 10 | [Translating RNA into Protein](stronghold/prot.py) | Codon table, Translation |
| 11 | [Inferring mRNA from Protein](stronghold/mrna.py) | Modular arithmetic |
| 12 | [RNA Splicing](stronghold/splc.py) | Intron/Exon, Translation |
| 13 | [Genome Assembly as Shortest Superstring](stronghold/long.py) | Greedy algorithm |

---

## Biological Background

This repository covers core concepts in bioinformatics:

- **Central Dogma**: DNA → RNA → Protein
- **RNA Secondary Structure**: Perfect matching and RNA folding
- **Genome Assembly**: Reconstructing sequences from fragments
- **RNA Splicing**: Removing introns and joining exons for translation

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
```

---

## Tech Stack

- **Language**: Python 3.12
- **Libraries**: `math`, `collections`

---

## Progress

- [x] Bioinformatics Stronghold (13/35)
- [ ] Bioinformatics Armory (0/30)
