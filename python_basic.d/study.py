#! /usr/bin/env python
"""
# Rosalind problem solve
# Complementing a Strand of DNA
DNA_seq = 'AAAACCGGT'
DNA_seq = DNA_seq.lower()
DNA_seq = DNA_seq.replace('a','T')
DNA_seq = DNA_seq.replace('c','G')
DNA_seq = DNA_seq.replace('t','A')
DNA_seq = DNA_seq.replace('g','C')
print(DNA_seq[::-1])

#Computing GC Content
Rosalind_6404="CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"
Rosalind_5959="CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC"
Rosalind_0808="CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"

d_GC = {'Rosalind_6404':((Rosalind_6404.count('G')+Rosalind_6404.count('C'))/len(Rosalind_6404))*100,
'Rosalind_5959':((Rosalind_5959.count('G')+Rosalind_5959.count('C'))/len(Rosalind_5959)*100),
'Rosalind_0808':((Rosalind_0808.count('G')+Rosalind_0808.count('C'))/len(Rosalind_0808)*100)}
val = 0
for i,j in d_GC.items():
    if val < j:
        val = j
        keys = i
print(keys, val)

#Counting Point Mutations
seq1 = "GAGCCTACTAACGGGAT"
seq2 = "CATCGTAATGACGGCCT"
counts = 0
for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        counts+=1
print(counts)

#Degree Array
dataset = [[6,7],[1,2],[2,3],[6,3],[5,6],[2,5],[2,4],[4,1]]
d_result = {}
for i,j in dataset:
    if i in d_result:
        d_result[i] += 1
    else:
        d_result[i] = 1
    if j in d_result:
        d_result[j] += 1
    else:
        d_result[j] = 1
for i,j in sorted(d_result.items()):
    print(j)

# RNA Splicing
seq1 = 'ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG'
d_codon = {
            'AAA':'K','AAG':'K','AAT':'N','AAC':'N','AGA':'R',
            'AGG':'R','AGT':'S','AGC':'S','ATA':'I','ATG':'M',
            'ATT':'I','ATC':'I','ACA':'T','ACG':'T','ACT':'T',
            'ACC':'T','GAA':'E','GAG':'E','GAT':'D','GAC':'D',
            'GGA':'G','GGG':'G','GGT':'G','GGC':'G','GTA':'V',
            'GTG':'V','GTT':'V','GTC':'V','GCA':'A','GCG':'A',
            'GCT':'A','GCC':'A','TAT':'Y','TAC':'Y','TGG':'W',
            'TGT':'C','TGC':'C','TTA':'L','TTG':'L','TTT':'F',
            'TTC':'F','TCA':'S','TCG':'S','TCT':'S','TCC':'S',
            'CAA':'Q','CAG':'Q','CAT':'H','CAC':'H','CGA':'R',
            'CGG':'R','CGT':'R','CGC':'R','CTA':'L','CTG':'L',
            'CTT':'L','CTC':'L','CCA':'P','CCG':'P','CCT':'P',
            'CCC':'P','TAG':'stop','TAA':'stop','TGA':'stop'
            }
splicing = ''
protein = ''
seq_len = 0
while 1:
    for i in range(seq_len,len(seq1)-2):
        if d_codon[seq1[i:i+3]]=='M':
            break
    for j in range(i,len(seq1),3):
        if d_codon[seq1[j:j+3]]=='stop':
            print(seq1[j:j+3])
            splicing += seq1[i:j]
            break
    seq_len = j+3
    print(seq_len)
    if seq_len == len(seq1):
        break
print(splicing)
"""
# 12 Finding a Protein Motif
import re

p = re.compile("N[^P][S][^P]")
p2 = re.compile("N[^P][T][^P]")

with open("rosalind_mprt.txt", "r") as handle:
    protein_name = handle.readlines()
for n in protein_name:
    name = n.strip()
    with open("{}.fasta".format(name), "r") as f:
        content = f.readlines()
    seq = content[1:]
    for s in range(len(seq)):
        seq[s] = seq[s].strip()
    seq = "".join(seq)

    result1 = p.finditer(seq)
    result2 = p2.finditer(seq)

    l_result = [int(r.start()) + 1 for r in result1]
    for r in result2:
        l_result.append(int(r.start()) + 1)
    l_result = list(set(l_result))
    l_result.sort()

    print(name)
    for i in l_result:
        print(i, end=" ")
    print()
