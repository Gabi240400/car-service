from Domain.Car import Car
from Exceptions.CarError import InvalidCarException


class CarValidator:
    @staticmethod
    def validate_car(car: Car):
        """
        Function verify if an object respects some conditions and if it finds an irregularity raise an exception
        :param car: an Car object
        :return: exceptions
        """
        # VALUE ERROR
        if not isinstance(car.id_entity(), int):
            raise InvalidCarException("Car id {} is not int".format(car.id_entity()))
        if not isinstance(car.get_model(), str):
            raise InvalidCarException("Car model {} is not string".format(car.get_model()))
        if not isinstance(car.get_year(), int):
            raise InvalidCarException("Car year {} is not int".format(car.get_year()))
        if not isinstance(car.get_km(), int):
            raise InvalidCarException("Car kilometer {} is not int".format(car.get_km()))
        if car.id_entity() < 0:
            raise InvalidCarException("Car id must be a positive")
        if car.get_km() <= 0:
            raise InvalidCarException("Car number of kilometer {} must be a positive "
                                      "number".format(car.get_km()))
        if car.get_year() <= 0:
            raise InvalidCarException("Car year {} must be a positive "
                                      "number".format(car.get_year()))
        if len("{}".format(car.get_model())) == 0:
            raise InvalidCarException("Car has to get a model ")
