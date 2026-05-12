"""
Problem : Genome Assembly as Shortest Superstring (LONG)
Rosalind: https://rosalind.info/problems/long/

Approach:
    Greedy algorithm — repeatedly merge the pair of fragments with the
    longest overlap until a single superstring remains.
    At each iteration:
        1. Find the pair (i, j) with the maximum suffix-prefix overlap.
        2. Merge them: merged = fragments[i] + fragments[j][overlap:]
        3. Replace the two fragments with the merged string.

Time complexity: O(n^3 * k)  where n = number of fragments, k = fragment length
"""

import sys


def parse_fasta(text: str) -> list[str]:
    """Parse FASTA-formatted text and return a list of sequences."""
    sequences = []
    for block in text.split(">")[1:]:
        lines = block.splitlines()
        sequences.append("".join(lines[1:]))
    return sequences


def overlap_length(s: str, t: str) -> int:
    """Return the length of the longest suffix of s that matches a prefix of t."""
    max_len = min(len(s), len(t))
    for length in range(max_len, 0, -1):
        if s[-length:] == t[:length]:
            return length
    return 0


def shortest_superstring(fragments: list[str]) -> str:
    """Assemble fragments into the shortest superstring using a greedy approach."""
    while len(fragments) > 1:
        best_overlap = 0
        best_i, best_j = None, None

        for i in range(len(fragments)):
            for j in range(len(fragments)):
                if i != j:
                    ov = overlap_length(fragments[i], fragments[j])
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

    return fragments[0]


def main():
    input_file = "rosalind_long.txt"
    with open(input_file, "r") as f:
        data = f.read()

    fragments = parse_fasta(data)
    result = shortest_superstring(fragments)
    print(result)


if __name__ == "__main__":
    main()
