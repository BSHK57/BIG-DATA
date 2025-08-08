import sys

for line in sys.stdin:
	line = line.strip()
	words = line.split()

	for i in range(len(words)-1):
		bigram = "%s,%s" % (words[i], words[i+1])
		print("%s\t%s" % (bigram,1))