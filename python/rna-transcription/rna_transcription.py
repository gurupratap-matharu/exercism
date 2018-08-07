def to_rna(dna_strand):
    transcription = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    rna_strand = ''
    for dna in dna_strand:
        rna_strand += transcription[dna]
    return rna_strand


print(to_rna('ACGTGGTCTTAA'))
