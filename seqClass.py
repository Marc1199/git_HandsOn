#!/usr/bin/env python
#Here we are practicing the push on git.
import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()                 # Note we just added this line

# Validate sequence is not empty
if not args.seq.strip():
    print('Error: sequence cannot be empty')
    sys.exit(1)

if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for the motif "{args.motif}" in the sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("I FOUND SOMETHING")
    else:
        print("NOT FOUND IN ANY PLACE") 

