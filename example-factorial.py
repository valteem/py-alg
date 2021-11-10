import pdb
from algpy.recursion.factorial.factorial import factorial

def example_factorial():
    print("factorial (5) = " + str(factorial(5)))

#pdb.set_trace()

if __name__ == "__main__":
  example_factorial()
  print(str(factorial(7)))