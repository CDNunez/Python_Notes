
#? Lists and Dictionaries Continued

bag = {}
bag['key items'] = ['town map', 'bike', 'old rod']

poke_ball = 10
great_ball = 5
premier_ball = 1
rare_candy = 1
repel = 5
escape_rope = 2

bag['Poke Balls'] = [poke_ball, great_ball,premier_ball]
bag['Items'] = [rare_candy, escape_rope, repel]

bag['TM&HM Case'] = {'HM01': "Cut", 'HM02' : 'Surf'}

print(bag)

for item in bag['Items']:
    print(item) # prints the values of the vars

for move in bag['TM&HM Case']:
    print(bag['TM&HM Case'][move]) #prints Cut and Surf

#looping thru strings like lists
for letter in 'Pokemon':
    print(letter)

#* Oldale Poke Mart
oldale_poke_mart = {}
oldale_poke_mart['prices'] = {'poke ball' : 200, 'potion' : 300, 'antidote' : 100, 'paralyz heal' : 200, 'awakening' : 250}
oldale_poke_mart['stock'] = {'poke ball' : 10, 'potion' : 5, 'antidote' : 0, 'paralyz heal' : 20, 'awakening' : 2}

print('')
print ("Welcome to Oldale's Poke Mart")
print('')

for key in oldale_poke_mart['prices']:
    print (key)
    print('price: %s' % oldale_poke_mart['prices'][key])
    print('stock: %s' % oldale_poke_mart['stock'][key])
    print('')#for readability

#inventory worth
print('')
total = 0
for key in oldale_poke_mart['prices']:
    count = oldale_poke_mart['prices'][key] * oldale_poke_mart['stock'][key]
    total += count
print('Oldale\'s Poke Mart inventory total : %s' % total)