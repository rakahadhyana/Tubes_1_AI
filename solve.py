def rookEat(rook, state):
  count = 0
  # searc horizontal
  horizontal = []
  for catur in state:
    if catur["x"] == rook["x"]:
      horizontal.append(catur)
  # get up and down
  up = []
  down = []
  for catur in horizontal:
    if catur["y"] > rook["y"]:
      up.append(catur)
    else:
      down.append(catur)
  # Search nearest Up
  if len(up) > 0:
    nearestUp = up[0]
    for catur in up:
      if catur["y"] - rook["y"] < nearestUp["y"] - rook["y"]:
        nearestUp = catur
  if nearestUp["color"] != rook["color"]:
    count += 1
  # Search nearest Down
  if len(down) > 0:
    nearestDown = down[0]
    for catur in down:
      if rook["y"] - catur["y"] < rook["y"] - nearestDown["y"]:
        nearestDown = catur
  if nearestDown["color"] != rook["color"]:
    count += 1

def main():
  

if __name__ == '__main__':
  main()