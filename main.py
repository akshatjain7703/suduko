# import only system from os 
from os import system, name 
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 



a = [[0, 0, 0, 0, 3, 0, 0, 0, 9],
     [0, 0, 0, 0, 0, 5, 0, 6, 0],
     [0, 0, 0, 0, 0, 7, 5, 0, 8],
     [0, 0, 6, 0, 0, 0, 0, 0, 0],
     [3, 2, 0, 0, 0, 0, 6, 0, 0],
     [0, 0, 0, 0, 8, 0, 0, 5, 4],
     [0, 3, 0, 0, 5, 0, 0, 0, 0],
     [8, 1, 0, 9, 4, 3, 0, 0, 0],
     [9, 0, 0, 0, 0, 8, 0, 0, 0]]


def findsq(i,j):
  if i<3:
    if j<3:
      return (0,0)
    if j<6:
      return (0,3)
    if j<9:
      return (0,6)
  elif i<6:
    if j<3:
      return (3,0)
    if j<6:
      return (3,3)
    if j<9:
      return (3,6)
  else:
    if j<3:
      return (6,0)
    if j<6:
      return (6,3)
    if j<9:
      return (6,6)


def printal(ax):
  for ii in range(0,9):
    for jj in range(0,9):
      print(ax[ii][jj], end="  ")
    print("\n")


def check(sud,i,j,x):

  sq = findsq(i,j)
  for z in range(0,9):
    if sud[i][z]==x and j!=z:
      return False

  for z in range(0,9):
    if sud[z][j]==x and i!=z:
      return False

  for y in range(sq[0], sq[0]+3):
    for z in range(sq[1], sq[1]+3):
      if sud[y][z]==x and i!=y and j!=z:
        return False

  return True


def find_zero(sud):
  for i in range(0,9):
        for j in range(0,9):
            if sud[i][j] == 0:
                return (i, j) 
  return None



def assign(sud):
  
  zero = find_zero(sud)
  if not zero:
    return True
  else:
    i,j = zero
  for x in range(1,10):
    if check(sud,i,j,x):
      sud[i][j]=x
      if assign(sud):
        return True
      sud[i][j]=0
  return False
  
   
print("START")
assign(a)
printal(a)
