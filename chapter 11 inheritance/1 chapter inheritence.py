class Employee:
  company = 'Microsoft'
  def __init__(self):
    print('Welcome to Microsoft!')

class Asset:
  asset = 'Microsoft Surfece'

  def config(self):
    print(f'processer: i9 13 Gen')
    print(f'ram: 32 GB')
    print(f'rom: 512 GB SSD')

class Programmer(Employee, Asset):
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