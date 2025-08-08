import sys

current_year = None
current_year_temps = []
min_avg_temp = float('inf')
coolest_year = None

for line in sys.stdin:
	line = line.strip()
	year, temperature_str = line.split('\t')
	temperature = float(temperature_str)
	

	if current_year == year:
		current_year_temps.append(temperature)
	else:
		if current_year is not None:
			avg_temp = sum(current_year_temps) / len(current_year_temps)
			if avg_temp < min_avg_temp:
				min_avg_temp = avg_temp
				coolest_year = current_year
		current_year = year
		current_year_temps = [temperature]
if current_year is not None:
	avg_temp = sum(current_year_temps) / len(current_year_temps)
	if avg_temp < min_avg_temp:
		min_avg_temp = avg_temp
		coolest_year = current_year

if coolest_year is not None:
	print("The coolest year is: %s with an average temperature of: %s" % (coolest_year,min_avg_temp))