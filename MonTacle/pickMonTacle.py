import os
import random

cards_dir = os.path.join(os.path.dirname(__file__), "..")
cards = []

blacklist_path = os.path.join(os.path.dirname(__file__), "blacklist.txt")
with open(blacklist_path, 'r') as f:
  blacklist = [line.strip() for line in f]

for path in os.listdir(cards_dir):
  if path.endswith(".PNG") and path not in blacklist:
    cards.append(path)

n = random.randrange(len(cards))
montaclePick = cards[n].replace(".PNG", "")

output_path = os.path.join(os.path.dirname(__file__), "montacle.txt")
with open(output_path, 'w') as f:
  f.write(montaclePick)

if len(blacklist) >= 2:
  with open(blacklist_path, 'w') as f:
    f.writelines(blacklist[1:])
with open(blacklist_path, 'a') as f:
  f.write(montaclePick + ".PNG\n")
