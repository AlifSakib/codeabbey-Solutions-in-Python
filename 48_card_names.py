inp = input()
v = []
a = map(int, raw_input().split())
suits = ['Clubs','Spades','Diamonds','Hearts']
ranks = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
for i in a:
	card_value = i
	suit_rank = card_value / 13
	rank_value = card_value % 13
	suit = suits[suit_rank]
	rank = ranks[rank_value]
	val = rank + '-of-' + suit
	v.append(val)
print ' '.join(v)