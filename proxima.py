import argparse
import interpreter
import sys


version = '0.0.3'
debug = False



def parse_args():
	parser = argparse.ArgumentParser()
	parser = argparse.ArgumentParser(description='Official Proxima Language Interpreter.')
	parser.add_argument('file', nargs='?')
	return parser.parse_args()

if __name__ == '__main__':
	args = parse_args()
	
	if not debug:
		sys.tracebacklimit=0


	if args.file:
		with open(args.file) as f:
			interpreter.evaluate(f.read())
