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
    vowels = {
        "open": frozenset(["æ"]),
        "close": frozenset(["ɪ", "ʊ"]),
        "mid": frozenset(["ə", "ɒ"]),

        "rounded": frozenset(["æ", "ʊ", "ɒ"]),
        "unrounded": frozenset(["ɪ", "ə"]),

        "front": frozenset(["æ", "ɪ"]),
        "back": frozenset(["ʊ", "ɒ"])
    }

    dipthongs = frozenset(['aɪ', 'əʊ', 'ɪə', 'aʊ', 'ɔɪ', 'ɪʊ'])
    thriptons = frozenset(['aɪə', 'aʊə', 'ɔɪə'])

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
