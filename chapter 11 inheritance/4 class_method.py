class Demo:
  a = 10

  @classmethod
  def show(cls):
    print(f"this is the class attribute {cls.a}")

obj = Demo()
obj.a = 7

obj.show()