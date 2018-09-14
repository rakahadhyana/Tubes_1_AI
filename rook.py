from print import printBoard

def rookEat(rook, state):
  count = 0
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
      count += 1
  # Search nearest Down
  if len(down) > 0:
    nearestDown = down[0]
    for catur in down:
      if rook["y"] - catur["y"] < rook["y"] - nearestDown["y"]:
        nearestDown = catur
    if nearestDown["color"] != rook["color"]:
      count += 1
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
      count += 1
  # Search nearest Left
  if len(left) > 0:
    nearestLeft = left[0]
    for catur in left:
      if rook["x"] - catur["x"] < rook["x"] - nearestLeft["x"]:
        nearestLeft = catur
    if nearestLeft["color"] != rook["color"]:
      count += 1
  return count

<<<<<<< HEAD:solve.py
def bishopEat(bishop, state):
  count_right_diagonal = 0
  # search right diagonal /
  right_diagonal = []
  for catur in state:
    if catur["x"] - bishop["x"] == catur["y"] - bishop["y"]:
      right_diagonal.append(catur)
  # get up and down
  upright = []
  downleft = []
  for catur in right_diagonal:
    if catur["x"] > bishop["x"] and catur["y"] > bishop["y"]:
      upright.append(catur)
    elif catur["x"] < bishop["x"] and catur["y"] < bishop["y"]:
      downleft.append(catur)
  print(right_diagonal)
  # Search nearest Up
  if len(upright) > 0:
    nearestUpright = upright[0]
    for catur in upright:
      if catur["x"] - bishop["x"] < nearestUpright["x"] - bishop["x"] and catur["y"] - bishop["y"] < nearestUpright["y"] - bishop["y"]:
        nearestUpright = catur
    if nearestUpright["color"] != bishop["color"]:
      count_right_diagonal += 1
  # Search nearest Down
  if len(downleft) > 0:
    nearestDownleft = downleft[0]
    for catur in downleft:
      if bishop["y"] - catur["y"] < bishop["y"] - nearestDownleft["y"] and bishop["y"] - catur["y"] < bishop["y"] - nearestDownleft["y"]:
        nearestDownleft = catur
    if nearestDownleft["color"] != bishop["color"]:
      count_right_diagonal += 1
  
  # search left diagonal /
  count_left_diagonal = 0
  left_diagonal = []
  for catur in state:
    if catur["x"] + catur["y"] == bishop["x"] + bishop["y"]:
      left_diagonal.append(catur)
  # get up and down
  upleft = []
  downright = []
  for catur in left_diagonal:
    if catur["x"] < bishop["x"] and catur["y"] > bishop["y"]:
      upleft.append(catur)
    elif catur["x"] > bishop["x"] and catur["y"] < bishop["y"]:
      downright.append(catur)
  print(left_diagonal)
  # Search nearest Up
  if len(upleft) > 0:
    nearestUpleft = upleft[0]
    for catur in upleft:
      if catur["x"] - bishop["x"] > nearestUpleft["x"] - bishop["x"] and catur["y"] - bishop["y"] > nearestUpleft["y"] - bishop["y"]:
        nearestUpleft = catur
    if nearestUpleft["color"] != bishop["color"]:
      count_left_diagonal += 1
  # Search nearest Down
  if len(downright) > 0:
    nearestDownright = downright[0]
    for catur in downright:
      if bishop["y"] - catur["y"] > bishop["y"] - nearestDownright["y"] and bishop["y"] - catur["y"] > bishop["y"] - nearestDownright["y"]:
        nearestDownright = catur
    if nearestDownright["color"] != bishop["color"]:
      count_left_diagonal += 1
  count = count_left_diagonal + count_right_diagonal
  return count








  
=======
>>>>>>> 1a126f16c32e4826dcfb83293ad5a291aeaf00e5:rook.py
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
      "color": "BLACK"
    },
    {
      "type": "QUEEN",
      "x": 2,
      "y": 7,
      "color": "BLACK"
    },
    {
      "type": "QUEEN",
      "x": 2,
      "y": 1,
      "color": "BLACK"
    },
	{
	  "type": "QUEEN",
      "x": 5,
      "y": 3,
      "color": "BLACK"
	},
	{
	  "type": "BISHOP",
      "x": 2,
      "y": 2,
      "color": "WHITE"
<<<<<<< HEAD:solve.py
	},
	{
	  "type": "QUEEN",
      "x": 1,
      "y": 1,
      "color": "BLACK"
	},
	{
	  "type": "QUEEN",
      "x": 3,
      "y": 1,
      "color": "BLACK"
	},
	{
	  "type": "QUEEN",
      "x": 1,
      "y": 3,
      "color": "BLACK"
	}
=======
    },
    {
      "type": "BISHOP",
      "x": 6,
      "y": 3,
      "color": "BLACK"
    }
>>>>>>> 1a126f16c32e4826dcfb83293ad5a291aeaf00e5:rook.py
  ]
  printBoard(state)
  print(rookEat(state[0], state))
  print("ngentot")
  print(bishopEat(state[5], state))


if __name__ == '__main__':
  main()