# Задание 3
# Создайте класс Car, реализуйте в нем 5 атрибутов :
# цвет,
# марку,
# кузов (сидан sedan, грузовик truck),
# скорость,
# тип коробки передач;
# и 6 методов:
# start - заставляет начинать движение
# stop - останавливает машину
# turn - поворачивает машину в какую-либо сторону, и выводит сообщение:" Машина повернула налево"
# speed_up - ускоряет автомобиль
# speed_down - замедляет автомобиль
# beep - сигналит
# Создайте два экземпляра класса truck и car. Продемонстрируйте работу всех методов

class Car :
    def __init__(self,color,marka,kyzov,skorost,transmission):
        self.color=color
        self.marka=marka
        self.kyzov=kyzov
        self.skorost=skorost
        self.transmission=transmission
    def start (self):
        self.skorost=10
    def turn (self):
        print('Машина повернула налево -->')
    def speed_up(self):
        self.skorost= 30
    def beep (self):
        print("Биииип")
    def speed_down (self):
        self.skorost=10
    def stop(self):
        self.skorost=0
truck=Car("Синий","BMW","грузовик",0,"Механика ")
print("Инфорация об авто :")
print("Марка -",truck.marka)
print("Цвет -",truck.color)
print("Кузов -",truck.kyzov)
print("Начальная скорость -",truck.skorost,"km/h")
print("Тип трансмисии -",truck.transmission)
print("------------------------------")
car=Car("Черный","Mercedes","cидан",0 ,"Автомат")
print("Инфорация об авто :")
print("Марка -",car.marka)
print("Цвет -",car.color)
print("Кузов -",car.kyzov)
print("Начальная скорость -",car.skorost,"km/h")
print("Тип трансмисии -",car.transmission)

print("------------------------------")
print("Начальная скорость :")
print(truck.skorost, "km/h")
print("Машина тронулась с места :")
truck.start()
print(truck.skorost,"km/h")

truck.turn()#Машина поварачивает налево

print("Машина ускорилась :")
truck.speed_up()
print(truck.skorost,"km/h")

print("Машина сигналит :")
truck.beep()#машина сигналит какому-то ослу на дороге

print("Машина замедляется :")
truck.speed_down()
print(truck.skorost,"km/h")

print("Машина остановилась:")
truck.stop()
print(truck.skorost,"km/h")
