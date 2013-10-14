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

rev_dict = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}

def translate_codon(codon):
    """Convert a codon (three nucleotides) to the corresponding protein."""
    # For convenience, put it into uppercase
    codon = codon.upper()
    # Look it up in the table
    try:
        return codons[codon]
    except KeyError:
        return '*'

def find_start(nucs):
	for_start_list = []
	rev_start_list = []
	for r in range(0,len(nucs)+1,3):
		try:
			if translate_codon(nucs[r]+nucs[r+1]+nucs[r+2]) == 'M':
				for_start_list.append(r)
		except IndexError:
			continue
		try:			
			if translate_codon(nucs[r+1]+nucs[r+2]+nucs[r+3]) == 'M':
				for_start_list.append(r+1)
		except IndexError:
			continue
		try:					
			if translate_codon(nucs[r+2]+nucs[r+3]+nucs[r+4]) == 'M':
				for_start_list.append(r+2)
		except IndexError:
			continue
	nums = range(0, len(nucs)+1, 3)
	for rn in nums[::-1]:	
		try:					
			if translate_codon(rev_dict[nucs[rn]]+rev_dict[nucs[rn-1]]+rev_dict[nucs[rn-2]]) == 'M':
				rev_start_list.append(rn)
		except IndexError:
			continue
		try:					
			if translate_codon(rev_dict[nucs[rn-1]]+rev_dict[nucs[rn-2]]+rev_dict[nucs[rn-3]]) == 'M':
				rev_start_list.append(rn-1)
		except IndexError:
			continue
		try:					
			if translate_codon(rev_dict[nucs[rn-2]]+rev_dict[nucs[rn-3]]+rev_dict[nucs[rn-4]]) == 'M':
				rev_start_list.append(rn-2)
		except IndexError:
			continue		
	return for_start_list, rev_start_list
	
def find_stop(nucs):
	for_stop_list = []
	rev_stop_list = []
	for r in range(0,len(nucs)+1,3):
		try:
			if translate_codon(nucs[r]+nucs[r+1]+nucs[r+2]) == '*':
				for_stop_list.append(r)
		except IndexError:
			continue
		try:			
			if translate_codon(nucs[r+1]+nucs[r+2]+nucs[r+3]) == '*':
				for_stop_list.append(r+1)
		except IndexError:
			continue
		try:					
			if translate_codon(nucs[r+2]+nucs[r+3]+nucs[r+4]) == '*':
				for_stop_list.append(r+2)
		except IndexError:
			continue
	nums = range(0, len(nucs)+1, 3)
	for rn in nums[::-1]:	
		try:					
			if translate_codon(rev_dict[nucs[rn]]+rev_dict[nucs[rn-1]]+rev_dict[nucs[rn-2]]) == '*':
				rev_stop_list.append(rn)
		except IndexError:
			continue
		try:					
			if translate_codon(rev_dict[nucs[rn-1]]+rev_dict[nucs[rn-2]]+rev_dict[nucs[rn-3]]) == '*':
				rev_stop_list.append(rn-1)
		except IndexError:
			continue
		try:					
			if translate_codon(rev_dict[nucs[rn-2]]+rev_dict[nucs[rn-3]]+rev_dict[nucs[rn-4]]) == '*':
				rev_stop_list.append(rn-2)
		except IndexError:
			continue		
	return for_stop_list, rev_stop_list	
	
def find_orf(start_lists, stop_lists):
	orf_list_for = []
	orf_list_rev = []
	last_start = []
	for pos_start_f in start_lists[0]:
		for pos_stop_f in stop_lists[0]:
			if pos_start_f%3 == pos_stop_f%3 and pos_stop_f > pos_start_f and pos_start_f not in last_start:
				last_start.append(pos_start_f)
				orf_list_for.append([pos_start_f, pos_stop_f])
	last_start = []			
	for pos_start_r in start_lists[1]:
		for pos_stop_r in stop_lists[1]:
			if pos_start_r%3 == pos_stop_r%3 and pos_stop_r < pos_start_r and pos_start_r not in last_start:
				last_start.append(pos_start_r)
				orf_list_rev.append([pos_start_r, pos_stop_r])
							
	return orf_list_for, orf_list_rev							
		        
nuc_list = []      
with open("rosalind_orf.txt", "r") as f:
	for a in f:
		if a[0] != '>':
			for nuc in a.strip():  
				nuc_list.append(nuc)

	print find_orf(find_start(nuc_list), find_stop(nuc_list))
	ans = find_orf(find_start(nuc_list), find_stop(nuc_list))
	pairs_f = ans[0]
	pairs_r = ans[1]
	
	aa_seq_list =[]
	for p in pairs_f:
		aa_seq = ''
		for n in range(p[0], p[1]+1, 3):
			aa_seq += translate_codon(nuc_list[n]+nuc_list[n+1]+nuc_list[n+2])
		if aa_seq.strip('*') not in aa_seq_list:
			aa_seq_list.append(aa_seq.strip('*'))
	
	for pr in pairs_r:
		aa_seq = ''
		ran = range(pr[1],pr[0]+1,3)
		for nr in ran[::-1]:
			aa_seq += translate_codon(rev_dict[nuc_list[nr]]+rev_dict[nuc_list[nr-1]]+rev_dict[nuc_list[nr-2]])			
		if aa_seq.strip('*') not in aa_seq_list:
			aa_seq_list.append(aa_seq.strip('*'))
		
				
			
	for x in aa_seq_list:
		print x		     
        
