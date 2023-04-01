# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:

    def __init__(self, city_population, room_name):
        self.city_popultaion = city_population
        self.room_num = room_name

    def get_person_room(self):
        return self.room_name

    def get_city_population(self):
        return self.city_popultaion


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

person = Person('Уфа', 24)
print(person.city_popultaion, person.room_num)