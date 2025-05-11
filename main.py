from func import *

#從NCBI的蛋白質數據庫中查詢符合條件的蛋白質ID，並將其寫入檔案。
'''
email = 'ruby2015095231128@gmail.com'
term = 'alkaliphilic'
idlist = './NCBI_fasta/idlist.txt'

fetch_ncbi_ids(email = email, 
               term = term, 
               filename = idlist)
'''


#從NCBI查詢FASTA序列並將結果寫入檔案。
'''
ncbi_seqs_fasta = './NCBI_fasta/seqs.fasta'

fetch_ncbi_seqs(email = email, 
                id_file = idlist, 
                output_file = ncbi_seqs_fasta)
'''


#將CSV檔案中的PDB序列轉換為FASTA格式並寫入檔案。
'''
pdb_seqs_fasta = './pdb_fasta/pdb_all_seqs.fasta'
pdb_seqs_csv = './pdb_fasta/rcsb_pdb_sequence_20250422064207.csv'

pdb_csv2fasta(csv_file = pdb_seqs_csv, 
              fasta_file = pdb_seqs_fasta)
'''


#根據長度和模糊殘基條件過濾FASTA檔案中的序列。

ncbi_seqs_fasta = './NCBI_fasta/seqs.fasta'
uniprot_seqs = './uniprot_fasta/uniprotkb_seqs.fasta'
pdb_seqs_fasta = './pdb_fasta/pdb_all_seqs.fasta'

filtered_ncbi = './NCBI_fasta/filtered_seqs.fasta'
filtered_uniprot = './uniprot_fasta/filtered_uniprot_seqs.fasta'
filtered_pdb = './pdb_fasta/filtered_pdb_seqs.fasta'
'''
residues = ['B', 'J', 'o', 'U', 'X', 'Z']

filter_seqs(input_file = ncbi_seqs_fasta,
            output_file = filtered_ncbi,
            min_length = 100,
            ambiguous_residues = residues)

filter_seqs(input_file = uniprot_seqs,
            output_file = filtered_uniprot,
            min_length = 100,
            ambiguous_residues = residues)

filter_seqs(input_file = pdb_seqs_fasta,
            output_file = filtered_pdb,
            min_length = 100,
            ambiguous_residues = residues)
'''


#將多個FASTA檔案合併成一個檔案

files = [filtered_ncbi, filtered_uniprot, filtered_pdb]
all_seqs = './all_fasta/all.fasta'
'''
merge_fasta_files(fasta_files = files,
                  output_file = all_seqs)
'''


#計算FASTA檔案中的序列數量
'''
count = count_seqs(all_seqs)
print(count)
'''


#用CD-HIT將相似的序列聚類
exe = './cd-hit-v4.8.1-2019-0228/cd-hit'

'''
input_file = [filtered_ncbi, filtered_uniprot, filtered_pdb]
output_file = []
identity = [40, 50, 60, 70, 80, 90, 95]
dataset = ['ncbi', 'uniprot', 'pdb']

for i in dataset:
    for j in identity:
        output_file.append(f'./cdhit_result/{i}{j}.fasta')

word_size = [2, 3, 4, 5, 5, 5, 5]
sc = True
sf = True

output_index = 0

for file in input_file:
    count_identity = 0
    count_word_size = 0
    
    for k in range(7):
        run_cdhit(executable = exe,
                  input_file = file,
                  output_file = output_file[output_index + k],
                  identity = identity[count_identity - 1],
                  word_size = word_size[count_word_size - 1],
                  search_clustering = sc,
                  sequence_filter = sf)
        
        count_identity += 1
        count_word_size += 1
    
    output_index += 7
'''

'''
output = './all_fasta/all40.fasta'
identity = 0.4
word_size = 2

run_cdhit(executable = exe,
          input_file = all_seqs,
          output_file = output,
          identity = identity,
          word_size = word_size,
          search_clustering = True,
          sequence_filter = True)

print(count_seqs(output))
'''


#根據給定的FASTA檔案，將 all_fasta_file 寫入不同的FASTA檔案
all_fasta_file = './all_fasta/all40.fasta'
original_files = [filtered_ncbi, filtered_uniprot, filtered_pdb]

ncbi_branch = './all_fasta/all40_ncbi.fasta'
uniprot_branch = './all_fasta/all40_uniprot.fasta'
pdb_branch = './all_fasta/all40_pdb.fasta'

output_files = [ncbi_branch, uniprot_branch, pdb_branch]

all2three(all_fasta_file = all_fasta_file,
          original_files = original_files,
          output_files = output_files)