from Bio import SeqIO

# 定義模糊殘基
residues = ['B','J','o','U','X','Z']

# 讀取原始 NCBI_fasta 檔案，並將過濾後的序列寫入新的檔案
with open('./NCBI_fasta/seqs.fasta', 'r') as input_fasta,\
    open('./NCBI_fasta/filtered_seqs.fasta', 'w') as output_fasta:
    
    sequence_count = 0

    for record in SeqIO.parse(input_fasta, 'fasta'):
        sequence = str(record.seq)
        
        # 檢查序列長度和模糊殘基
        if len(sequence) > 100 and not any(res in residues for res in sequence):
            SeqIO.write(record, output_fasta, 'fasta')
            sequence_count += 1

print("過濾完成，結果已寫入 filtered_seqs.fasta")
print(f"ffiltered_seqs.fasta 有 {sequence_count} 筆序列資料。")





#uniprot_fasta
with open('./uniprot_fasta/uniprotkb_seqs.fasta', 'r') as input_fasta,\
    open('./uniprot_fasta/filtered_uniprot_seqs.fasta', 'w') as output_fasta:
    
    sequence_count = 0

    for record in SeqIO.parse(input_fasta, 'fasta'):
        sequence = str(record.seq)
        
        # 檢查序列長度和模糊殘基
        if len(sequence) > 100 and not any(res in residues for res in sequence):
            SeqIO.write(record, output_fasta, 'fasta')
            sequence_count += 1

print("過濾完成，結果已寫入 filtered_uniprot_seqs.fasta")
print(f"filtered_uniprot_seqs.fasta 有 {sequence_count} 筆序列資料。")





#pdb_fasta
with open('./pdb_fasta/pdb_all_seqs.fasta', 'r') as input_fasta,\
    open('./pdb_fasta/filtered_pdb_seqs.fasta', 'w') as output_fasta:
    
    sequence_count = 0

    for record in SeqIO.parse(input_fasta, 'fasta'):
        sequence = str(record.seq)
        
        # 檢查序列長度和模糊殘基
        if len(sequence) > 100 and not any(res in residues for res in sequence):
            SeqIO.write(record, output_fasta, 'fasta')
            sequence_count += 1

print("過濾完成，結果已寫入 filtered_pdb_seqs.fasta")
print(f"filtered_pdb_seqs.fasta 有 {sequence_count} 筆序列資料")