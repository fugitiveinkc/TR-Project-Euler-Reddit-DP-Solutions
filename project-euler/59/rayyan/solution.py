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

Questions:
1) Is there a statistically valid choice for how many common words I should check to determine if a message is a valid English paragraph?
2) What are ways I could optimize this code?

'''

import itertools, sys

def encryption_decryption_method(encrypted_message, current_key):
	rotating_index = 0 #Used as an index to rotate through characters of the key
	temp_message = [] #Used to store current, possible plain text
	for x in encrypted_message:
		rotating_index = rotating_index % len(current_key)
		temp_message.append(chr(x ^ current_key[rotating_index])) #XOR
		rotating_index += 1
	return ''.join(temp_message)

if __name__ == "__main__":

	#Read in encrypted message
	encrypted_message = [int(x) for x in open('p059_cipher.txt').read().strip('\n').split(',')]
	#Create a list with the 10 most common words in the English language
	common_words = [x for x in open('common.txt').read().strip('\n').split(',')]

	#Generate testing keys and loop through XOR
	for a,b,c in itertools.product(range(97,123), range(97,123), range(97,123)):
		current_key = [a,b,c] #Current key being checked

		#SDecrypt message with key
		temp_message_str = encryption_decryption_method(encrypted_message, current_key)
		
		#Check if a valid message.  Measure here is if all 10 words in the common words list is present in the message.
		validity = 0
		for word in common_words:
			if word in temp_message_str:
				validity += 1
		if validity >= 10:
			print "PLAIN TEXT:"
			print temp_message_str
			print "ASCII Sum = " + str(sum([ord(character) for character in temp_message_str]))
			sys.exit()		
