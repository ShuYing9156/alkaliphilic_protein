from Bio import Entrez

# 設置電子郵件
Entrez.email = "ruby2015095231128@gmail.com"

# 設置查詢參數
db = "protein"
term = "alkaliphilic"
retmax = 100  # 每次查詢返回 100 條記錄

# 獲取總記錄數
handle = Entrez.esearch(db=db, term=term)
record = Entrez.read(handle)
total_records = int(record["Count"])
handle.close()
#print(total_records)
#print(record)


# 分頁查詢
for start in range(0, total_records, retmax):
    handle = Entrez.esearch(db=db, term=term, retmax=retmax, retstart=start)
    record = Entrez.read(handle)
    handle.close()

    #將id寫入檔案
    with open('idlist.txt', mode='a+', encoding='utf-8') as idlist_file:
        for id in record['IdList']:
            idlist_file.write(f'{id}\n')
    
    # 印出出當前頁的 ID
    print(f"Records {start + 1} to {start + len(record['IdList'])}")
    ''': {record['IdList']}'''