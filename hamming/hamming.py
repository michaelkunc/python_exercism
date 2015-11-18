def distance(first_strand, second_strand):
    return sum(a != b  for a, b in zip(first_strand, second_strand))
