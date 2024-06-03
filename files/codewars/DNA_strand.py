#Can we optimize with hashmaps?
def DNA_strand(dna):
    result = ''
    for letter in dna:
        if letter == 'A':
            result += 'T'
        elif letter == 'T':
            result += 'A'
        elif letter == 'C':
            result += 'G'
        elif letter == 'G':
            result += 'C'
    return result
