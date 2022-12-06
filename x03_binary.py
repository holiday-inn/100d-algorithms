#!python3

"""
Create a function that takes an integer value from 0-255 and
converts it into a list.  Each element is equal to the power
of 2 that corresponds to that place value
"""


def toBinary(value):
  
  lis = []
  x = bin(value)
  if value >255:
    exit()
  else:
    x = x.replace("0b","")
    for i in range(len(x)):
      if x[i] == "1":
        lis.append(1)
      elif x[i] == "0":
        lis.append(0)
  lis.reverse()
  while len(lis) != 8:
    lis.append(0)
  return lis

def toDecimal(myList):
  x = 0
  b=-1
  for i in myList:
    b+=1
    if i == 1:
      x += 2**b
    else: pass
  
  return x
def problem1():
  assert toBinary(0) == [0,0,0,0,0,0,0,0]
  assert toBinary(1) == [1,0,0,0,0,0,0,0]
  assert toBinary(2) == [0,1,0,0,0,0,0,0]
  assert toBinary(5) == [1,0,1,0,0,0,0,0]
  assert toBinary(10) == [0,1,0,1,0,0,0,0]
  assert toBinary(30) == [0,1,1,1,1,0,0,0]
  assert toBinary(45) == [1,0,1,1,0,1,0,0]

def problem2():
  assert toDecimal([0,0,0,0,0,0,0,0]) == 0
  assert toDecimal([1,0,0,0,0,0,0,0]) == 1
  assert toDecimal([0,1,0,0,0,0,0,0]) == 2
  assert toDecimal([1,0,1,0,0,0,0,0]) == 5
  assert toDecimal([0,1,0,1,0,0,0,0]) == 10
  assert toDecimal([0,1,1,1,1,0,0,0]) == 30
  assert toDecimal([1,0,1,1,0,1,0,0]) == 45
  
if __name__ == "__main__":
  problem1()
  problem2()
  
