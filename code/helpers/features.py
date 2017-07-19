FEATURES = ['label','sequence_length', 'molecular_weight', 'isoelectric_point', 'aromaticity']

for letter in ascii_uppercase:
    FEATURES = np.append(FEATURES, 'global_' + letter)

for letter in ascii_uppercase:
    FEATURES = np.append(FEATURES, 'local_first_50_' + letter)

for letter in ascii_uppercase:
    FEATURES = np.append(FEATURES, 'local_last_50_' + letter)
