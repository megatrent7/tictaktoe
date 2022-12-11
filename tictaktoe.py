# Initialize the board
board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

# Print the current state of the board
def print_board():
  for row in board:
    print(" ".join(row))

# Check if a player has won
def has_won(player):
  # Check the rows
  for row in board:
    if row == [player, player, player]:
      return True
      
  # Check the columns
  for col in range(3):
    if board[0][col] == player and board[1][col] == player and board[2][col] == player:
      return True
      
  # Check the diagonals
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
    
  # If none of the above conditions are met, then the player has not won
  return False

# Check if the game is a draw
def is_draw():
  # If there are any empty spaces on the board, then the game is not a draw
  for row in board:
    if "-" in row:
      return False
  
  # If there are no empty spaces on the board, then the game is a draw
  return True

# Play the game
player = "X"
while True:
  # Print the current state of the board
  print_board()
  
  # Ask the player for their move
  row = int(input("Enter row (0-2): "))
  col = int(input("Enter col (0-2): "))
  
  # Make the move
  if board[row][col] == "-":
    board[row][col] = player
  else:
    print("That space is already taken! Try again.")
    continue
  
  # Check if the player has won
  if has_won(player):
    print(f"{player} has won the game!")
    break
  
  # Check if the game is a draw
  if is_draw():
    print("The game is a draw!")
    break
  
  # Switch players
  if player == "X":
    player = "O"
  else:
    player = "X"