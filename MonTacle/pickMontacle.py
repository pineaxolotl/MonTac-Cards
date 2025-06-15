import random
cards = []

for path in os.listdir(r"MonTac-Cards\\"):
  if path.endswith(".PNG"):
    cards.append(path)

n = random.randrange(0, len(cards)-1)
montaclePick = cards[n]
with open('Montac-Cards\\MonTacle\\montacle.txt', 'w') as f:
  f.write(montaclePick)
