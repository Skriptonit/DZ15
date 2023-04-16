# Задание 5
# Создайте класс светофор (trafficlight).
# Реализуйте в нем метод, который будет переключать цвета (red, green, yellow) по определенному времени:
# red = 1 сек, green 2 сек, yellow = 0.5 сек.
# Подсказка:
# Воспользуйтесь модулем time. В нем есть функция sleep

class trafficlight:
    def __init__ (self,red,green,yellow):
        self.red=red
        self.green=green
        self.yellow=yellow
metod = trafficlight("RED","GREEN","YELLOW")
from time import sleep
print('На сфетофоре загарается красный цвет :')
sleep(1)
print(metod.red)
print ("На сфетофоре загарается желтый цвет :")
sleep(0.5)
print(metod.yellow)
print ("На сфетофоре загарается зеленый цвет :")
sleep(2)
print(metod.green)
