codons = {}
codons['AAA'] = 'K'
codons['AAC'] = 'N'
codons['AAG'] = 'K'
codons['AAT'] = 'N'
codons['ACA'] = 'T'
codons['ACC'] = 'T'
codons['ACG'] = 'T'
codons['ACT'] = 'T'
codons['AGA'] = 'R'
codons['AGC'] = 'S'
codons['AGG'] = 'R'
codons['AGT'] = 'S'
codons['ATA'] = 'I'
codons['ATC'] = 'I'
codons['ATG'] = 'M'
codons['ATT'] = 'I'
codons['CAA'] = 'Q'
codons['CAC'] = 'H'
codons['CAG'] = 'Q'
codons['CAT'] = 'H'
codons['CCA'] = 'P'
codons['CCC'] = 'P'
codons['CCG'] = 'P'
codons['CCT'] = 'P'
codons['CGA'] = 'R'
codons['CGC'] = 'R'
codons['CGG'] = 'R'
codons['CGT'] = 'R'
codons['CTA'] = 'L'
codons['CTC'] = 'L'
codons['CTG'] = 'L'
codons['CTT'] = 'L'
codons['GAA'] = 'E'
codons['GAC'] = 'D'
codons['GAG'] = 'E'
codons['GAT'] = 'D'
codons['GCA'] = 'A'
codons['GCC'] = 'A'
codons['GCG'] = 'A'
codons['GCT'] = 'A'
codons['GGA'] = 'G'
codons['GGC'] = 'G'
codons['GGG'] = 'G'
codons['GGT'] = 'G'
codons['GTA'] = 'V'
codons['GTC'] = 'V'
codons['GTG'] = 'V'
codons['GTT'] = 'V'
codons['TAA'] = '*'
codons['TAC'] = 'Y'
codons['TAG'] = '*'
codons['TAT'] = 'Y'
codons['TCA'] = 'S'
codons['TCC'] = 'S'
codons['TCG'] = 'S'
codons['TCT'] = 'S'
codons['TGA'] = '*'
codons['TGC'] = 'C'
codons['TGG'] = 'W'
codons['TGT'] = 'C'
codons['TTA'] = 'L'
codons['TTC'] = 'F'
codons['TTG'] = 'L'
codons['TTT'] = 'F'


def remove_sub(str1, sub1):
	if sub1 in str1:
		start = str1.index(sub1)
		end = start+len(sub1)
	if start == 0:	
		return str1[end:]
	elif end == len(str1):
		return	str1[0:start]
	else:
		return str1[0:start]+str1[end:]

def translate_codon(codon):
    """Convert a codon (three nucleotides) to the corresponding protein."""
    # For convenience, put it into uppercase
    codon = codon.upper()
    # Look it up in the table
    try:
        return codons[codon]
    except KeyError:
        return '*'			

with open('rosalind_splc.txt', 'r') as f:   
	seq_list = []
	seq = ''
	for lin in f:
		if lin[0] != '>':
			seq += lin.strip()
		else:
			if seq != '':
				seq_list.append(seq)
				seq = ''
	if seq != '':
		seq_list.append(seq)
		
	final = seq_list[0]	
	for intron in seq_list[1:]:
		final = remove_sub(final, intron)
		
	aa_seq = ''	
	for r in range(0,len(final)+1,3):
		try:
			aa_seq += translate_codon(final[r]+final[r+1]+final[r+2])
		except IndexError:
			continue	
	print aa_seq.strip('*')		
