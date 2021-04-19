# from exception.InvalidCNPException import InvalidCNPException
# from exception.InvalidCustomerCardException import InvalidCustomerCardException
from Exceptions.InvalidID import InvalidIdException
# from exception.InvalidCarException import InvalidCarException
from Exceptions.TransactionError import InvalidTransactionException
# from Exceptions.InvalidID import InvalidIdException
from Service.ServiceCard import CardService
from Service.ServiceCar import CarService
from Service.ServiceTransaction import TransactionService


class Console:
    def __init__(self,
                 car_service: CarService,
                 customer_card_service: CardService,
                 transaction_service: TransactionService
                 ):
        self.__car_service = car_service
        self.__customer_card_service = customer_card_service
        self.__transaction_service = transaction_service

    @staticmethod
    def __show_menu():
        print('1. Add car')
        print('2. Read cars')
        print('3. Update car')
        print('4. Delete car')
        print('p. Populate cars')
        print('5. Add card')
        print('6. Read cards')
        print('7. Update card')
        print('8. Delete card')
        print('9. Add transaction')
        print('10. Read transactions')
        print('11. Update transaction')
        print('12. Delete transaction')
        print('13. Search for cars and customers by model, year of manufacture, first name, CNP etc. Full text search.')
        print('14. Displaying all transactions with the amount within a given range.')
        print('15. Display of the cars ordered in descending order by the amount obtained on the labor.')
        print('16. Display of the ordered customer cards in descending order by the value of the discounts obtained.')
        print('17. Delete all transactions within a certain day range.')
        print('18. Update of the warranty on each car: a car is under warranty if and only if it is maximum 3 years and maximum 60 000 km.')
        print('19. Waterfall removal.')
        print('x. Exit')

    def run_console(self):
        while True:
            self.__show_menu()
            option = input('The option is: ')
            if option == '1':
                self.__handleCarsAdd()
            elif option == '2':
                self.__show_list(self.__car_service.get_all())
            elif option == '3':
                self.__handleUpdateCar()
            elif option == '4':
                id_car = int(input('What car do you want to delete? '))
                try:
                    self.__car_service.delete_car(id_car)
                    print('The car was deleted! ')
                except Exception as e:
                    print(e)
            elif option == 'p':
                self.__populateCar()
            elif option == '5':
                self.__handleCardsAdd()
            elif option == '6':
                self.__show_list(self.__customer_card_service.get_all())
            elif option == '7':
                self.__handleUpdateCard()
            elif option == '8':
                id_card = int(input('What customer card do you want to delete? '))
                try:
                    self.__customer_card_service.delete_card(id_card)
                    print('The customer card was deleted! ')
                except Exception as e:
                    print(e)
            elif option == '9':
                self.__handleTransactionAdd()
            elif option == '10':
                self.__show_list(self.__transaction_service.get_all_transactions())
            elif option == '11':
                self.__handleTransactionsUpdate()
            elif option == '12':
                id_transaction = int(input('What transaction do you want to delete? '))
                try:
                    self.__transaction_service.remove_transaction(id_transaction)
                    print('Transaction deleted!')
                except Exception as e:
                    print(e)
            elif option == '13':
                while True:
                    print('1. Cars')
                    print('2. Customer')
                    print('b. Back')
                    op2 = input('Where do you want to look?')

                    if op2 == '1':
                        string = input('What do you want to look for?')
                        cars_text = self.__car_service.get_list_of_car_that_match(string)
                        self.__show_list(cars_text)
                    elif op2 == '2':
                        string = input('What do you want to look for?')
                        cards_text = self.__customer_card_service.get_list_of_customer_cards_that_match(string)
                        self.__show_list(cards_text)
                    elif op2 == 'b':
                        break
            elif option == '14':
                less_sum = int(input('Minimum sum: '))
                greater_sum = int(input('Maximum sum: '))
                list_t = self.__transaction_service.show_transaction_with_sum_in_range(less_sum, greater_sum)
                for trn in list_t:
                    print(trn)
            elif option == '15':
                all_list = self.__car_service.show_cars_based_on_sum_man()
                for car in all_list:
                    print(car[0], "Workmanship cost: ", car[1])
            elif option == '16':
                all_list = self.__customer_card_service.show_card_client_desc_ord()
                for card in all_list:
                    print(card[0], 'Discount: ', card[1])
            elif option == '17':
                self.__handle_remove_transactions_between_dates()
            elif option == '18':
                self.__car_service.modify_guarantee()
            elif option == '19':
                print('1. Cars')
                print('2. Customer Card')
                print('b. Back')
                choice = input('What do you want to delete in the waterfall?')
                if choice == '1':
                    self.delete_id_car_and_transaction()
                elif choice == '2':
                    self.delete_id_card_and_transaction()
                elif choice == 'b':
                    break
                else:
                    print('Invalid command!')
            elif option == 'x':
                break
            else:
                print('Invalid command!')

    @staticmethod
    def __show_list(objects):
        for obj in objects:
            print(obj)

    def __handleCarsAdd(self):
        try:
            idCar = int(input('The id = '))
            model = input('The model = ')
            year = int(input('The year of purchase = '))
            km = int(input('The number of kilometer = '))
            guarantee = input('In guarantee (yes or no) = ')
            self.__car_service.add_car(idCar, model, year, km, guarantee, False)
            print('Car added!')
        except Exception as ve:
            print('There are errors!', ve)

    def __handleUpdateCar(self):
        try:
            idCar = int(input('The id for update = '))
            model = input('The new model = ')
            year = int(input('The new year of purchase = '))
            km = int(input('The new number of kilometer = '))
            guarantee = input('In guarantee (yes or no) = ')
            self.__car_service.update_car(idCar, model, year, km, guarantee, False)
            print('Car updated!')
        except Exception as ve:
            print('There are errors!', ve)

    def __populateCar(self):
        try:
            x = int(input("Give number = "))
            result = self.__car_service.populate(x)
            for car in result:
                print(car)
        except ValueError as a:
            print(a)

    def __handleCardsAdd(self):
        try:
            idCard = int(input('The card ID = '))
            name = input("The customer name = ")
            surname = input('The customer surname = ')
            cnp = int(input('The customer cnp is = '))
            dateBirth = input("The date of birth = ")
            dateRegistration = input("The date of registration = ")
            self.__customer_card_service.add_customer_card(idCard,
                                                           name,
                                                           surname,
                                                           cnp,
                                                           dateBirth,
                                                           dateRegistration,
                                                           False)
            print("Card added!")
        except Exception as ve:
            print(ve)

    def __handleUpdateCard(self):
        try:
            idCard = int(input('The card ID = '))
            name = input("The new customer name = ")
            surname = input('The new customer surname = ')
            cnp = int(input('The new customer cnp is = '))
            dateBirth = input("The new date of birth = ")
            dateRegistration = input("The new date of registration = ")
            self.__customer_card_service.update_card(idCard,
                                                     name,
                                                     surname,
                                                     cnp,
                                                     dateBirth,
                                                     dateRegistration,
                                                     False)
            print("Card updated!")
        except Exception as ve:
            print(ve)

    def __handleTransactionAdd(self):
        """

        :return:
        """
        try:
            idTransaction = int(input('Transaction Id = '))
            idCar = int(input('Car ID = '))
            idCardClient = int(input('Card ID = '))
            sumPieces = float(input('Pieces cost = '))
            sumMan = float(input('Workmanship cost = '))
            date = input('Transaction date = ')
            hour = float(input('Transaction hour = '))
            reducedSum = 0

            self.__transaction_service.add_transaction(
                idTransaction,
                idCar,
                idCardClient,
                sumPieces,
                sumMan,
                date,
                hour,
                reducedSum
            )
            transaction = self.__transaction_service.get_transaction(idTransaction)
            print('The price paid is: ', transaction.get_cost_labor() + transaction.get_cost_parts())
            print('The discounts granted are: ', transaction.get_discount())
            print('Transaction added!')
        except ValueError as ve:
            print('There are errors', ve)
        except InvalidIdException as f:
            print(f)
        except InvalidTransactionException as v:
            print(v)

    def __handleTransactionsUpdate(self):
        """

        :return:
        """
        try:
            idTransaction = int(input('Transaction Id for update = '))
            idCar = int(input('Car ID = '))
            idCardClient = int(input('Card ID = '))
            sumPieces = float(input('Pieces cost = '))
            sumMan = float(input('Workmanship cost = '))
            date = input('Transaction date = ')
            hour = input('Transaction hour = ')
            reducedSum = 0.0

            self.__transaction_service.update_transaction(
                idTransaction,
                idCar,
                idCardClient,
                sumPieces,
                sumMan,
                date,
                hour,
                reducedSum
            )
            print('Transaction Updated!')
        except ValueError as ve:
            print('There are errors', ve)
        except InvalidIdException as ve:
            print(ve)

    def __handle_transactions_between_two_dates(self):
        print("Enter the data between which you want the transactions to be displayed:")
        try:
            date_one = input("First date: ")
            date_two = input("Second date: ")
            result = self.__transaction_service.get_transactions_between_two_dates(date_one, date_two)
            print(result)
            if len(result) != 0:
                for i in range(len(result)):
                    print(self.__transaction_service.get_transaction(result[i]))
            else:
                print(result)
        except InvalidTransactionException as r:
            print(r)
        except ValueError as w:
            print(w)

    def __handle_remove_transactions_between_dates(self):
        try:
            print("Enter the data between which you want the transactions to be removed:")
            date_one = input("First date: ")
            date_two = input("Second date: ")
            self.__transaction_service.remove_transactions_between_two_dates(date_one, date_two)
            result = self.__transaction_service.get_all_transactions()
            for transaction in result:
                print(transaction)
        except InvalidTransactionException as p:
            print(p)
        except ValueError as h:
            print(h)

    def delete_id_car_and_transaction(self):
        """

        :return:
        """
        idCar = int(input('Enter id from the car to be deleted: '))
        for car in self.__car_service.get_all():
            if car.id_entity() == idCar:
                useful_car = car
                try:
                    if useful_car.get_guarantee():
                        inGuarantee = 'yes'
                    else:
                        inGuarantee = 'no'
                    self.__car_service.update_car(idCar, useful_car.get_model(), useful_car.get_year(),
                                                  useful_car.get_km(),
                                                  inGuarantee, True)
                except Exception as ve:
                    print('Errors', ve)
                for tran in self.__transaction_service.get_all_transactions():
                    if tran.get_id_car() == idCar:
                        self.__transaction_service.remove_transaction(tran.id_entity())

    def delete_id_card_and_transaction(self):
        """

        :return:
        """
        idCard = int(input('Enter id from the car to be deleted: '))
        for card in self.__customer_card_service.get_all():
            if card.id_entity() == idCard:
                useful_card = card
                try:
                    self.__customer_card_service.update_card(idCard, useful_card.get_name(),
                                                            useful_card.get_surname(),
                                                            useful_card.get_cnp(),
                                                            useful_card.get_date_birth(),
                                                            useful_card.get_date_registered(),
                                                            True)
                except Exception as ve:
                    print('Errors', ve)
                for tran in self.__transaction_service.get_all_transactions():
                    if tran.get_id_card() == idCard:
                        self.__transaction_service.remove_transaction(tran.id_entity())
