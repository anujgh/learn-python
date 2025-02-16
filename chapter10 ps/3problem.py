class Demo:
  a = 4

obj = Demo()
print(obj.a) # it's showing only class attribute.
obj.a = 7 # it not change variable of class Demo. it just create a instate variable.
print(obj.a)    
print(Demo.a)