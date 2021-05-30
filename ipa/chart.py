class IPAConsonantChart:
    manner = {
        "nasal": frozenset(["m", "n", "ɲ", "ŋ"]),
        "plosive": frozenset(["p", "b", "t", "d", "k", "g", "Ɂ"]),
        "fricative": frozenset(["f", "v", "θ", "ð", "s", "z", "ʃ", "ʒ", "x", "h"]),
        "aproximant": frozenset(["w", "ɹ", "j"]),
        "affricate": frozenset(["ts", "ʧ", "dʒ"]),
        "trill": frozenset(["r"]),
        "lateral": frozenset(["l"])
    }

    place = {
        "bilabial": frozenset(["m", "p", "b", "w"]),
        "labiodental": frozenset(["f", "v"]),
        "dental": frozenset(["θ", "ð"]),
        "alveolar": frozenset(["n", "t", "d", "s", "z", "ɹ", "ts", "r", "l"]),
        "postalveolar": frozenset(["ʃ", "ʒ", "ʧ", "dʒ"]),
        "palatal": frozenset(["ɲ", "j"]),
        "velar": frozenset(["ŋ", "k", "g", "x"]),
        "glotal": frozenset(["h", "Ɂ"])
    }

    voicing = {
        "voiced": frozenset(["m", "n", "ɲ", "ŋ", "b", "d", "g", "v", "ð", "z", "ʒ", "w", "ɹ", "j", "dʒ", "r", "l"]),
        "voiceless": frozenset(["p", "t", "k", "Ɂ", "f", "θ", "s", "ʃ", "x", "h", "ts", "ʧ"])
    }

    @classmethod
    def get_element(cls, m, p, v):
        return list(cls.manner[m] & cls.place[p] & cls.voicing[v])[0]

    @classmethod
    def get_from(cls, voicing, articulation):
        chart = None
        if articulation in ['nasal', 'plosive', 'fricative', 'aproximant', 'affricate', 'trill', 'lateral']:
            chart = cls.manner[articulation]
        elif articulation in ['bilabial', 'labiodental', 'dental', 'alveolar', 'postalveolar', 'palatal', 'velar',
                              'glotal']:
            chart = cls.place[articulation]

        return list(cls.voicing[voicing] & chart)


class PhonlogicalInventory(IPAConsonantChart):
    dipthongs = frozenset(['aɪ', 'əʊ', 'ɪə', 'aʊ', 'ɔɪ', 'ɪʊ'])
    thriptons = frozenset(['aɪə', 'aʊə', 'ɔɪə'])


class IPASymbol:
    symbol = None


class IPAConsonant(IPASymbol):

    def __init__(self, symbol, place, manner, voicing):
        self.symbol = symbol
        self.place = place
        self.manner = manner
        self.voicing = voicing


class IPAVowel(IPASymbol):
    def __init__(self, symbol, openess, roundness, frontness):
        self.symbol = symbol
        self.openness = openess
        self.roundness = roundness
        self.frontness = frontness


vowels = {
    "open": frozenset(["æ"]),
    "close": frozenset(["ɪ", "ʊ"]),
    "partial": frozenset(["ə", "ɒ"]),

    "rounded": frozenset(["æ", "ʊ", "ɒ"]),
    "unrounded": frozenset(["ɪ", "ə"]),

    "front": frozenset(["æ", "ɪ"]),
    "mid": frozenset(['ə']),
    "back": frozenset(["ʊ", "ɒ"])
}

manner = {
    "nasal": frozenset(['m', 'n', 'ɲ', 'ŋ']),
    "plosive": frozenset(['p', 'b', 't', 'd', 'k', 'g']),
    "fricatives": frozenset(['f', 'θ', 's', 'ʃ', 'x', 'h']),
    "aproximants": frozenset(['w', 'ɹ', 'j']),
    "affricates": frozenset(['ʧ']),
    "trill": frozenset(['r']),
    "lateral": frozenset(['l'])
}
place = {
    "bilabial": frozenset(['m', 'p', 'b', 'w']),
    "labiodental": frozenset(['f']),
    "dental": frozenset(['θ']),
    "alveolar": frozenset(['n', 't', 'd', 's', 'ɹ', 'r', 'l']),
    "postalveolar": frozenset(['ʃ', 'ʧ']),
    "palatal": frozenset(['ɲ', 'j']),
    "velar": frozenset(['ŋ', 'k', 'g', 'x']),
    "glotal": frozenset(['h'])
}
voicing = {
    "voiced": frozenset(['m', 'n', 'ɲ', 'ŋ', 'b', 'd', 'g', 'b', 'd', 'g', 'w', 'ɹ', 'j', 'r', 'l']),
    "voiceless": frozenset(['p', 't', 'k', 'f', 'θ', 's', 'ʃ', 'x', 'h'])
}

Phonlogical_Inventory = []
openess, roundness, frontness = 0, 0, 0
for vowel in ["æ", "ɪ", "ʊ" "ə", "ɒ"]:
    for how_open in ['open', 'close', 'partial']:
        if vowel in vowels[how_open]:
            openess = how_open
    for how_round in ['rounded', 'unrounded']:
        if vowel in vowels[how_round]:
            roundness = how_round
    for how_front in ['front', 'mid', 'back']:
        if vowel in vowels[how_front]:
            frontness = how_front
    symbol = IPAVowel(vowel, openess, roundness, frontness)
    Phonlogical_Inventory.append(symbol)

_place, _manner, _voicing = 0, 0, 0
for consonant in ['m', 'n', 'ɲ', 'ŋ', 'b', 'd', 'g', 'b', 'd', 'g', 'w', 'ɹ',
                  'j', 'r', 'l', 'p', 't', 'k', 'f', 'θ', 's', 'ʃ', 'x', 'h']:
    for the_place in place:
        if consonant in vowels[the_place]:
            _place = how_open
    for the_manner in manner:
        if consonant in vowels[the_manner]:
            _manner = how_round
    for the_voicing in voicing:
        if consonant in vowels[the_voicing]:
            _voicing = how_front
    symbol = IPAConsonant(consonant, _place, _manner, _voicing)
    Phonlogical_Inventory.append(symbol)
