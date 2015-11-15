def to_rna(strand):
    translation = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna_strand = []
    for nucleotide in strand:
        rna_strand.append(translation[nucleotide])
    return ''.join(rna_strand)
