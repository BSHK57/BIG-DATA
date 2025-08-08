
import sys

for line in sys.stdin:
	line = line.strip()
	parts = line.split(',')

	if len(parts) >= 2:
		year = parts[0].strip()
		year = year.split("-")[0]
		temperature = parts[1].strip()
		try:
			float(temperature)
			print("%s\t%s" % (year,temperature))
		except ValueError:
			continue