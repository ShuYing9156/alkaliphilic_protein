from Bio import Entrez

Entrez.email = 'ruby2015095231128@gmail.com'

handle = Entrez.efetch( db = 'protein', term = 'alkaliphilic', rettype='gb', retmode='text' )
record = Entrez.read(handle)

print(record)
#print(record.keys())
#print(record['Count'])
#print(record['DbInfo'].keys())
#print(record['DbInfo']['MenuName'])