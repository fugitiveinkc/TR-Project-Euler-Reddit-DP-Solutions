from string import printable, ascii_letters as letters, punctuation, digits
from itertools import cycle

LETTER_FREQUENCIES = {
    "a": 0.08167,
    "b": 0.01492,
    "c": 0.02782,
    "d": 0.04253,
    "e": 0.12702,
    "f": 0.02228,
    "g": 0.02015,
    "h": 0.06094,
    "i": 0.06966,
    "j": 0.00153,
    "k": 0.00772,
    "l": 0.04025,
    "m": 0.02406,
    "n": 0.06749,
    "o": 0.07507,
    "p": 0.01929,
    "q": 0.00095,
    "r": 0.05987,
    "s": 0.06327,
    "t": 0.09056,
    "u": 0.02758,
    "v": 0.00978,
    "w": 0.0236,
    "x": 0.0015,
    "y": 0.01974,
    "z": 0.00074}


def cipher(message, key):
    return "".join(chr(ord(c) ^ ord(k)) for c, k in zip(message, cycle(key)))


def count_printable():
    """
    For each single-character key, how many ciphertext characters are actually
    printable?

    Answer: too many for this to be a useful way to rate potential keys :-/
    """
    plaintext = (
        "The quick brown fox jumped over the lazy dog."
        "?!@#$%^&*()0987654321\n\t")

    printable_counts = []
    
    for key in range(256):
        ciphertext = cipher(plaintext, chr(key))
        print(repr(ciphertext))
        printable_count = sum(ciphertext.count(c) for c in printable)
        printable_counts.append(printable_count)
        print("printable: ", printable_count)
        print("letters: ", sum(ciphertext.count(c) for c in letters))
        print("punctuation: ", sum(ciphertext.count(c) for c in punctuation))
        print("digits: ", sum(ciphertext.count(c) for c in digits))
        print()

    print("printable counts: ", printable_counts)    


if __name__ == "__main__":
    count_printable()
