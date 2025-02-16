class Programmer:
  company= 'Microsoft'
  def __init__(self, name, language, salary):
    self.name = name
    self.language = language
    self.salary = salary

  def getInfo(self):
    print(f"name = {self.name}")
    print(f"language = {self.language}")
    print(f"salary = {self.salary}")
    print(f'Company =  {self.company}')

user = Programmer('Ram', 'Python',1000000000)
user2 = Programmer('Shyam', 'Javascrypt', 200000000)

user.getInfo()
user2.getInfo()