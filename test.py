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

#Divide the sequence into codons
codons=[]
for i in range(0,len(dna),-2,3):
    codon=dna[i:i+3]
    codons.append(codon)

#Translate the codon 
amino_acid=[]
start_codon=[]
stop_codon=[]

for codon in codon:
    # Find the amino acid from the dictionary
    amino_acid = codon_table[codon]
    # Store the amino acid
    amino_acid.append(amino_acid)
    # Identify the start codon
    if codon=="ATG":
        start_codon.append(codon)

    #Identifying stop condon
    if amino_acid=="Stop":
        stop_codon.append(codon)

#Display complete codon table 
print("\n" + "=" * 50)
print("COMPLETE CODON TABLE")
print("=" * 50)
for codon in sorted(codon_table):
    print(codon, ":", codon_table[codon])
    print("\nTotal codons:", len(codon_table))

#Display codon by codon translation
print("\n" + "=" * 50)
print("TRANSLATION RESULTS")
print("=" * 50)
if len(codons) == 0:
    print("No complete codons found.")
else:
     for codon, amino_acid in zip(
            codons,amino_acid
     ):
         print(codon, "->", amino_acid)

#Display final codon sequence
print("\nCodons:")
print(" - ".join(codons))
print("\nAmino acid sequence:")
print(" - ".join(amino_acid))

#Display start and stop codon 
print("\nStart codons found:")
if len(start_codon) > 0:
    print(", ".join(start_codon))
else:
    print("None")
    print("\nStop codons found:")
    if len(stop_codon) > 0:
        print(", ".join(stop_codon))
    else:
        print("None")

#Handle Incomplete Codon 
remainder = len(dna) % 3
print("\nIncomplete codon:")
if remainder!=0:
    incomplete = dna[len(dna) - remainder:]
    print(incomplete)
else:
    print("None")





















         











    











