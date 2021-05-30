from random import choices

population = ["ə", "n", "r", "t", "ɪ", "s", "d", "l", "i", "k", "m", "p", "æ", "w", "u", "b", "f", "aɪ", "ɑ", "h", "o",
              "ɒ", "ŋ", "ʃ", "j", "g", "tʃ", "aʊ", "ʊ", "θ", "ɔɪ", "əʊ", "ɪə", "ɪʊ", "aɪə", "aʊə", "ɔɪə"]
commonness = [11.49, 7.11, 6.94, 6.91, 6.32, 4.75, 4.21, 3.96, 3.61, 3.18, 2.76, 2.15, 2.10, 1.95, 1.93, 1.80, 1.71,
              1.50, 1.45, 1.40, 1.25, 1.18, 0.99, 0.97, 0.81, 0.80, 0.56, 0.50, 0.43, 0.41, 0.10, 0.10, 0.10, 0.10,
              0.10, 0.10, 0.10]

consonants = ['m', 'n', 'ɲ', 'ŋ', 'b', 'd', 'g', 'b', 'd', 'g', 'w', 'ɹ', 'j', 'r', 'l', 'p', 't', 'k', 'f', 'θ', 's',
              'ʃ', 'x', 'h']
vowels = ["æ", "ʊ", "ɒ", "ɪ", "ə", 'aɪ', 'əʊ', 'ɪə', 'aʊ', 'ɔɪ', 'ɪʊ', 'aɪə', 'aʊə', 'ɔɪə']

structure = "CVCC"
for i in range(10):
    while "C" in structure or "V" in structure:
        item = choices(population, weights=commonness)[0]
        if item in consonants:
            structure = structure.replace('C', item, 1)
        elif (item in vowels) and (item != 'ə'):
            structure = structure.replace('V', item, 1)

    print(structure)
    structure = 'CVCC'
