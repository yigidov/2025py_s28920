# s8920_2025.py
# ---------------------------------------------------------
# Purpose:
# This program generates a random DNA nucleotide sequence
# and writes it in FASTA format. It takes input from the
# user for sequence length, ID, description, and name.
# It calculates nucleotide percentages and CG/AT ratio,
# then inserts the name into the sequence without affecting
# statistical calculations. The sequence is saved in a file
# named {ID}.fasta.
#
# Context of use:
# This script is part of an assignment for generating
# and analyzing random DNA sequences in FASTA format.
# ---------------------------------------------------------

import random

# Define valid DNA nucleotides
nucleotides = ['A', 'C', 'G', 'T']

# Prompt the user for input parameters
seq_length = int(input("Enter the sequence length: "))
seq_id = input("Enter the sequence ID: ")
description = input("Provide a description of the sequence: ")
name = input("Enter your name: ")

# Generate a random DNA sequence of specified length
# ORIGINAL:
# sequence = ''.join(random.choices(nucleotides, k=seq_length))
# MODIFIED (explanation: used SystemRandom for cryptographic-quality randomness):
secure_random = random.SystemRandom()
sequence = ''.join(secure_random.choices(nucleotides, k=seq_length))

# Insert the user's name at a random position in the sequence
# ORIGINAL:
# insert_position = random.randint(0, len(sequence))
# MODIFIED (explanation: use secure_random for consistent randomness quality):
insert_position = secure_random.randint(0, len(sequence))
sequence_with_name = sequence[:insert_position] + name + sequence[insert_position:]

# Count nucleotide frequencies (ignoring the inserted name)
# MODIFIED (justification: added function for modularity and reuse)
def calculate_nucleotide_frequencies(seq):
    """Calculates frequency of each nucleotide in the sequence."""
    counts = {nt: seq.count(nt) for nt in nucleotides}
    total = len(seq)
    percentages = {nt: (counts[nt] / total) * 100 for nt in nucleotides}
    return counts, percentages

# ORIGINAL:
# a_count = sequence.count('A')
# c_count = sequence.count('C')
# g_count = sequence.count('G')
# t_count = sequence.count('T')
# MODIFIED (explanation: replaced with cleaner function call)
counts, percentages = calculate_nucleotide_frequencies(sequence)

# Calculate CG to AT ratio
# Avoid division by zero
at_total = counts['A'] + counts['T']
cg_total = counts['C'] + counts['G']
cg_at_ratio = (cg_total / at_total * 100) if at_total != 0 else 0.0

# Write the sequence to a FASTA file
filename = f"{seq_id}.fasta"
with open(filename, 'w') as fasta_file:
    # FASTA header
    fasta_file.write(f">{seq_id} {description}\n")
    # Sequence with inserted name
    fasta_file.write(sequence_with_name + "\n")

# Notify user of successful write
print(f"\nThe sequence was saved to the file {filename}")

# Print statistics
print("Sequence statistics:")
for nt in nucleotides:
    print(f"{nt}: {percentages[nt]:.1f}%")
print(f"%CG: {cg_total / len(sequence) * 100:.1f}")

# ADDITIONAL IMPROVEMENT:
# MODIFIED (justification: formatted output and added error handling for robustness)
# Wrap main logic in function and try-except block
# Original was a flat script

# ORIGINAL:
# seq_length = int(input("Enter the sequence length: "))
# MODIFIED:
# Now wrapped in main() and error-handled for robustness
# Uncomment below if you want to encapsulate the whole logic for larger applications

# def main():
#     try:
#         <... full code here ...>
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# if __name__ == "__main__":
#     main()

# This was omitted in final form for simplicity, but advisable in production code.
