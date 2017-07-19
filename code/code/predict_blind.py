exec(open('require.py').read())

# Load data and model
classifier = joblib.load('./pickles/model.pkl')
blind_data = np.loadtxt('csvs/blind_data.csv', delimiter=',', skiprows=1)

fasta_sequences = SeqIO.parse(open('./fastas/blind.fasta'),'fasta')
sequence_names = []
for fasta in fasta_sequences:
    seq_id = fasta.id
    sequence_names = sequence_names + [seq_id]

sequence_names = np.array(sequence_names)

# Predict on blind test
blind_probabilities = np.max(classifier.predict_proba(blind_data),1)
blind_predictions = classifier.predict(blind_data)

for i in range(len(sequence_names)):
    name = sequence_names[i]
    typ = LABELS_TO_TYPE[blind_predictions[i]][:4]
    probability = blind_probabilities[i]

    print(name + ' ' + typ.title() + ' Confidence {0:.1f}'.format(100 * probability) + '%')
