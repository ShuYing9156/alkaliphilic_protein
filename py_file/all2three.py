from Bio import SeqIO

# 讀取 all40.fasta 中的所有序列 ID
all40_ids = set()
for record in SeqIO.parse("./cdhit_result/all40.fasta", "fasta"):
    all40_ids.add(record.id)

# 讀取 filtered_seqs.fasta 中的序列 ID
filtered_ids = set()
for record in SeqIO.parse("./NCBI_fasta/filtered_seqs.fasta", "fasta"):
    filtered_ids.add(record.id)

# 讀取 filtered_uniprot_seqs.fasta 中的序列 ID
filtered_uniprot_ids = set()
for record in SeqIO.parse("./uniprot_fasta/filtered_uniprot_seqs.fasta", "fasta"):
    filtered_uniprot_ids.add(record.id)

# 讀取 filtered_pdb_seqs.fasta 中的序列 ID
filtered_pdb_ids = set()
for record in SeqIO.parse("./pdb_fasta/filtered_pdb_seqs.fasta", "fasta"):
    filtered_pdb_ids.add(record.id)

# 準備寫入不同的 FASTA 檔案
ncbi_records = []
uniprot_records = []
pdb_records = []

for record in SeqIO.parse("./cdhit_result/all40.fasta", "fasta"):
    seq_id = record.id
    if seq_id in filtered_ids:
        ncbi_records.append(record)
    elif seq_id in filtered_uniprot_ids:
        uniprot_records.append(record)
    elif seq_id in filtered_pdb_ids:
        pdb_records.append(record)

# 寫入到不同的 FASTA 檔案
SeqIO.write(ncbi_records, "ncbi_branch.fasta", "fasta")
SeqIO.write(uniprot_records, "uniprot_branch.fasta", "fasta")
SeqIO.write(pdb_records, "pdb_branch.fasta", "fasta")

print("序列已成功寫入各自的 FASTA 檔案。")
