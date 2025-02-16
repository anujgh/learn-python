class Employee:

  def __init__(self, name, language, salary):
    self.name = name
    self.language = language
    self.salary = salary
    print('Hi this is constructor function.')

  def get_info(self):
    print(f"name is {self.name} language is {self.language} salsry is {self.salary}")


obj = Employee('Ram','Javascript', 100000000)
obj.get_info()