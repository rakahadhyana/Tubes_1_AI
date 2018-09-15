from print import printBoard

def rookEat(rook, state):
  countDiff = 0
  countSame = 0
  # searc horizontal
  horizontal = []
  for catur in state:
    if catur["x"] == rook["x"] and catur["y"] != rook["y"]:
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
      countDiff += 1
    else:
      countSame += 1  
  # Search nearest Down
  if len(down) > 0:
    nearestDown = down[0]
    for catur in down:
      if rook["y"] - catur["y"] < rook["y"] - nearestDown["y"]:
        nearestDown = catur
    if nearestDown["color"] != rook["color"]:
      countDiff += 1
    else:
      countSame += 1 
  # Search vertical
  vertical = []
  for catur in state:
    if catur["y"] == rook["y"] and catur["x"] != rook["x"]:
      vertical.append(catur)
  # get right and left
  right = []
  left = []
  for catur in vertical:
    if catur["x"] > rook["x"]:
      right.append(catur)
    else:
      left.append(catur)
  # Search nearest right
  if len(right) > 0:
    nearestRight = right[0]
    for catur in right:
      if catur["x"] - rook["x"] < nearestRight["x"] - rook["x"]:
        nearestRight = catur
    if nearestRight["color"] != rook["color"]:
      countDiff += 1
    else:
      countSame += 1 
  # Search nearest Left
  if len(left) > 0:
    nearestLeft = left[0]
    for catur in left:
      if rook["x"] - catur["x"] < rook["x"] - nearestLeft["x"]:
        nearestLeft = catur
    if nearestLeft["color"] != rook["color"]:
      countDiff += 1
    else:
      countSame += 1  
  return {"same": countSame, "diff": countDiff}

def main():
  state = [
    {
      "type": "ROOK",
      "x": 2,
      "y": 3,
      "color": "WHITE"
    },
    {
      "type": "QUEEN",
      "x": 2,
      "y": 5,
      "color": "WHITE"
    },
    {
      "type": "QUEEN",
      "x": 2,
      "y": 7,
      "color": "WHITE"
    },
    {
      "type": "QUEEN",
      "x": 2,
      "y": 1,
      "color": "WHITE"
    },
    {
      "type": "BISHOP",
      "x": 6,
      "y": 3,
      "color": "BLACK"
    }
  ]
  printBoard(state)
  print(rookEat(state[0], state))


if __name__ == '__main__':
  main()