TYPE_TO_LABELS = OrderedDict({
    'cyto':1,
    'mito':2,
    'nuclear':3,
    'secreted':4
})

LABELS_TO_TYPE = {v: k for k, v in TYPE_TO_LABELS.items()}

LABELS = ['cyto', 'mito', 'nuclear', 'secreted']
