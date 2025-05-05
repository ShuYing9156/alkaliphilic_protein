'''
from Bio import SeqIO


# 設定FASTA檔案
all_fasta_file = "all.fasta"
fasta_01_file = "fasta_01.fasta"
fasta_02_file = "fasta_02.fasta"
fasta_03_file = "fasta_03.fasta"


# 讀取fasta_01、fasta_02、fasta_03中的序列並儲存到集合中
ncbi_sequences = {str(record.seq) for record in SeqIO.parse('./NCBI_fasta/filtered_seqs.fasta', "fasta")}
uniprot_sequences = {str(record.seq) for record in SeqIO.parse('./uniprot_fasta/filtered_uniprot_seqs.fasta', "fasta")}
pdb_sequences = {str(record.seq) for record in SeqIO.parse('./pdb_fasta/filtered_pdb_seqs.fasta', "fasta")}

# 創建檔案來寫入結果
with open("ncbi_branch.fasta", "w") as ncbi_branch, \
     open("uniprot_branch.fasta", "w") as uniprot_branch, \
     open("pdb_branch.fasta", "w") as pdb_branch:

    # 讀取all_fasta檔案並檢查每條序列
    for record in SeqIO.parse('all.fasta', "fasta"):
        sequence_str = str(record.seq)
        if sequence_str in ncbi_sequences:
            ncbi_branch.write(f">{record.id}\n{sequence_str}\n")
        if sequence_str in uniprot_sequences:
            uniprot_branch.write(f">{record.id}\n{sequence_str}\n")
        if sequence_str in pdb_sequences:
            pdb_branch.write(f">{record.id}\n{sequence_str}\n")

        print(f"已完成比對序列: {record.id}")

print("序列檢查完成，已將結果寫入相應的檔案中。")
'''



from Bio import SeqIO

'''
# 設定FASTA檔案
all_fasta_file = "all.fasta"
fasta_01_file = "fasta_01.fasta"
fasta_02_file = "fasta_02.fasta"
fasta_03_file = "fasta_03.fasta"
'''

# 讀取fasta_01、fasta_02、fasta_03中的序列並儲存到集合中
ncbi_sequences = {str(record.seq): record.id for record in SeqIO.parse('./NCBI_fasta/filtered_seqs.fasta', "fasta")}
uniprot_sequences = {str(record.seq): record.id for record in SeqIO.parse('./uniprot_fasta/filtered_uniprot_seqs.fasta', "fasta")}
pdb_sequences = {str(record.seq): record.id for record in SeqIO.parse('./pdb_fasta/filtered_pdb_seqs.fasta', "fasta")}

# 用於追蹤已寫入的序列
written_sequences = set()

# 創建檔案來寫入結果
with open("ncbi_branch.fasta", "w") as ncbi_branch, \
     open("uniprot_branch.fasta", "w") as uniprot_branch, \
     open("pdb_branch.fasta", "w") as pdb_branch:

    # 讀取all_fasta檔案並檢查每條序列
    for record in SeqIO.parse('all.fasta', "fasta"):
        sequence_str = str(record.seq)
        
        # 檢查序列來源並寫入檔案
        if sequence_str in ncbi_sequences and sequence_str not in written_sequences:
            ncbi_branch.write(f">{record.id}\n{sequence_str}\n")
            written_sequences.add(sequence_str)  # 標記為已寫入
            print(f"已完成比對序列: {record.id} (來源: fasta_01)")
            print(f"選擇的序列 ID: {record.id} (資料集: fasta_01)")  # 印出選擇的序列 ID 和資料集
            continue  # 跳過後續檢查
        
        if sequence_str in uniprot_sequences and sequence_str not in written_sequences:
            uniprot_branch.write(f">{record.id}\n{sequence_str}\n")
            written_sequences.add(sequence_str)  # 標記為已寫入
            print(f"已完成比對序列: {record.id} (來源: fasta_02)")
            print(f"選擇的序列 ID: {record.id} (資料集: fasta_02)")  # 印出選擇的序列 ID 和資料集
            continue  # 跳過後續檢查
        
        if sequence_str in pdb_sequences and sequence_str not in written_sequences:
            pdb_branch.write(f">{record.id}\n{sequence_str}\n")
            written_sequences.add(sequence_str)  # 標記為已寫入
            print(f"已完成比對序列: {record.id} (來源: fasta_03)")
            print(f"選擇的序列 ID: {record.id} (資料集: fasta_03)")  # 印出選擇的序列 ID 和資料集

print("序列檢查完成，已將結果寫入相應的檔案中。")
