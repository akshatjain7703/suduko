
a = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]



def findsq(i,j):
  if i<3:
    if j<3:
      return (0,0)
    if j<6:
      return (3,0)
    if j<9:
      return (6,0)
  elif i<6:
    if j<3:
      return (0,3)
    if j<6:
      return (3,3)
    if j<9:
      return (6,3)
  else:
    if j<3:
      return (0,6)
    if j<6:
      return (3,6)
    if j<9:
      return (6,6)


def boom(i,j):
  flag=0
  sq = findsq(i,j)
  for x in range(1,10):
    for l in range(0,9):
      if x == a[i][l]:
        flag=1
        break
   
    for m in range(0,9):
      if x== a[m][j]:
        flag=1
        break

      
    for u in range(sq[0],sq[0]+3):
      for v in range(sq[1], sq[1]+3):
        if x == a[u][v]:
         flag=1
         break

    if flag==1:
      flag=0
      continue

    a[i][j] = x
    return






for i in range(0,9):
  for j in range(0,9):
    if a[i][j] == 0:
      boom(i,j)


for i in range(0,9):
  for j in range(0,9):
    print(a[i][j], end="  ")
  print("\n")
