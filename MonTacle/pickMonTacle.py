import os
import random

cards_dir = os.path.join(os.path.dirname(__file__), "..")
cards = []

for path in os.listdir(cards_dir):
  if path.endswith(".PNG"):
    cards.append(path)

n = random.randrange(0, len(cards)-1)
print(n)
montaclePick = cards[n]

output_path = os.path.join(os.path.dirname(__file__), "montacle.txt")
with open(output_path, 'w') as f:
  f.write(montaclePick)
