from Domain.Entity import Entity


class Transaction(Entity):
    """
    Transaction object
    """
    def __init__(self, id_transaction, id_car, id_card, cost_parts, cost_labor, date, time, discount):
        """

        :param id_transaction:
        :param id_car:
        :param id_card:
        :param cost_parts:
        :param cost_labor:
        :param date:
        :param time:
        :param discount:
        """
        super(Transaction, self).__init__(id_transaction)
        self.__id_car = id_car
        self.__id_card = id_card
        self.__cost_parts = cost_parts
        self.__cost_labor = cost_labor
        self.__date = date
        self.__time = time
        self.__discount = discount

    def get_id_car(self):
        return self.__id_car

    def get_id_card(self):
        return self.__id_card

    def get_cost_parts(self):
        return self.__cost_parts

    def get_cost_labor(self):
        return self.__cost_labor

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def get_discount(self):
        return self.__discount

    def get_text_format(self):
        return '{}, {}, {}, {}, {}, {}, {}, {}'.format(self.id_entity(),
                                                       self.get_id_car(),
                                                       self.get_id_card(),
                                                       self.get_cost_parts(),
                                                       self.get_cost_labor(),
                                                       self.get_date(),
                                                       self.get_time(),
                                                       self.get_discount())

    def __str__(self):
        """
        Preparing the object for display
        :return: text formatting for display
        """
        return "transactionID = {}, carID = {}, cardID = {}, piecesCost = {}" \
               ", workmanshipCost = {}, date = {}, hour = {}, discount = {}".format(self.id_entity(),
                                                                                    self.get_id_car(),
                                                                                    self.get_id_card(),
                                                                                    self.get_cost_parts(),
                                                                                    self.get_cost_labor(),
                                                                                    self.get_date(),
                                                                                    self.get_time(),
                                                                                    self.get_discount())

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_entity() == other.id_entity() and self.get_id_car() == other.get_id_car() and \
               self.get_id_card() == other.get_id_card() and self.get_cost_parts() == other.get_cost_parts() and \
               self.get_cost_labor() == other.get_cost_labor() and self.get_date() == other.get_date() and \
               self.get_time() == other.get_time()

    def __ne__(self, other):
        return not self == other
