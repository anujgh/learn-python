import math
class Calculator:
  def __init__(self, no):
    self.no = no

  def squar(self):
    print(f"squar: {self.no * self.no}")

  def cube(self):
    print(f"cube: {self.no * self.no * self.no}")

  def squarRoot(self):
    print(f"squar root: {math.sqrt(self.no)}")
    print(f"squar root: {self.no**1/2}")

no = Calculator(4)
no.squar()
no.cube()
no.squarRoot()