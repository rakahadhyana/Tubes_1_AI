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