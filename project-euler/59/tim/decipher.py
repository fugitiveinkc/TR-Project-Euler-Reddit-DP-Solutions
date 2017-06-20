import re
from string import ascii_lowercase as lowercase
from itertools import product, cycle

# regular expression to find lowercase words
WORDS_RE = re.compile("[a-z]+")

# courtesy of https://en.wikipedia.org/wiki/Letter_frequency
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

EXPECTED_PLAINTEXT = (
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


def decipher(ciphertext, key):
    """Decipher a ciphertext by xoring it with a repeating key"""
    return "".join(chr(ord(c)^ord(k)) for c, k in zip(ciphertext, cycle(key)))


"""
def decipher(ciphertext, key):
    key_length = len(key)
    key_index = 0
    result = ""
    for char in ciphertext:
        result += chr(ord(char) ^ ord(key[key_index]))
        key_index = (key_index + 1) % key_length

    return result
"""


def score(plaintext):
    """
    Calculate a score representing how much the given string "looks like
    english".
    """
    plaintext_words = WORDS_RE.findall(plaintext.lower())
    common_words = ["the", "be", "to", "of", "and", "a", "in", "that", "have"]
    return sum(plaintext_words.count(word) for word in common_words)


assert (score("lkjsdflkjdsf") == 0), "random characters don't have words"
assert (score("the the the") == 3), "three the's"
assert (score("there") == 0), "'there' is not 'the'"
assert (score("to.be") == 2), "'.' is a separator"
assert (score("to be, or not to be") == 4), "'to be or not to be' scores 4"


def score_distribution(text):
    """
    Return the sum of square errors between the distribution of letters in the
    string compared to the distribution of letters in english.
    """
    # calculate distribution
    counts = dict((letter, 0) for letter in lowercase)
    total_count = 0
    for char in text:
        if char in counts:
            counts[char] += 1
            total_count += 1

    # Sum squared errors
    error = 0
    for letter in lowercase:
        freq = float(counts[letter]) / total_counts
        error += (freq - LETTER_FREQUENCIES[letter])**2

    return error


def find_keys_by_freq(text):
    """
    For each single letter key, try deciphering the text, and find the error
    between the resulting potential plaintext's letter frequencies and english.
    Return a list of (key, plaintext) pairs, sorted by error, ascending.
    """
    plaintexts = [(key, decipher(text, key)) for key in letters]
    plaintexts.sort(key=(lambda pair: score_distribution(pair[1])))
    return plaintexts


def split_string(text, n):
    """
    Split a string into n groups on a rotating basis. For example,
    split_string("lkjsdf", 3) will generate groups of every third character,
    and return ["ls", "kd", "jf"]. If the string is a ciphertext with a key of
    length 3, this returns the characters that each character of the key would
    apply to.
    """
    groups = [list() for _ in range(n)]
    key_index = 0
    for char in text:
        groups[n].append(char)
        n = (n + 1) % key_length
    return groups


# BRUTE FORCE brute force
def break_cipher(ciphertext, key_length):
    """
    Test every possible key and return the ones with the highest english-
    language score.
    """
    best_score = -1
    best_key = None
    best_plaintext = None

    for k1, k2, k3 in product(lowercase, lowercase, lowercase):
        key = k1 + k2 + k3
        plaintext = decipher(ciphertext, key)
        key_score = score(plaintext)
        if key_score > best_score:
            # If debugging, print best so far
            # print("decrypt('", key, "'): ", plaintext, sep="")
            # print("with score ", key_score)
            # print()
            best_score = key_score
            best_key = key
            best_plaintext = plaintext

    return best_plaintext


if __name__ == "__main__":
    with open("cipher.txt") as f:
        data = [chr(int(x)) for x in f.read().strip().split(",")]

    key_length = 3

    # Split into KEY_LENGTH groups, all of the characters that had the same key
    groups = [list() for _ in range(key_length)]
    n = 0
    for char in data:
        groups[n].append(char)
        n = (n + 1) % key_length

    # Now for each group we can use char distributions to find likely keys
    plaintext = break_cipher(data, 3)
    assert (plaintext == EXPECTED_PLAINTEXT)
    print(sum(ord(char) for char in plaintext))
