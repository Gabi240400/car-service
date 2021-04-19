import random
import string
from Domain.CardCustomer import Card
from Domain.ValidateCard import CustomerCardValidator
from Repository.GenericRepository import GenericFileRepository


class CardService:
    def __init__(self,
                 card_repository: GenericFileRepository,
                 card_validator: CustomerCardValidator,
                 transaction_repository: GenericFileRepository):
        self.__card_repository = card_repository
        self.__card_validator = card_validator
        self.__transaction_repository = transaction_repository

    def add_customer_card(self,
                          customer_card_id,
                          customer_name,
                          customer_first_name,
                          customer_cnp,
                          birth_date,
                          registration_date,
                          isRemoved):
        """
        Function creates a card
        :param customer_card_id: int
        :param customer_name: string
        :param customer_first_name: string
        :param customer_cnp: int
        :param birth_date: string
        :param registration_date: string
        :param isRemoved: bool
        """
        customer_card = Card(customer_card_id,
                                     customer_name,
                                     customer_first_name,
                                     customer_cnp,
                                     birth_date,
                                     registration_date,
                                     isRemoved)
        self.__card_validator.validate_date(birth_date)
        self.__card_validator.validate_date(registration_date)
        self.__card_repository.ensure_unique_cnp(customer_card)
        self.__card_validator.validate_customer_card(customer_card)
        self.__card_repository.create(customer_card)

    # READ

    def get_all(self):
        """
        The functionality for getting all the object from file
        :return: all the object from file
        """
        return self.__card_repository.read()

    # UPDATE

    def update_card(self, ID, name, surname, cnp, date_birth, date_registration, is_removed):
        """

        :param ID:
        :param name:
        :param surname:
        :param cnp:
        :param date_birth:
        :param date_registration:
        :param is_removed:
        :return:
        """
        new_card = Card(ID, name, surname, cnp, date_birth, date_registration, is_removed)
        self.__card_validator.validate_customer_card(new_card)
        self.__card_repository.update(new_card)

    # DELETE

    def delete_card(self, id_card):
        """

        :param id_card:
        :return:
        """
        self.__card_repository.delete(id_card)

    def get_list_of_customer_cards_that_match(self, string_card):
        """
        Function finds all the cards that have the given string in them
        :param string_card: string
        :return: a list of CustomerCards objects that contain the string
        """
        found_customer_cards = []
        for customer_card in self.__card_repository.read():
            if string_card in customer_card.get_text_format():
                found_customer_cards.append(customer_card)
        return found_customer_cards

    def get_all_cards(self):
        """
        Gets all cards from repository
        :return: a list of CustomerCard objects
        """
        found_cards = []
        for card in self.__card_repository.read():
            found_cards.append(card)
        return found_cards

    def search_text(self, string_cards):
        """

        :param string_cards:
        :return:
        """
        list_cards = []
        for cards in self.__card_repository.read():
            if string_cards in cards.get_text_format():
                list_cards.append(cards)

        return list_cards

    def populate(self):
        """

        :return:
        """
        letters = string.ascii_lowercase
        id_card = random.randint(1, 101)
        surname = ''.join(random.choice(letters) for i in range(10))
        name = ''.join(random.choice(letters) for i in range(10))
        cnp = random.randint(1000000000000, 7000000000000)
        day1 = random.randint(0, 31)
        month1 = random.randint(0, 12)
        year1 = random.randint(1950, 2000)
        date_birth = "{}.{}.{}".format(day1, month1, year1)
        day2 = random.randint(0, 31)
        month2 = random.randint(0, 12)
        year2 = random.randint(1950, 2000)
        date_registered = "{}.{}.{}".format(day2, month2, year2)
        self.add_customer_card(id_card, name, surname, cnp, date_birth, date_registered, False)

    def clear(self):
        self.__card_repository.clear()

    def show_card_client_desc_ord(self):
        list_of_customer_cards = self.__card_repository.read()
        max_per_id = {}
        for transaction in self.__transaction_repository.read():
            card_id_in_transaction = transaction.get_id_card()
            discount_for_card = transaction.get_discount()
            if card_id_in_transaction not in max_per_id:
                max_per_id[card_id_in_transaction] = 0
            max_per_id[card_id_in_transaction] += discount_for_card
        list_of_filtered_cards = []
        for card_d in list_of_customer_cards:
            if card_d.id_entity() in max_per_id:
                list_of_filtered_cards.append(card_d)
        return sorted(list_of_filtered_cards, key=lambda card: max_per_id[card.id_entity()], reverse=True)
