# N-ything Problem

## Description
N-ything problem is a modification of the N-queen problem. The difference is that chess is considered not only queen (queen), but also includes knights, elephants (bishops), and rooks.

Local Search Algorithm we use:
  1. Hill climbing
  2. Simulated annealing
  3. Genetic algorithm

Elements:
  1. Knight (move L)
  2. Bishop (move diagonal)
  3. Rook (move vertical)
  4. Queen (move diagonal and vertical)

Input format: <colour> <element type> <count> (file)
  ```
  WHITE KNIGHT 2
  WHITE BISHOP 2
  WHITE ROOK 2
  WHITE QUEEN 2
  BLACK KNIGHT 0
  BLACK BISHOP 0
  BLACK ROOK 0
  BLACK QUEEN 0
  ```
  
Output format:
  ```
  ......K.
  .K......
  ........
  .B.....B
  .....R..
  ....R...
  ..Q.....
  Q.......
  0 0
  ```

Board Size: 
  8 x 8

Files description:
  <br>`solver.py` : solve the n-ything problem
  <br>`printer.py` : print output
  <br>`parser.py` : parse user-input into 2D array
  <br>`main.py` : run the n-ything problem solver

## Authors
* **Dinda Yora Islami** - 13516067
* **Haifa Fadhila Ilma** - 13516076
* **Timothy Thamrin A. H. S** - 13516090
* **Raka Hadhyana** - 13516099
* **Dimas Aditia Pratikto** - 13516153
