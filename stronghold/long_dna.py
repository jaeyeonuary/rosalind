#9 Overlap Graphs
file9 = open('C:\\python\\rosalind\\dataset\\rosalind_grph.txt', 'r')
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
            if s_seq[-3:] == t_seq[:3]:
                print(s_name, t_name)

#10 Genome Assembly as Shortest Superstring
file10 = open('C:\\python\\rosalind\\dataset\\rosalind_long.txt', 'r')
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