def generate_features(sequence):
    sequence = sequence.upper()

    return merge_dicts(sequence_length_as_dict(sequence),
        molecular_weight_as_dict(sequence),
        aromaticity_as_dict(sequence),
        isoelectric_point_as_dict(sequence),
        global_amino_percentages(sequence),
        local_first_50(sequence),
        local_last_50(sequence)
    )

def seperate(sequence):
    return list(sequence)

def global_amino_percentages(sequence):
    total_aminos = sequence_length(sequence)
    separated_sequence = seperate(sequence)

    global_amino_percentages = {}
    for letter in ascii_uppercase:
        amino_percentage = separated_sequence.count(letter)/total_aminos
        dict_entry = {'global_' + letter:amino_percentage}
        global_amino_percentages = merge_dicts(global_amino_percentages, dict_entry)

    return global_amino_percentages

def local_first_50(sequence):
    total_aminos = 50
    sequence = sequence[0:51]
    separated_sequence = seperate(sequence)

    local_amino_percentages = {}
    for letter in ascii_uppercase:
        amino_percentage = separated_sequence.count(letter)/total_aminos
        dict_entry = {'local_first_50_' + letter:amino_percentage}
        local_amino_percentages = merge_dicts(local_amino_percentages, dict_entry)

    return local_amino_percentages

def local_last_50(sequence):
    total_aminos = 50
    sequence = sequence[-51:]
    separated_sequence = seperate(sequence)

    local_amino_percentages = {}
    for letter in ascii_uppercase:
        amino_percentage = separated_sequence.count(letter)/total_aminos
        dict_entry = {'local_last_50_' + letter:amino_percentage}
        local_amino_percentages = merge_dicts(local_amino_percentages, dict_entry)

    return local_amino_percentages

def sequence_length(sequence):
    return len(sequence)

def sequence_length_as_dict(sequence):
    return {'sequence_length':sequence_length(sequence)}

def aromaticity_as_dict(sequence):
    sequence_str = sequence.tostring()
    return {'aromaticity':ProteinAnalysis(sequence_str).aromaticity()}

def isoelectric_point_as_dict(sequence):
    sequence_str = sequence.tostring()
    return {'isoelectric_point':ProteinAnalysis(sequence_str).isoelectric_point()}

def molecular_weight_as_dict(sequence):
    sequence_str = sequence.tostring()
    sequence_str = sequence_str.replace("X", "")
    sequence_str = sequence_str.replace("B", "")
    return {'molecular_weight':ProteinAnalysis(sequence_str).molecular_weight()}
