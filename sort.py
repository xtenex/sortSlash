#!/usr/bin/python
#-*- coding: utf-8 -*-

#This script is for sorting strings like: Zip/Calibri/Venom/Alpha
#without losing the format and getting a better view due to sort

import sys

def main():
	fr = open(sys.argv[1], "r")
	#fw = open(sys.argv[2], "a+")

	for line in fr:
		tmp = line.rstrip().split("/")
		tmp.sort()
		#print tmp
		print str("/".join(tmp))
		#fw.write(tmp)

	fr.close()
	#fw.close()

if __name__ == '__main__':
	main()
