import csv
import os
from pprint import pprint

class CarBase:
    def __init__(self, brand, photo_file_name, carrying, car_type):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        self.car_type = car_type

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count, car_type):
        super().__init__(brand, photo_file_name, carrying, car_type)
        self.passenger_seats_count = int(passenger_seats_count)

    # def __repr__(self):
    #     return f'Это {self.car_type} для {self.passenger_seats_count} пассажиров'



class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl, car_type):
        super().__init__(brand, photo_file_name, carrying, car_type)
        self.body_whl = body_whl


    # def __repr__(self):
    #     return f'Это {self.car_type} с объемом кузова {self.get_body_volume()} '

    def get_body_volume(self):
        return self.body_height * self.body_width * self.body_length

    @property
    def body_width(self):
        if self.body_whl == '':
            return 0.0
        return float(self.body_whl.split('x')[0])

    @property
    def body_height(self):
        if self.body_whl == '':
            return 0.0
        return float(self.body_whl.split('x')[1])

    @property
    def body_length(self):
        if self.body_whl == '':
            return 0.0
        return float(self.body_whl.split('x')[2])





class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra, car_type):
        super().__init__(brand, photo_file_name, carrying, car_type)
        self.extra = extra

    # def __repr__(self):
    #     return f'Это {self.extra}'


def mkCar(car_info: list):
    if car_info[0] == 'car':
        car = Car(car_type=car_info[0], brand=car_info[1], passenger_seats_count=car_info[2],
                  photo_file_name=car_info[3], carrying=car_info[5])
        return car
    elif car_info[0] == 'truck':
        car = Truck(car_type=car_info[0], brand=car_info[1],
                  photo_file_name=car_info[3], carrying=car_info[5], body_whl=car_info[4])
        return car
    elif car_info[0] == 'spec_machine':
        car = SpecMachine(car_type=car_info[0], brand=car_info[1],
                  photo_file_name=car_info[3], carrying=car_info[5], extra=car_info[6])
        return car
    # else:
    #     return None

def get_car_list(csv_filename):
    car_list = []
    car_types = ['car', 'truck', 'spec_machine']
    with open(csv_filename, encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if len(row) < 7 or row[0] not in car_types:
                pass
            else:
                car_list.append(mkCar(row))

    return car_list

def main():
    csv_filename = 'coursera_week3_cars.csv'
    car_list = get_car_list(csv_filename)
    pprint(car_list)


if __name__ == '__main__':
    main()