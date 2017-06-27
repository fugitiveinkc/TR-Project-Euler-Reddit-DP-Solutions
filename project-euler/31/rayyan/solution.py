'''

Question: Given an n amount of dollars and change, how many ways can that amount be broken up into change?

Hint: Dynamic programming may work here

Solution #1: Recursive

'''
		
#Solution 1: Recursive

def make_change(current_amount, current_coin = 200):
	'''
	Function takes the current amount you're trying to break into change
	and checks all possible divisions in pences.  It uses the coin from 
	the last function call to access which pence denominations are usable.
	'''
	if current_amount == 0: #You've reached a possible change combination
		return 1
	variations = 0
	for coin in (x for x in (1,2,5,10,20,50,100,200) if x <= current_coin): #Will cycle through possible coins less than the current value and will break the current amount down further.
		if coin <= current_amount:
			variations += make_change(current_amount-coin, coin) #Keeps track of the amount of change combinations that have been found.
	return variations

if __name__ == "__main__":
	print make_change(200)	#Check 200 pences	
