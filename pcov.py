import cProfile

def process(reads, superstr):
	used_reads = []
	for read in reads:
		unused_reads = [read for read in reads if read not in used_reads]
		if len(read) == len(superstr):
			superstr, phr_to_cons = align(superstr, unused_reads)
			used_reads.append(phr_to_cons)
		elif len(read) != len(superstr):
			if read in superstr:
				used_reads.append(read)
			else:
				superstr, phr_to_cons = align(superstr, unused_reads)
				used_reads.append(phr_to_cons)
	return superstr

def align(superstring, reads):
	alignments = dict()
	ls = len(superstring)
	for read in reads:
		for i in range(len(read), 0, -1):
			if read[:i] == superstring[ls-i:]:
				alignments[read] = superstring+read[i:]
			elif read[i:] == superstring[:ls-i]:
				alignments[read] = read[:i] + superstring
		alignments = {v: k for k, v in alignments.items()}
	return alignments[min(alignments.keys(), key=len)], min(alignments.keys(), key=len)

def encycle(string):
	outcomes = []
	for i in range(len(string)):
		if string[:i] == rev(string[-i:]):
			outcomes.append(string[:-i])
	try:
		return min(outcomes, key=len)
	except ValueError:
		print("nocycle")
		return string
		
def rev(s):
    return s[::-1]

def main():
	with open("/home/haelmorn/Downloads/rosalind_pcov.txt", 'r') as data:
		reads = data.read().splitlines()
	superstr = reads[0]
	reads.remove(superstr)
	non_cyclic = process(reads, superstr)
	print(encycle(non_cyclic))

if __name__ == "__main__":
	main()