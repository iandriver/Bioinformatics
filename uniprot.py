from Bio import ExPASy
from Bio import SwissProt

with open('rosalind_dbpr.txt', 'r') as f:   
	seq_list = []
	seq = ''
	for lin in f:
		prot_id = lin.strip()
		handle = ExPASy.get_sprot_raw(prot_id)
		record = SwissProt.read(handle)
		for r in record.cross_references:
			if r[0] == 'GO' and r[2][0] == 'P':
				print r[2][2:]