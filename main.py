# import only system from os 
from os import system, name 
from time import sleep
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


a = [[0, 2, 0, 6, 0, 8, 0, 0, 0],
     [5, 8, 0, 6, 0, 9, 7, 0, 0],
     [0, 0, 0, 0, 4, 0, 0, 0, 0],
     [3, 7, 0, 0, 0, 0, 5, 0, 0],
     [6, 0, 0, 0, 0, 0, 0, 0, 4],
     [0, 0, 8, 0, 0, 0, 0, 1, 3],
     [0, 0, 0, 0, 2, 0, 0, 0, 0],
     [0, 0, 9, 8, 0, 9, 0, 3, 6],
     [0, 0, 0, 3, 0, 6, 0, 9, 0]]

done= []
iii=0
jjj=0

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


def printal():
  for ii in range(0,9):
    for jj in range(0,9):
      print(a[ii][jj], end="  ")
    print("\n")


def boom(i,j):
  global a
  flag=0
  sq = findsq(i,j)
  for x in range(a[i][j]+1,10):
    for l in range(0,9):
      flag=0
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
      if x==9:
        a[i][j]=0
      continue

    a[i][j] = x
    return
    

def recheck():
  global done,iii,jjj,a
  a[iii][jjj]=0
  tpp=done.pop()
  boom(tpp[0],tpp[1])
  if a[tpp[0]][tpp[1]]!=0:
    done.append(tpp)
  
  iii=tpp[0]
  jjj=tpp[1]

  
  

iii=0
jjj=0


while iii < 9:
  jjj=0
  while jjj < 9:
    clear() 
    printal()
    if a[iii][jjj] == 0:      
      tp=(iii,jjj)
      boom(iii,jjj)

      if a[iii][jjj]!=0:
        done.append(tp)
      else:
        while a[iii][jjj]==0:
          recheck()
        iii=0
        jjj=-1
    jjj+=1
  iii+=1



         
        
        
          
        
    

