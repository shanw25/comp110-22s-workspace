def locate_substring(dna_snippet, dna):
    result = []
    current_dna: str = ""
    i: int = 0
    while i < len(dna) - 4:
        current_dna = dna[i]
        current_dna += dna[i + 1]
        current_dna += dna[i + 2]
        current_dna += dna[i + 3]
        if current_dna == dna_snippet:
            result.append(i)
        i += 1
    return result


print(locate_substring("ATAT", "GATATATGCATATACTT"))