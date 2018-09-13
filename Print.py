import sys

def printBoard(state):
  board = []
  for i in range(8):
    board.append(['_','_','_','_','_','_','_','_']);
  for catur in state:
    board[catur["y"] - 1].pop(catur["x"] - 1);
    board[catur["y"] - 1].insert(catur["x"] - 1, catur["jenis"]);
  i = 8;
  for row in reversed(board):
    sys.stdout.write(str(i)+" ");
    i -= 1;
    for grid in row:
      sys.stdout.write(grid + " ");
    print();
  print("  1 2 3 4 5 6 7 8");  
  # print(objective(state));

def main():
  state = [
    {
      "jenis": "Q",
      "x": 5,
      "y": 5,
      "warna": "putih"
    },
    {
      "jenis": "Q",
      "x": 8,
      "y": 8,
      "warna": "putih"
    }, 
    {
      "jenis": "Q",
      "x": 6,
      "y": 5,
      "warna": "putih"
    },   
    {
      "jenis": "R",
      "x": 6,
      "y": 1,
      "warna": "hitam"
    }
  ]
  printBoard(state);

if __name__ == '__main__':
  main()