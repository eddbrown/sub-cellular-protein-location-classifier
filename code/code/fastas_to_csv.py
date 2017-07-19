exec(open('require.py').read())

types = ['cyto', 'mito', 'nucleus', 'secreted']

def label(t):
    return {'label': TYPE_TO_LABELS[t]}

with open('./csvs/data.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=FEATURES)
    writer.writeheader()
    for t in types:
        fasta_sequences = SeqIO.parse(open('./fastas/' + t + '.fasta'),'fasta')
        for fasta in fasta_sequences:
            sequence = fasta.seq
            writer.writerow(merge_dicts(generate_features(sequence),label(t)))
