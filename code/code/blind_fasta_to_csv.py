exec(open('require.py').read())

with open('./csvs/blind_data.csv', 'w') as csvfile:
    labelless_features = np.delete(FEATURES,0)
    writer = csv.DictWriter(csvfile, fieldnames=labelless_features)
    writer.writeheader()
    fasta_sequences = SeqIO.parse(open('./fastas/blind.fasta'),'fasta')
    for fasta in fasta_sequences:
        sequence, seq_id = fasta.seq, fasta.id
        writer.writerow(generate_features(sequence))
