import pandas as pd

all_seqs = pd.read_csv('./pdb_fasta/rcsb_pdb_sequence_20250422064207.csv')
#print(pdb_seqs['Entry ID'], pdb_seqs['Sequence'])

seqs_needed = all_seqs[['Entry ID', 'Sequence']]
with open('./pdb_fasta/pdb_csv2fasta.fasta', 'w') as fasta_file:
    for _, row in seqs_needed.iterrows():
        entry_id = row['Entry ID']
        sequence = row['Sequence']
        if pd.notna(entry_id) and pd.notna(sequence):
            fasta_file.write(f">{entry_id}\n{sequence}\n")