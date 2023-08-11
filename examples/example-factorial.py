import pdb
# Running from top level package directory:
# $ python3 -m examples.example-factorial
# 'It is an antipattern running a script directly from its folder' https://stackoverflow.com/a/68315950
#from algpy.recursion.factorial.factorial import factorial
from algpy import factorial

def example_factorial():
    print("factorial (5) = " + str(factorial(5)))

#pdb.set_trace()

if __name__ == "__main__":
  example_factorial()
  print(str(factorial(7)))
