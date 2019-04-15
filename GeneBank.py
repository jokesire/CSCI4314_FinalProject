from Bio import SeqIO
for seq_record in SeqIO.parse("sequence.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

sequence_dict = SeqIO.index("sequence.fasta", "fasta")
print(sequence_dict)
