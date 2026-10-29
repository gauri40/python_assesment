# Devlopment of codon table generator
codon_table={
    "TTT":"Phenylalanine",
    "TTC":"Phenylalanine",
    "TTA":"Leucine",
    "TTG":"Leucine",

    "TAT":"Tyrosine",
    "TAC":"Tyrosine",
    "TAA":"Stop",
    "TAG":"Stop",

    "TCT": "Serine",
    "TCC": "Serine",
    "TCA": "Serine",
    "TCG": "Serine",

    "TAT": "Tyrosine",
    "TAC": "Tyrosine",
    "TAA": "Stop",
    "TAG": "Stop",

    "TGT": "Cysteine",
    "TGC": "Cysteine",
    "TGA": "Stop",
    "TGG": "Tryptophan",

    "CTT": "Leucine",
    "CTC": "Leucine",
    "CTA": "Leucine",
    "CTG": "Leucine",

    "CCT": "Proline",
    "CCC": "Proline",
    "CCA": "Proline",
    "CCG": "Proline",

    "CAT": "Histidine",
    "CAC": "Histidine",
    "CAA": "Glutamine",
    "CAG": "Glutamine",

    "CGT": "Arginine",
    "CGC": "Arginine",
    "CGA": "Arginine",
    "CGG": "Arginine",

    "ATT": "Isoleucine",
    "ATC": "Isoleucine",
    "ATA": "Isoleucine",
    "ATG": "Methionine",

    "ACT": "Threonine",
    "ACC": "Threonine",
    "ACA": "Threonine",
    "ACG": "Threonine",

    "AAT": "Asparagine",
    "AAC": "Asparagine",
    "AAA": "Lysine",
    "AAG": "Lysine",

    "AGT": "Serine",
    "AGC": "Serine",
    "AGA": "Arginine",
    "AGG": "Arginine",

    "GTT": "Valine",
    "GTC": "Valine",
    "GTA": "Valine",
    "GTG": "Valine",

    "GCT": "Alanine",
    "GCC": "Alanine",
    "GCA": "Alanine",
    "GCG": "Alanine",

    "GAT": "Aspartic acid",
    "GAC": "Aspartic acid",
    "GAA": "Glutamic acid",
    "GAG": "Glutamic acid",

    "GGT": "Glycine",
    "GGC": "Glycine",
    "GGA": "Glycine",
    "GGG": "Glycine"

} 
print("="*50)
print("Codon Table")
print("="*50)

#Take Input Sequence from the user
sequence= input(
    "\nEnter a DNA or RNA sequence:"
)
#Convert lowercase letters into uppercase
sequence=sequence.upper()

#Validate the sequnce
if sequence =="":
    print("\nError: The sequence cannot be empty")
elif "T" in sequence and "U" in sequence:
    print("\nError: DNA and RNA bases cannot be together")
elif not set(sequence).issubset(set("ATGC")) and not set(sequence).issubset(set("AUGC")):
     print("\nError: Invalid sequence.")
     print("Use only A, T, G, C for DNA.")
     print("Use only A, U, G, C for RNA.")

#Convert RNA into DNA coding format
else:
    if "U" in sequence:
        sequence_type="RNA"
        dna=sequence.replace("U","T")
    else:
        sequence_type="DNA"
        dna=sequence
        print("\nSequence Type:", sequence_type)
        print("\nInput Sequence:", sequence)










