rna_codon_dict ={}
with open("RNA_codon.txt", "r") as var:
  for codon in var:
		if codon[5] == " ":
			aa_or_stop = codon[4]
		else:
			aa_or_stop = codon[4:8]
		rna_codon_dict[codon[0:3]]= aa_or_stop.rstrip()\
print rna_codon_dict		
