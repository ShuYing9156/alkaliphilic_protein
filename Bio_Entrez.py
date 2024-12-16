from Bio import Entrez

Entrez.email = 'ruby2015095231128@gmail.com'

handle = Entrez.einfo()
record = Entrez.read(handle)

print(record)
print(type(record))