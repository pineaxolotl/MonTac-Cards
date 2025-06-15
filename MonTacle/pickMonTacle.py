import os
import random

cards_dir = os.path.join(os.path.dirname(__file__), "..")
cards = []

blacklist_path = os.path.join(os.path.dirname(__file__), "blacklist.txt")
with open(blacklist_path, 'r') as f:
  blacklist = [line.strip() + ".PNG" for line in f]

for path in os.listdir(cards_dir):
  if path.endswith(".PNG"):
    cards.append(path)

n = random.randrange(len(cards))
montaclePick = cards[n].replace(".PNG", "")

output_path = os.path.join(os.path.dirname(__file__), "montacle.txt")
with open(output_path, 'w') as f:
  f.write(montaclePick)

with open(blacklist_path, 'w' as f:
    lines = f.readlines()
    if len(blacklist) => 30:
      f.writelines(lines[1:])
    f.write(montaclePick)
