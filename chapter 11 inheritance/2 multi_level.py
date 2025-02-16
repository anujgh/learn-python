class Employee:
  company = 'Microsoft'
  def __init__(self):
    print('Welcome to Microsoft!')

class Asset(Employee):
  asset = 'Microsoft Surfece'
  def __init__(self):
    super().__init__()

  def config(self):
    print(f'processer: i9 13 Gen')
    print(f'ram: 32 GB')
    print(f'rom: 512 GB SSD')

class Programmer(Asset):
  def __init__(this,uname):
    super().__init__()
    this.name = uname

  def info(self):
    print(f'Name: {self.name}')
    print(f'Company: {self.company}')
    print(f'Laptop: {self.asset}')


puser = Programmer('Ram')
puser.info()
puser.config()