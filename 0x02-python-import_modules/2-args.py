#!/usr/bin/python3

if __name__ == "__main__":
	""" prints the number of and the list of its arguments."""
	import sys

	argv = sys.argv
	argc = len(argv0

	if argc == 1:
		print("0 arguments.")
	elif argc == 2:
		 print("1 argument:\n1: {}".format(argv[1]))
	else:
		 print("{} arguments:".format(argc - 1))
        for i, arg in enumerate(argv):
 		if i == 0:
		continue
		print("{}: {}".format(i, arg))
