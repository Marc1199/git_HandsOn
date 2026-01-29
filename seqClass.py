#!/usr/bin/env python
# Classify a sequence as DNA or RNA and optionally search for a motif

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif to search")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

seq = args.seq.upper()   #Note we just added this line

if not re.fullmatch(r"[ACGTU]+", seq):
    print("The sequence is not DNA nor RNA (invalid characters found)")
    sys.exit(1)

contains_T = "T" in seq
contains_U = "U" in seq

if contains_T and contains_U:
    print("Invalid sequence: contains both T and U")
elif contains_T:
    print("The sequence is DNA")
elif contains_U:
    print("The sequence is RNA")
else:
    print("The sequence can be DNA or RNA")

if args.motif:
    motif = args.motif.upper()
    print(f'Motif search enabled: looking for "{motif}" in the sequence')
    if re.search(motif, seq):
        print("I FOUND SOMETHING")
    else:
        print("NOT FOUND IN ANY PLACE")
