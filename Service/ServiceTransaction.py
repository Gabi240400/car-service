import datetime

from Domain.Transaction import Transaction
from Domain.ValidateTransaction import TransactionValidator
from Repository.GenericRepository import GenericFileRepository
from Exceptions.InvalidID import InvalidIdException


class TransactionService:
    def __init__(self,
                 transaction_repository: GenericFileRepository,
                 transaction_validator: TransactionValidator,
                 customer_card_repository: GenericFileRepository,
                 car_repository: GenericFileRepository):
        self.__transaction_repository = transaction_repository
        self.__transaction_validator = transaction_validator
        self.__customer_card_repository = customer_card_repository
        self.__car_repository = car_repository

    def get_cars_id(self):
        found_id = []
        for car in self.__car_repository.read():
            found_id.append(car.id_entity())
        return found_id

    def add_transaction(self,
                        transaction_id,
                        car_id,
                        card_id,
                        pieces_cost,
                        sum_man,
                        date,
                        hour,
                        reduced_sum):
        """

        :param transaction_id:
        :param car_id:
        :param card_id:
        :param pieces_cost:
        :param sum_man:
        :param date:
        :param hour:
        :param reduced_sum:
        :return:
        """
        if car_id not in self.get_cars_id():
            raise InvalidIdException("There is no such car with that id")
        for card in self.__customer_card_repository.read():
            if card.id_entity() == card_id:
                reduced_sum += sum_man * 10 / 100
                sum_man = sum_man * 90 / 100
                break
        for cars in self.__car_repository.read():
            if cars.id_entity() == car_id and cars.get_guarantee():
                reduced_sum += pieces_cost
                pieces_cost = 0.0

        transaction = Transaction(transaction_id, car_id, card_id, pieces_cost, sum_man, date, hour, reduced_sum)
        self.__transaction_validator.validate_transaction(transaction)
        self.__transaction_repository.create(transaction)

    def get_all_transactions(self):
        """

        :return: all the transactions from storage
        """
        found_transactions = []
        for transaction in self.__transaction_repository.read():
            found_transactions.append(transaction)
        return found_transactions

    def get_transaction(self, transaction_id):
        """

        :param transaction_id: int
        :return: the Transaction object that has the given id
        """
        return self.__transaction_repository.read_by_id(transaction_id)

    def update_transaction(self,
                           new_transaction_id,
                           new_car_transacted_id,
                           new_customer_card_transaction_id,
                           new_pieces_cost,
                           new_workmanship_cost,
                           new_date,
                           new_time,
                           reduced_sum):
        """

        :param new_transaction_id:
        :param new_car_transacted_id:
        :param new_customer_card_transaction_id:
        :param new_pieces_cost:
        :param new_workmanship_cost:
        :param new_date:
        :param new_time:
        :param reduced_sum:
        :return:
        """
        new_time = float(new_time)
        if new_car_transacted_id not in self.get_cars_id():
            raise InvalidIdException("There is no such car with that id")
        for card in self.__customer_card_repository.read():
            if card.id_entity() == new_customer_card_transaction_id:
                reduced_sum += new_workmanship_cost * 10 / 100
                new_workmanship_cost = new_workmanship_cost * 90 / 100
                break
        for cars in self.__car_repository.read():
            if cars.id_entity() == new_car_transacted_id and cars.get_guarantee():
                reduced_sum += new_pieces_cost
                new_pieces_cost = 0.0
        transaction = Transaction(new_transaction_id,
                                  new_car_transacted_id,
                                  new_customer_card_transaction_id,
                                  new_pieces_cost,
                                  new_workmanship_cost,
                                  new_date,
                                  new_time,
                                  reduced_sum)
        self.__transaction_validator.validate_transaction(transaction)
        self.__transaction_repository.update(transaction)

    def remove_transaction(self, transaction_id):
        """
        Deletes the Transaction object with the given id
        :param transaction_id: int
        """
        self.__transaction_repository.delete(transaction_id)

    def show_transaction_with_sum_in_range(self, less_sum, greater_sum):
        """

        :param less_sum:
        :param greater_sum:
        :return:
        """
        return filter(lambda transaction: less_sum < transaction.get_cost_labor() + transaction.get_cost_parts() < greater_sum,
                      self.__transaction_repository.read())

    def show_card_client_desc_ord(self):
        transactions = self.__transaction_repository.read()
        max_per_id = {}
        for transaction in transactions:
            id_card = transaction.get_id_card()
            sum_discount = transaction.get_discount()
            if id_card not in max_per_id:
                max_per_id[id_card] = 0
            max_per_id[id_card] += sum_discount
        new_max_per_id = sorted(max_per_id, key=max_per_id.__getitem__, reverse=True)
        return new_max_per_id

    @staticmethod
    def __get_date_in_format(date):
        """
        Transforms a string that represents a date into datetime format
        :param date: string
        :return: a datetime date
        """
        date_list = date.split(sep="/")
        year = int(date_list[2])
        month = int(date_list[1])
        day = int(date_list[0])
        date_in_date_format = datetime.datetime(year, month, day)
        return date_in_date_format

    def get_transactions_between_two_dates(self, date_one, date_two):
        """
        Gets all the transactions made between two given dates
        :param date_one: string
        :param date_two: string
        :return: list of Transaction objects type
        """
        list_of_transactions = []
        self.__transaction_validator.validate_date(date_one)
        self.__transaction_validator.validate_date(date_two)
        date_one_obj = self.__get_date_in_format(date_one)
        date_two_obj = self.__get_date_in_format(date_two)
        difference = date_two_obj - date_one_obj
        for transaction in self.__transaction_repository.read():
            checked_date = self.__get_date_in_format(transaction.get_date())
            zero_days = datetime.timedelta(0)
            if difference > zero_days:
                if (checked_date - date_one_obj) > zero_days and (date_two_obj - checked_date) > zero_days:
                    list_of_transactions.append(transaction.id_entity())
            elif difference < zero_days:
                if (date_one_obj - checked_date) > zero_days and (checked_date - date_two_obj) > zero_days:
                    list_of_transactions.append(transaction.id_entity())
            elif difference == zero_days:
                list_of_transactions = []
        return list_of_transactions

    def remove_transactions_between_two_dates(self, date_one, date_two):
        """
        Deletes all the transactions made between two given dates
        :param date_one: string
        :param date_two: string
        """
        self.__transaction_validator.validate_date(date_one)
        self.__transaction_validator.validate_date(date_two)
        date_one_obj = self.__get_date_in_format(date_one)
        date_two_obj = self.__get_date_in_format(date_two)
        difference = date_two_obj - date_one_obj
        list_of_transaction_to_remove = []
        for transaction in self.__transaction_repository.read():
            checked_date = self.__get_date_in_format(transaction.get_date())
            zero_days = datetime.timedelta(0)
            if difference > zero_days:
                if (checked_date - date_one_obj) > zero_days and \
                        (date_two_obj - checked_date) > zero_days:
                    list_of_transaction_to_remove.append(transaction.id_entity())
            elif difference < zero_days:
                if (date_one_obj - checked_date) > zero_days and \
                        (checked_date - date_two_obj) > zero_days:
                    list_of_transaction_to_remove.append(transaction.id_entity())
            elif difference == zero_days:
                list_of_transaction_to_remove.append(transaction.id_entity())
        for i in range(len(list_of_transaction_to_remove)):
            self.remove_transaction(list_of_transaction_to_remove[i])
