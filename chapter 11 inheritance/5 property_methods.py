class Employee:
  
  @property
  def name(self):
    return self.ename
  

  @name.setter
  def name(self, value):
    name_arr = value.split(' ')
    self.f_name = name_arr[0]
    self.l_name = name_arr[1]


user = Employee()
user.name = 'Ram Singh'
print(user.f_name, user.l_name)