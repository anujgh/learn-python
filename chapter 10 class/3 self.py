class Employee:
  language= 'Python'
  salary= 70000000

  def getInfo(self):
    print(f"language is {self.language} and salary is {self.salary}")

  def sayHi(self):
    print("Hello how are you?")

ram = Employee()
ram.language = "Javascrypt"
ram.getInfo()
ram.sayHi()
# Employee.getInfo(ram)