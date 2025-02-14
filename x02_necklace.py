#!python3

""" 
Necklace numbers are a number sequence.  You start with 2 digits. The 3rd digit is created by adding the previous 2 digits, but if it's greater than 10, you add the sum of those 2 digits again.  You keep repeating this process until you get back to the 2 digits you started with

extra: What is the shortest necklace number sequence that can be made?
"""

def necklace(a,b):
  stir = f"{a}{b}"
  x = a
  y = b
  con = True
  while(x!=a or y!=b) or con == True:
    con = False
    if y+x >=10:   
      x = ((x+y)%10)+1
      y = int(stir[-1])
      stir += str(x)
    else:
      x = x+y
      y = int(stir[-1])
      stir += str(x)
  stir += str(b)
  return stir

def main():
  assert necklace(9,4) == "94483257314595516742685494"
  assert necklace(1,3) == "13472922461786527977538213"
  assert necklace(5,1) == "51674268549448325731459551"
  assert necklace(3,4) == "34729224617865279775382134"

if __name__ == "__main__":
  main()