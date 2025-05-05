from Bio import SeqIO

fasta_file = "./cdhit_result/all40.fasta"  
count = 0

for record in SeqIO.parse(fasta_file, "fasta"):
    count += 1

print(f"序列數量: {count}")
