#!/usr/bin/python
import sys
import itertools;

if len(sys.argv) < 4:
	print "Usage <file1> <file2> <maxPercentageError>"
	exit(2)

file1 = open(sys.argv[1],"r");
file2 = open(sys.argv[2],"r");
relErrorLimit = float(sys.argv[3])

for (line1,line2) in itertools.izip_longest(file1, file2):
	# If both are finite floats check distance
	# Otherwise check equality
	isNumber1 = True;
	isNumber2 = True;
	number1 = 0;
	number2 = 0;
	line1 = line1.rstrip('\n');
	line2 = line2.rstrip('\n');
	try:
		number1 = float(line1);
		number2 = float(line2);
		if number1 != 0 or number2 != 0:
			error = abs(number1-number2);
			relError = error/max(abs(number1),abs(number2)) * 100;
			# Only print out error of more than relErrorLimit%
			if relError > relErrorLimit:
				print "%g / %g => %g%%" % (number1,number2,relError)
	except:
		if line1 != line2:
			sys.stderr.write("Error %s vs %s\n" % (line1,line2));
			exit(1)
		print line1
