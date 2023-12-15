#!/usr/bin/env python

from optparse import OptionParser
from sys import stdin, stdout

def main():
	parser = OptionParser(usage='''
		%prog <TAB >FASTA
		
		Transforms a tab-delimited file with two columns into a FASTA file;
		each row in the input is converted into a FASTA block.
	''')
	parser.add_option('-s', '--already_sorted', dest='already_sorted', action='store_true', default=False, help='assume input already sorted on firs column.')
	options, args = parser.parse_args()
	
	if len(args) != 0:
		exit('Unexpected argument number.')
	
	pre_id = None
	for lineidx, line in enumerate(stdin):
		line = line.rstrip('\r\n')
		tokens = line.split('\t')
		id = tokens[0]
		if pre_id is None or id != pre_id:
			if pre_id > id and not options.already_sorted:
				exit("Input not lexicographically sorted on col 1.")
			print(">%s" % tokens[0])
		print("\t".join(tokens[1:]))
		pre_id = id
	
if __name__ == '__main__':
	main()
