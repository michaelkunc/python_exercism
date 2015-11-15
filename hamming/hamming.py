def distance(first_strand, second_strand):
    return len([a for a, b in zip(first_strand, second_strand) if a != b])
