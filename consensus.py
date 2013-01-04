  def cons(strings):
		from collections import Counter
		counters = map(Counter, zip(*strings))
		print counters
		consensus = "".join(c.most_common(1)[0][0] for c in counters)
		profile_matrix = "\n".join(b + ": " + \
			" ".join(str(c[b]) for c in counters) for b in "ACGT")
		return consensus + "\n" + profile_matrix
