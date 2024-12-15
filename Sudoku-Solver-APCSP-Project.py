#4x4 sudoku solver. For no 2x2 subsquares, comment out lines 49-64 and 120-132. 
import copy
sudoku_puzzle = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

#Get values from user, store in variables.
def getvalues(message):
  print(message)
  
  if message[:9] == "Incorrect":
    print("Remember to format your puzzle correctly.")
  
  for i in range(1, 5):
    row = input("Enter row " + str(i) + ". ")
    sudoku_puzzle[i-1] = row.split()

  for j in range(4):
    for element in sudoku_puzzle[j]:
      if element != "1" and element != "2" and element != "3" and element != "4" and element != "x":
        getvalues("Incorrect formatting. \n" + message)
  
  make_integers()
  print("\nGenerating solutions...")

#Make the values in the array integers, and change the x to 0.
def make_integers():
  for i in range(4):
    for j in range(4):
      if sudoku_puzzle[i][j] == "1":
          sudoku_puzzle[i][j] = 1
          
      if sudoku_puzzle[i][j] == "2":
          sudoku_puzzle[i][j] = 2
          
      if sudoku_puzzle[i][j] == "3":
          sudoku_puzzle[i][j] = 3
          
      if sudoku_puzzle[i][j] == "4":
          sudoku_puzzle[i][j] = 4
          
      if sudoku_puzzle[i][j] == "x":
          sudoku_puzzle[i][j] = 0

#This is the array of all possible values for each blank square, which will be changed in the next function.
values_matrix = [[[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]],[[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]],[[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]],[[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]]]

#Finds the possible values for each square.
def get_possible():
  for i in range(4):
    for j in range(4):
      if sudoku_puzzle[i][j] == 0:
        for k in range(4):
          if sudoku_puzzle[k][j] in values_matrix[i][j]:
            values_matrix[i][j].remove(sudoku_puzzle[k][j])
          if sudoku_puzzle[i][k] in values_matrix[i][j]:
            values_matrix[i][j].remove(sudoku_puzzle[i][k])
            
        if i%2 == 0:
          x = 1
        else:
          x = -1
          
        if j%2 == 0:
          y = 1
        else:
          y = -1
          
        for a in range(2):
          for b in range(2):
            if sudoku_puzzle[i+(a*x)][j+(b*y)] in values_matrix[i][j]:
              values_matrix[i][j].remove(sudoku_puzzle[i+(a*x)][j+(b*y)])
              
      else:
        values_matrix[i][j] = [0]

global possible_configurations
possible_configurations = [[]]

#Enumerates each possibility for solving.
def enumerate():
  global possible_configurations
  get_possible()
  
  for value1 in range(4):
    for value2 in range(4):
      if values_matrix[value1][value2] != [0]:
        possible_configurations2 = possible_configurations.copy()
        possible_configurations = []
        
        for thingy in possible_configurations2:
          x = thingy.copy()
          
          for thingy2 in values_matrix[value1][value2]:
            x.append(thingy2)
            possible_configurations.append([])
            
            for element in x:
              possible_configurations[len(possible_configurations)-1].append(element)
            x.pop(len(x)-1)

#Adds each possibility to the original sudoku.
def add_to_sudoku(add):
  sudokupuzzle2 = copy.deepcopy(sudoku_puzzle)
  add2 = add.copy()
  
  for number1 in range(4):
    for number2 in range(4):
      if sudoku_puzzle[number1][number2] == 0:
        sudokupuzzle2[number1][number2] = add2[0]
        add2.pop(0)
        
  return sudokupuzzle2

#Check some sudoku puzzle.
def check_sudoku(puzzle):
  for row in puzzle:
    if row[0] != row[1] and row[1] != row[2] and row[2] != row[3] and row[3] != row[0] and row[0] != row[2] and row[1] != row[3]:
      asdf = 1
    else:
      return False
      
  for number in range(4):
    column = [puzzle[0][number], puzzle[1][number], puzzle[2][number], puzzle[3][number]]
    if column[0] != column[1] and column[1] != column[2] and column[2] != column[3] and column[3] != column[0] and column[0] != column[2] and column[1] != column[3]:
      asdf = 1
    else:
      return False
      
  for number in range(2):
    for number2 in range(2):
      num1 = puzzle[number*2][number2*2]
      num2 = puzzle[number*2][number2*2 + 1]
      num3 = puzzle[number*2 + 1][number2*2]
      num4 = puzzle[number*2 + 1][number2*2 + 1]
      
      if num1 != num2 and num2 != num3 and num3 != num4 and num4 != num1 and num1 != num3 and num2 != num4:
        asdf = 1
      else:
        return False
        
  return True

#Return all possible solutions.
def return_all_possible():
  answers = []
  
  for element in possible_configurations:
    if check_sudoku(add_to_sudoku(element)) == True:
      answers.append(add_to_sudoku(element))
      
  return answers

#Format the answers.
def format_answers(stuffs):
  for thing in stuffs:
    print('\nSolution:')
    for thingy in thing:
      print(str(thingy[0]) + " " + str(thingy[1]) + " " + str(thingy[2]) + " " + str(thingy[3]))
      
  if stuffs == []:
    print("No solutions")

#Runs the code.
getvalues("This is a 4x4 sudoku solver. \n\nTo input a line of the puzzle, enter x for an unfilled square and spaces between squares. \nExamples: 'x x 1 2', '1  4  2  x'\n")
enumerate()
format_answers(return_all_possible())
