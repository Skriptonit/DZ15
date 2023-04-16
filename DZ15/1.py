#Задание 1
#Создайте класс cat и добавьте 3 атрибута (имя, окрас, возраст) и 3 метода класса (мяукнуть,
#мурлыкать и еще один на ваше усмотрение).
#Создайте 1 экземпляр класса и продемонстрируйте его атрибуты и методы.
class Cat:
 def __init__(self, name, color, age):
  self.name = name
  self.age = age
  self.color = color
 def mayknyt (self):
  print ('Мяу!')
 def myr(self):
  print ('Муррр!')
 def mur (self ):
  print('Мрррр!')

print('Характеристики моего кота :')
Dog = Cat('Аякс ','Черно-серый ', '3 года ')
print('---------------------------')
print('1)',Dog.name)
print('2)',Dog.color)
print('3)',Dog.age)
print('---------------------------')
print('Мяукнуть Аякс:')
Dog.mayknyt()
print('Аякс,мурлыкай :')
Dog.myr()
print('Хороший мальчик Аякс :')
Dog.mur()