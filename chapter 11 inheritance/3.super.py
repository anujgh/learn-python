class Employee:
  company = 'Microsoft'
  def __init__(self):
    print('Cunstrocter fucntion of Employee')
    

class Asset(Employee):
  def __init__(self):
    super().__init__()
    print('Cunstroctor function of Asset')


class Programmer(Asset):
  def __init__(this,uname):
    super().__init__()
    print('Cunstroctor function in Programmer')

puser = Programmer('Ram')