# Создайте класс Good, который будет вычислять значения стоимости товаров.
# В качестве атрибутов пусть будут:
# name (имя товара),
# price(цена за 1 кг),
# cost (стоимость),
# weight(масса);
# в качестве методов:
# calc - вычисляющий стоимость товара.
# Реализуйте два экземпляра класса Good:
# Яблоки apple('apple', price = 100, weight = 1.5)
# Груши pear('pear', price = 120, weight = 0.8)
# Выведите их стоимость
class Good :
    def __init__ (self , name ,price,weight ):
        self.name=name
        self.price=price
        self.weight=weight
    def calc (self):
        cost = self.price * self.weight
        return cost
print("Информация о яблоке:")
apple= Good('apple', price = 100, weight = 1.5)
print("Наименование:",apple.name,'.')
print ("Цена за 1 килограмм:",apple.price,"рублей.")
print("Масса:",apple.weight,"кг.")
print ("Стоимость товара:",apple.calc(),"рублей.")
print("------------------------------------")

print("Информация о  груше:")
pear= Good('pear', price = 120, weight = 0.8)
print("Наименование:",pear.name,'.')
print ("Цена за 1 килограмм:",pear.price,"рублей.")
print("Масса:",pear.weight,"кг.")
print ("Стоимость товара:",pear.calc(),"рублей.")


