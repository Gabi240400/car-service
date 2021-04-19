from Domain.Entity import Entity


class Card(Entity):
    """
    Card object
    """
    def __init__(self, id_card, name, surname, cnp, date_birth, date_registered, is_removed):
        """

        :param id_card:
        :param name:
        :param surname:
        :param cnp:
        :param date_birth:
        :param date_registered:
        :param is_removed:
        """
        super(Card, self).__init__(id_card)
        self.__name = name
        self.__surname = surname
        self.__cnp = cnp
        self.__date_birth = date_birth
        self.__date_registered = date_registered
        self.__is_removed = is_removed

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_cnp(self):
        return self.__cnp

    def get_date_birth(self):
        return self.__date_birth

    def get_date_registered(self):
        return self.__date_registered

    def get_is_removed(self):
        return self.__is_removed

    def get_text_format(self):
        return '{}, {}, {}, {}, {}, {}, {}'.format(self.id_entity(),
                                                   self.get_name(),
                                                   self.get_surname(),
                                                   self.get_cnp(),
                                                   self.get_date_birth(),
                                                   self.get_date_registered(),
                                                   self.get_is_removed())

    def __str__(self):
        """
        Preparing the object for display
        :return: text formatting for display
        """
        return "id_customer_card = {}, customer_name = {}, customer_first_name = {}, customer_cnp = {}," \
               " birth_date = {}, registration_date = {}, isRemoved= {}".format(self.id_entity(),
                                                                                self.get_name(),
                                                                                self.get_surname(),
                                                                                self.get_cnp(),
                                                                                self.get_date_birth(),
                                                                                self.get_date_registered(),
                                                                                self.get_is_removed())

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_entity() == other.id_entity() and self.get_name() == other.get_name() and \
               self.get_surname() == other.get_surname() and self.get_cnp() == other.get_cnp() and \
               self.get_date_birth() == other.get_date_birth() and \
               self.get_date_registered() == other.get_date_registered() and \
               self.get_is_removed() == other.get_is_removed()

    def __ne__(self, other):
        return not self == other
