from Domain.Entity import Entity


class Car(Entity):
    """
    Car object
    """

    def __init__(self, id_car, model, year, km, guarantee, is_removed):
        """

        :param id_car:
        :param model:
        :param year:
        :param km:
        :param guarantee:
        :param is_removed:
        """
        super(Car, self).__init__(id_car)
        self.__model = model
        self.__year = year
        self.__km = km
        self.__guarantee = guarantee
        self.__is_removed = is_removed

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_km(self):
        return self.__km
    
    def get_guarantee(self):
        return self.__guarantee

    def get_is_removed(self):
        return self.__is_removed

    def get_text_format(self):
        return '{}, {}, {}, {}, {}, {}'.format(self.id_entity(),
                                               self.get_model(),
                                               self.get_year(),
                                               self.get_km(),
                                               self.get_guarantee(),
                                               self.get_is_removed())

    def __str__(self):
        """
        Preparing the object for display
        :return: text formatting for display
        """
        return "id_car = {}, car_model = {}, car_year = {}, car_km = {}," \
               "car_guarantee = {}, isRemoved = {}".format(self.id_entity(),
                                                           self.get_model(),
                                                           self.get_year(),
                                                           self.get_km(),
                                                           self.get_guarantee(),
                                                           self.get_is_removed())

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_entity() == other.id_entity() and self.get_model() == other.get_model() and \
               self.get_year() == other.get_year() and self.get_km() == other.get_km() and \
               self.get_guarantee() == other.get_guarantee() and self.get_is_removed() == other.get_is_removed()

    def __ne__(self, other):
        return not self == other
