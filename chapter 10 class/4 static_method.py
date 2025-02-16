class Employee:
  language = "Python"
  salary = 9000000

  def getInfo(self):
    print(f"language is {self.language} and salary is {self.salary}")

  @staticmethod # In static method self is not required to pass
  def sayHi():
    print("Hello how are you?")


ram = Employee()
ram.sayHi()