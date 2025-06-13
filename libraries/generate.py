import random
'''
coin = random.choice (['heads','tails'])
print ('you flipped a coin and it landed on:', coin)
'''

'''
number = random.randint(1, 10)
print('the number you got is:', number)
'''

cards= ['jack','queen','king']
random.shuffle(cards)
print('the shuffled cards are:')
for card in cards:
    print(card)