'''

Title: XOR decryption

Project-euler problem #: 59

Objective: Given an ASCI encrypted message, and knowing the key is a 3 character, lower-case encryption key, decrypt message and sum the original ASCII values.

Procedure:
1) Read in encrypted message
2) Generate first key to test
3) Loop through message and XOR w/ key
4) Check if common words present to narrow options
5) If no real common words, go back to step 2.  If so, save message.
6) Calculate ASCII sum

'''

import itertools

if __name__ == "__main__":
	encrypted_message = [int(x) for x in open('p059_cipher.txt').read().strip('\n').split(',')]
	common_words = [x for x in open('common.txt').read().strip('\n').split(',')]
	for a,b,c in itertools.product(range(97,123), range(97,123), range(97,123)):
		temp_message = []
		current_key = [a,b,c]
		rotating_index = 0
		for x in encrypted_message:
			temp_message.append(chr(x ^ current_key[(rotating_index+1) % 3]))
		temp_message_str = ''.join(temp_message)
		print temp_message_str
		break
		
