class animal:
  type=''
  def speak(self):
    print('啊啊啊')

class dog(animal):
  __name = ''
  def __init__(self, name):
    self.__name = name
    self.type = 'dog'
  def speak(self):
    print(f'汪汪汪，我是{self.__name}')

bobo = dog('波波')
bobo.speak()
  
