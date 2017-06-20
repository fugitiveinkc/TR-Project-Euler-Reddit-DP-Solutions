from string import printable, ascii_letters as letters, punctuation, digits
from string import ascii_lowercase as lowercase
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

PLAINTEXT = (
    "(The Gospel of John, chapter 1) 1 In the beginning the Word already "
    "existed. He was with God, and he was God. 2 He was in the beginning with "
    "God. 3 He created everything there is. Nothing exists that he didn't "
    "make. 4 Life itself was in him, and this life gives light to everyone. 5 "
    "The light shines through the darkness, and the darkness can never "
    "extinguish it. 6 God sent John the Baptist 7 to tell everyone about the "
    "light so that everyone might believe because of his testimony. 8 John "
    "himself was not the light; he was only a witness to the light. 9 The one "
    "who is the true light, who gives light to everyone, was going to come "
    "into the world. 10 But although the world was made through him, the "
    "world didn't recognize him when he came. 11 Even in his own land and "
    "among his own people, he was not accepted. 12 But to all who believed "
    "him and accepted him, he gave the right to become children of God. 13 "
    "They are reborn! This is not a physical birth resulting from human "
    "passion or plan, this rebirth comes from God.14 So the Word became human "
    "and lived here on earth among us. He was full of unfailing love and "
    "faithfulness. And we have seen his glory, the glory of the only Son of "
    "the Father.")


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


def compare_distributions():
    """
    Compare letter distributions in text to expected distributions in the
    english language. The difference in distributions will be calculated as the
    sum of the squares of differences in frequency for each letter.

    It looks like this is a useful measure! The error for the actual plaintext
    is < .003, and the next smallest error is .0388! At the very least this
    would be good to eliminate most of the possible characters in the key!
    """
    errors = []
    for key in range(256):
        text = cipher(PLAINTEXT, chr(key))

        # count characters in plaintext
        distribution = dict((letter, 0) for letter in lowercase)
        total_chars = 0
        for char in text:
            if char in distribution:
                distribution[char] += 1
                total_chars += 1

        # Since some texts may not have any letters
        if total_chars == 0:
            continue
    
        # sum up the squares of the errors for each letter
        error = 0
        for char in lowercase:
            freq = distribution[char] / float(total_chars)
            error += (freq - LETTER_FREQUENCIES[char])**2
    
        errors.append(error)

    return errors


if __name__ == "__main__":
    # count_printable()
    errors = compare_distributions()
    print(errors)
    errors.sort()
    print(errors)
