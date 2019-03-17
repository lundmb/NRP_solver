import numpy as np
import math
import itertools

def hash_calc(array):
   new=array.flatten()
   length=len(new)
   value=0
   for i, x in enumerate(new):
      lt_x=sum(new[i:] < x)
      value+=lt_x*math.factorial(length-i)
   return value

def rotator(array, row, col, k=1):
   temp=array.copy()
   temp[[[row], [row+1]],[col,col+1]]=np.rot90(temp[[[row], [row+1]],[col,col+1]], k=k)
   return temp

#start=np.array([[3, 2, 5, 0],[4, 1, 6, 7]])
#solution=np.array([[4, 2, 5, 0],[3, 1, 6, 7]])
#start=np.array([[0, 1, 2],[3, 4, 5]])
#solution=np.array([[4, 2, 5],[1, 3, 0]])
start=np.array([[3, 2, 5, 0],[4, 1, 6, 7]])
solution=np.array([[4, 2, 5, 0],[3, 1, 6, 7]])
#start=np.array([[0, 1],[2,3]])
#solution=np.array([[3, 2],[1, 0]])
m,n =start.shape
print "Rows: ", n
print "Columns: ", m
records = [['']*4 for _ in range(math.factorial(n*m+1))]
solution_hash=hash_calc(solution)
current_los=[]
current_los.append([start, hash_calc(start)])
records[hash_calc(start)] = [0, start.flatten(), -1, None, None, None]
next_los=[]
unsolved=True
step =0
while unsolved:
   step+=1
   print "On step ", step
   next_los=[]
   for item in current_los:
      current_array=item[0]
      current_source=item[1]
      for index in list(itertools.product(range(n-1), range(m-1), [1, 3])):
         new_array=rotator(current_array, index[1],index[0], k=index[2])
         new_hash=hash_calc(new_array)
         if records[new_hash][0]=='':
            rot_L=None
            if index[2]==1: rot_L='CCW'
            if index[2]==3: rot_L='CW'
            records[new_hash]=[step, new_array.flatten(), current_source, index[1], index[0], rot_L]
            next_los.append([new_array, new_hash])
            if new_hash==solution_hash:
               print "solved"
               unsolved=False
               break
   current_los=next_los
   if current_los==[]:
      print "Ran out of branches: unsolvable"
      break

print "solution"
hashindex=solution_hash
solution_set=[]
while hashindex>=0:
   last_val=records[hashindex]
   solution_set.append(last_val)
   hashindex=last_val[2]
for x in solution_set[::-1]:
   print x[0], x[1], x[3], x[4], x[5]
