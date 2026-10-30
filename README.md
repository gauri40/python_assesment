DNA / RNA Codon Translator
A command-line Python program that takes a DNA or RNA sequence, converts it to RNA, splits it into codons, and translates it into amino acids using the standard genetic code.

Features
Accepts DNA (A, T, G, C) or RNA (A, U, G, C) input, in upper or lower case
Validates the input (empty sequence, invalid characters, mixed T and U)
Converts DNA to RNA by replacing thymine (T) with uracil (U)
Builds the RNA codon table from the standard 64-codon DNA table
Splits the sequence into complete 3-nucleotide codons
Translates each codon into its amino acid
Identifies the start codon (AUG) and stop codons (UAA, UAG, UGA)
Reports any incomplete codon left at the end of the sequence
Prints the full codon table and a project summary

Requirements
Python 3.8 or newer
No external libraries needed

How It Works
Input and validation: the sequence is converted to upper case and checked. Empty input, characters other than A/T/G/C/U, and sequences containing both T and U are rejected with an error message.
DNA to RNA conversion: DNA input has every T replaced by U. RNA input is used as it is.
Codon splitting: the RNA is cut into groups of three bases. A leftover group of one or two bases is reported as an incomplete codon.
Translation: each codon is looked up in the RNA codon table, which is built from the DNA codon table by replacing T with U in every key.
Output: the program prints the translation, the start and stop codons, the incomplete codon and a summary.