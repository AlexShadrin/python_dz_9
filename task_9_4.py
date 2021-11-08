class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('{} is going!'.format(self.name))
    def stop(self):
        print('{} is stoping!'.format(self.name))
    def turn(self, direction):
        print('{} is turning to {}!'.format(self.name, direction))
    def show_speed(self):
        print('Current speed:', self.speed)
class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Warning! Your speed is more than max!')
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        print('Current speed:', self.speed)
        if self.speed > 40:
            print('Warning! Your speed is more than max!')
class PoliceCar(Car):
    pass
town_car = TownCar(100, 'Чёрная', 'Городская машина', False)
sport_car = SportCar(274, 'Красная', 'Спортивная машина', False)
work_car = WorkCar(57, 'Зелёная', 'Рабочая машина', False)
police_car = PoliceCar(99, 'Синяя', 'Полицейская машина', True)
town_car.show_speed()
sport_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('right')