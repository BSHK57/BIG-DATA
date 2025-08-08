import sys

curr_bigram = None
curr_count = 0
for line in sys.stdin:
	line = line.strip()
	bigram, count = line.split('\t',1)
	count = int(count)
	if curr_bigram == bigram:
		curr_count += count
	else:
		if curr_bigram:
			print('%s\t%s' % (curr_bigram, curr_count))
		curr_bigram = bigram
		curr_count = count

if curr_bigram:
	print('%s\t%s' % (curr_bigram, curr_count))