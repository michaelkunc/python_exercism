from string import maketrans

DNA = 'GCTA'
RNA = 'CGAU'

def to_rna(strand):
    return strand.translate(maketrans(DNA, RNA))
