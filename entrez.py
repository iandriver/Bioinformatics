from Bio import Entrez
Entrez.email = "ihd2102@columbia.edu" 
handle = Entrez.esearch(db="nucleotide", retmax=15, term="decapentaplegic AND Drosophila melanogaster[porgn:__txid7227]")
list = []

for line in handle:
  if line.strip()[0:4] == '<Id>':
		len_id = 4
		for char in line.strip()[4:15]:
			if char == '<':
				list.append(line.strip()[4:len_id])
			elif char != '<':	
				len_id +=1
print list[0]			

for id_num in list:
	rec = Entrez.efetch(db="nucleotide", id=id_num, rettype = "gb", retmode="text")
	print rec.readline()
