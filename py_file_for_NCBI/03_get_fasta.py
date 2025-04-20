## 取得fasta檔
from Bio import Entrez
from Bio import SeqIO


## 設置電子郵件
Entrez.email = "ruby2015095231128@gmail.com"


# 讀檔並將id合成list
idlist = []

with open('idlist.txt', mode='r', encoding='utf-8') as idlist_file:
    for line in idlist_file:
        idlist.append(line.strip())

print(len(idlist))
print(type(idlist))


# 查詢每個id的fasta
retmax = 100


with open("seqs.fasta", "a+") as fasta_file:
    for start in range(0, len(idlist), retmax):
        # 分批取出 id
        batch_ids = idlist[start:start + retmax]
        ids = ",".join(batch_ids)  # 將 id 合併成逗號分隔的字串
        handle = Entrez.efetch(db="protein", id=ids, rettype="fasta", retmode="text")
        fasta_data = handle.read()  # 讀取 fasta 資料
        handle.close()
        # 寫入檔案
        fasta_file.write(fasta_data)
        print(f"Records {start + 1} to {start + len(batch_ids)} downloaded.")

