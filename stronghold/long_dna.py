#9 Overlap Graphs
# background: In genome assembly, DNA is sequenced in short fragments called reads
#             An overlap graph connects reads that share a suffix-prefix match,
#             helping to determine the order of fragments in the original genome
# purpose: Construct an overlap graph by finding pairs of sequences where
#          the 3-character suffix of one matches the 3-character prefix of another
# approach: Store sequences in a dictionary, compare all pairs using string slicing,
#           and print directed edges where suffix-prefix overlap of length 3 exists
# result: Adjacency list of directed edges representing overlapping sequence pairs

with open('C:\\python\\rosalind\\dataset\\rosalind_grph.txt', 'r') as file9:
    data9 = file9.read()
gene9 = data9.split('>')
genes = {}
for gene in gene9[1:]:
    lines9 = gene.splitlines()
    name = lines9[0]
    seq = ''.join(lines9[1:])
    genes[name] = seq

for s_name, s_seq in genes.items():
    for t_name, t_seq in genes.items():
        if s_name != t_name:
            if s_seq[-3:] == t_seq[:3]:  # check 3-character suffix-prefix overlap
                print(s_name, t_name)


#10 Genome Assembly as Shortest Superstring
# background: In shotgun sequencing, a genome is broken into overlapping fragments
#             Reconstructing the original genome requires finding the shortest superstring
#             that contains all fragments as substrings
# purpose: Assemble all DNA fragments into the shortest possible superstring
#          representing the original chromosome
# approach: Greedy algorithm — repeatedly merge the pair of fragments with the longest
#           overlap until a single superstring remains
#           Remove larger index first when popping to avoid index shifting
# result: A shortest superstring containing all given DNA fragments

with open('C:\\python\\rosalind\\dataset\\rosalind_long.txt', 'r') as file10:
    data10 = file10.read()
gene10 = data10.split('>')

fragments = []
for gene in gene10[1:]:
    line10 = gene.splitlines()
    seq = ''.join(line10[1:])
    fragments.append(seq)

def overlap(s, t):
    """Return the length of the longest suffix of s that matches a prefix of t."""
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

    merged = fragments[best_i] + fragments[best_j][best_overlap:]

    # Remove larger index first to avoid index shifting
    if best_i > best_j:
        fragments.pop(best_i)
        fragments.pop(best_j)
    else:
        fragments.pop(best_j)
        fragments.pop(best_i)

    fragments.append(merged)

print(fragments[0])