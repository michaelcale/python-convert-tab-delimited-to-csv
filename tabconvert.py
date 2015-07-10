# USE python tabconvert.py < /tmp/input.txt > /tmp/output.csv
import csv, sys

delimfile = csv.reader(sys.stdin, dialect=csv.excel_tab)
outputfile = csv.writer(sys.stdout, delimiter=',', lineterminator='\n')
for row in delimfile:
    outputfile.writerow(row)
