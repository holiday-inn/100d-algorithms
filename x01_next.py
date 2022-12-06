#!python3

"""
There are 2 important pieces of data that are going to be used for this assignment:
curValue : (an integer)
data: a List that specifies whether the item should be skipped or not
False indicates it should be skipped, True indicates it should not be skipped.

Create a funtion that receives 2 input paramters, the curValue and the list Data
Return the index of the next item to be used
"""




def next(x , data):
  lis = []
  b = 0
  top = None
  for i in data:

    if i == False:
      b+=1
      pass
    elif i == True:
      lis.append(b)
      b+=1
  for i in lis:
    if max(lis) <= x:
      top = lis[0]
      break
    elif i > x:
      top = i
      break
    else:
      top = None

  return top
  

  

def main():
  data = [False, True, True, False, True, False]
  assert next( 3 , data ) == 4
  assert next( 4 , data ) == 1
  assert next( 1 , data ) == 2
  data = [True, True, False, False, True, False, True]
  assert next( 1 , data ) == 4
  assert next( 6 , data ) == 0
  assert next( 0 , data ) == 1
  assert next( 3 , data ) == 4
  data = [True, True, False]
  assert next( 1 , data ) == 0
  assert next( 0 , data ) == 1
  data = [False, False, False]
  assert next( 1, data ) == None
  
  
  
  
  
  
  

if __name__ == "__main__":
  main()
  

