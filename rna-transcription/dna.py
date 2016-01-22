DNA = 'GCTA'
RNA = 'CGAU'

translation = dict(zip(DNA,RNA))

def to_rna(strand):
    return ''.join(translation[i] for i in strand)
