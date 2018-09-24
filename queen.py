from print import printBoard

def queenEat(queen, state):
  countDiff = 0
  countSame = 0
  # searc horizontal
  horizontal = []
  for catur in state:
    if catur["x"] == queen["x"] and catur["y"] != queen["y"]:
      horizontal.append(catur)
  # get up and down
  up = []
  down = []
  for catur in horizontal:
    if catur["y"] > queen["y"]:
      up.append(catur)
    else:
      down.append(catur)
  # Search nearest Up
  if len(up) > 0:
    nearestUp = up[0]
    for catur in up:
      if catur["y"] - queen["y"] < nearestUp["y"] - queen["y"]:
        nearestUp = catur
    if nearestUp["color"] != queen["color"]:
      countDiff += 1
    else:
      countSame += 1  
  # Search nearest Down
  if len(down) > 0:
    nearestDown = down[0]
    for catur in down:
      if queen["y"] - catur["y"] < queen["y"] - nearestDown["y"]:
        nearestDown = catur
    if nearestDown["color"] != queen["color"]:
      countDiff += 1
    else:
      countSame += 1 
  # Search vertical
  vertical = []
  for catur in state:
    if catur["y"] == queen["y"] and catur["x"] != queen["x"]:
      vertical.append(catur)
  # get right and left
  right = []
  left = []
  for catur in vertical:
    if catur["x"] > queen["x"]:
      right.append(catur)
    else:
      left.append(catur)
  # Search nearest right
  if len(right) > 0:
    nearestRight = right[0]
    for catur in right:
      if catur["x"] - queen["x"] < nearestRight["x"] - queen["x"]:
        nearestRight = catur
    if nearestRight["color"] != queen["color"]:
      countDiff += 1
    else:
      countSame += 1 
  # Search nearest Left
  if len(left) > 0:
    nearestLeft = left[0]
    for catur in left:
      if queen["x"] - catur["x"] < queen["x"] - nearestLeft["x"]:
        nearestLeft = catur
    if nearestLeft["color"] != queen["color"]:
      countDiff += 1
    else:
      countSame += 1
  count_right_diagonal_same = 0
  count_right_diagonal_diff = 0
  # search right diagonal /
  right_diagonal = []
  for catur in state:
    if catur["x"] - queen["x"] == catur["y"] - queen["y"]:
      right_diagonal.append(catur)
  # get up and down
  upright = []
  downleft = []
  for catur in right_diagonal:
    if catur["x"] > queen["x"] and catur["y"] > queen["y"]:
      upright.append(catur)
    elif catur["x"] < queen["x"] and catur["y"] < queen["y"]:
      downleft.append(catur)
  # print(right_diagonal)
  # Search nearest Up
  if len(upright) > 0:
    nearestUpright = upright[0]
    for catur in upright:
      if catur["x"] - queen["x"] < nearestUpright["x"] - queen["x"] and catur["y"] - queen["y"] < nearestUpright["y"] - queen["y"]:
        nearestUpright = catur
    if nearestUpright["color"] != queen["color"]:
      count_right_diagonal_diff += 1
    else:
      count_right_diagonal_same += 1  
  # Search nearest Down
  if len(downleft) > 0:
    nearestDownleft = downleft[0]
    for catur in downleft:
      if queen["y"] - catur["y"] < queen["y"] - nearestDownleft["y"] and queen["y"] - catur["y"] < queen["y"] - nearestDownleft["y"]:
        nearestDownleft = catur
    if nearestDownleft["color"] != queen["color"]:
      count_right_diagonal_diff += 1
    else:
      count_right_diagonal_same += 1 
  
  # search left diagonal /
  count_left_diagonal_diff = 0
  count_left_diagonal_same = 0
  left_diagonal = []
  for catur in state:
    if catur["x"] + catur["y"] == queen["x"] + queen["y"]:
      left_diagonal.append(catur)
  # get up and down
  upleft = []
  downright = []
  for catur in left_diagonal:
    if catur["x"] < queen["x"] and catur["y"] > queen["y"]:
      upleft.append(catur)
    elif catur["x"] > queen["x"] and catur["y"] < queen["y"]:
      downright.append(catur)
  # print(left_diagonal)
  # Search nearest Up
  if len(upleft) > 0:
    nearestUpleft = upleft[0]
    for catur in upleft:
      if catur["x"] - queen["x"] > nearestUpleft["x"] - queen["x"] and catur["y"] - queen["y"] > nearestUpleft["y"] - queen["y"]:
        nearestUpleft = catur
    if nearestUpleft["color"] != queen["color"]:
      count_left_diagonal_diff += 1
    else:
      count_left_diagonal_same += 1  
  # Search nearest Down
  if len(downright) > 0:
    nearestDownright = downright[0]
    for catur in downright:
      if queen["y"] - catur["y"] > queen["y"] - nearestDownright["y"] and queen["y"] - catur["y"] > queen["y"] - nearestDownright["y"]:
        nearestDownright = catur
    if nearestDownright["color"] != queen["color"]:
      count_left_diagonal_diff += 1
    else:
      count_left_diagonal_same += 1
  count_diagonal_same = count_left_diagonal_same + count_right_diagonal_same      
  count_diagonal_diff = count_left_diagonal_diff + count_right_diagonal_diff
  return {"same": countSame + count_diagonal_same, "diff": countDiff + count_diagonal_diff} 

def main():
  state = [
    {
      "type": "QUEEN",
      "x": 2,
      "y": 3,
      "color": "WHITE"
    },
    {
      "type": "QUEEN",
      "x": 4,
      "y": 5,
      "color": "BLACK"
    },
    {
      "type": "QUEEN",
      "x": 1,
      "y": 4,
      "color": "WHITE"
    },
    {
      "type": "QUEEN",
      "x": 1,
      "y": 2,
      "color": "WHITE"
    },
    {
      "type": "ROOK",
      "x": 6,
      "y": 3,
      "color": "BLACK"
    },
    {
      "type": "KNIGHT",
      "x": 5,
      "y": 6,
      "color": "WHITE"
    }    
  ]
  printBoard(state)
  print(queenEat(state[0], state))  

if __name__ == '__main__':
  main()