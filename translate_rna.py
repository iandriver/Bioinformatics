import string

codons = {}
codons['AAA'] = 'K'
codons['AAC'] = 'N'
codons['AAG'] = 'K'
codons['AAU'] = 'N'
codons['ACA'] = 'T'
codons['ACC'] = 'T'
codons['ACG'] = 'T'
codons['ACU'] = 'T'
codons['AGA'] = 'R'
codons['AGC'] = 'S'
codons['AGG'] = 'R'
codons['AGU'] = 'S'
codons['AUA'] = 'I'
codons['AUC'] = 'I'
codons['AUG'] = 'M'
codons['AUU'] = 'I'
codons['CAA'] = 'Q'
codons['CAC'] = 'H'
codons['CAG'] = 'Q'
codons['CAU'] = 'H'
codons['CCA'] = 'P'
codons['CCC'] = 'P'
codons['CCG'] = 'P'
codons['CCU'] = 'P'
codons['CGA'] = 'R'
codons['CGC'] = 'R'
codons['CGG'] = 'R'
codons['CGU'] = 'R'
codons['CUA'] = 'L'
codons['CUC'] = 'L'
codons['CUG'] = 'L'
codons['CUU'] = 'L'
codons['GAA'] = 'E'
codons['GAC'] = 'D'
codons['GAG'] = 'E'
codons['GAU'] = 'D'
codons['GCA'] = 'A'
codons['GCC'] = 'A'
codons['GCG'] = 'A'
codons['GCU'] = 'A'
codons['GGA'] = 'G'
codons['GGC'] = 'G'
codons['GGG'] = 'G'
codons['GGU'] = 'G'
codons['GUA'] = 'V'
codons['GUC'] = 'V'
codons['GUG'] = 'V'
codons['GUU'] = 'V'
codons['UAA'] = '*'
codons['UAC'] = 'Y'
codons['UAG'] = '*'
codons['UAU'] = 'Y'
codons['UCA'] = 'S'
codons['UCC'] = 'S'
codons['UCG'] = 'S'
codons['UCU'] = 'S'
codons['UGA'] = '*'
codons['UGC'] = 'C'
codons['UGG'] = 'W'
codons['UGU'] = 'C'
codons['UUA'] = 'L'
codons['UUC'] = 'F'
codons['UUG'] = 'L'
codons['UUU'] = 'F'

def translate_codon(codon):
    """Convert a codon (three nucleotides) to the corresponding protein."""
    # For convenience, put it into uppercase
    codon = codon.upper()
    # Look it up in the table
    try:
        return codons[codon]
    except KeyError:
        return '*'

def translate_rna(rna):
  
    length = len(rna)
    pos = 0
    protein = []
    while (pos < (length-2)):
        aa = translate_codon(rna[pos:pos+3])
        protein.append(aa)
        pos = pos + 3
    return string.join(protein, '')
    
    
with open('rosalind_prot.txt', 'r') as f:   
	for lin in f:
		print translate_rna(lin) 
