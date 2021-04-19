from Domain.Transaction import Transaction
from Exceptions.InvalidID import InvalidIdException
from Exceptions.TransactionError import InvalidTransactionException


class TransactionValidator:
    @staticmethod
    def validate_transaction(transaction: Transaction):
        """
        Function verify if an object respects some conditions and if it finds an irregularity raise an exception
        :param transaction: an Transaction object
        :return: exceptions
        """
        if not isinstance(transaction.id_entity(), int):
            raise InvalidIdException("Transaction id = {} is not int".format(transaction.id_entity()))
        if not isinstance(transaction.get_id_car(), int):
            raise InvalidIdException("Car id = {} is not "
                                     "int".format(transaction.get_id_car()))
        if transaction.get_id_car() != '':
            if not isinstance(transaction.get_id_car(), int):
                raise InvalidIdException("Customer id = {} is not "
                                         "int".format(transaction.get_id_card()))
        if not isinstance(transaction.get_cost_parts(), float):
            raise InvalidTransactionException("Pieces cost of car = {} is not"
                                              " int".format(transaction.get_cost_parts()))
        if not isinstance(transaction.get_cost_labor(), float):
            raise InvalidTransactionException("Workmanship cost of car = {} is not"
                                              " int".format(transaction.get_cost_labor()))
        if not isinstance(transaction.get_time(), float):
            raise InvalidTransactionException("Time = {} is not float".format(transaction.get_time()))
        if "/" not in transaction.get_date():
            raise InvalidTransactionException("Please use / for writing date")
        if len("{}".format(transaction.get_date())) < 5:
            raise InvalidTransactionException("This is not a valid date")
        date = transaction.get_date().split(sep="/")
        if len(date) != 3:
            raise InvalidTransactionException("Use only 2 /")
        if int(date[0]) < 1 or int(date[0]) > 31:
            raise InvalidTransactionException("Day {} must be between 1 and 31".format(int(date[0])))
        if int(date[1]) < 1 or int(date[1]) > 12:
            raise InvalidTransactionException("Month {} must be between 1 and 12".format(int(date[1])))
        if int(date[2]) > 2019:
            raise InvalidTransactionException("Year {} cannot be in the future".format(int(date[2])))

    @staticmethod
    def validate_date(date):
        """
        Function verify if a date id valid
        :param date: string
        :return: raise exceptions if date doesn't respects some conditions
        """
        date = date.split(sep="/")
        if len(date) != 3:
            raise InvalidTransactionException("Use only 2 /")
        if int(date[0]) < 1 or int(date[0]) > 31:
            raise InvalidTransactionException("Day {} must be between 1 and 31".format(int(date[0])))
        if int(date[1]) < 1 or int(date[1]) > 12:
            raise InvalidTransactionException("Month {} must be between 1 and 12".format(int(date[1])))
        if int(date[2]) > 2019:
            raise InvalidTransactionException("Year {} cannot be in the future".format(int(date[2])))
