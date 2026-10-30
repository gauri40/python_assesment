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
# Build the RNA codon table from the DNA one by replacing T with U
rna_codon_table = {codon.replace("T", "U"): amino for codon, amino in codon_table.items()}

print("=" * 50)
print("DNA / RNA Codon Translator")
print("=" * 50)
# Take input sequence from the user
sequence = input("\nEnter a DNA or RNA sequence:").upper().strip()

# Authincate the sequence
error = None
if sequence == "":
    error = "The sequence cannot be empty"
elif "T" in sequence and "U" in sequence:
    error = "DNA and RNA bases cannot be together"
elif not (set(sequence) <= set("ATGC") or set(sequence) <= set("AUGC")):
    error = "Invalid sequence.\nUse only A, T, G, C for DNA.\nUse only A, U, G, C for RNA."

if error:
    print("\nError:", error)
    raise SystemExit
# Detect type and convert everything to RNA (replace thymine T with uracil U)
if "U" in sequence:
    sequence_type = "RNA"
    rna = sequence
else:
    sequence_type = "DNA"
    rna = sequence.replace("T", "U")