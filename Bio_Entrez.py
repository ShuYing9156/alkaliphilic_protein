from Bio import Entrez
from Bio import SeqIO

#Just try
Entrez.email = 'ruby2015095231128@gmail.com'

handle = Entrez.esearch( db = 'protein', term = 'alkaliphilic' )
record = Entrez.read(handle)

idlist = list(record['IdList'])

#print(record)
#print(record.keys())
#print(record['IdList'])
#print(type(idlist))
print(idlist)
#print(record['DbInfo'].keys())
#print(record['DbInfo']['MenuName'])

handle.close()

id_str = ",".join(idlist)

handle2 = Entrez.efetch( db = 'protein', id = id_str, rettype="fasta", retmode="text" )
#record2 = Entrez.read(handle2)

record2 = list(SeqIO.parse(handle2, "fasta"))
handle2.close()

for records in record2:
    print(f"ID: {records.id}")
    print(f"描述: {records.description}")
    print(f"序列: {records.seq}")
    print(f"序列長度: {len(records.seq)}\n")


