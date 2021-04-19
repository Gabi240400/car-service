from Domain.ValidateCard import CustomerCardValidator
from Domain.ValidateCar import CarValidator
from Domain.ValidateTransaction import TransactionValidator
from Repository.GenericRepository import GenericFileRepository
from Service.ServiceCard import CardService
from Service.ServiceCar import CarService
from Service.ServiceTransaction import TransactionService
from UI.Console import Console


def main():
    car_repository = GenericFileRepository("cars.pkl")
    car_validator = CarValidator()
    customer_card_repository = GenericFileRepository("cards.pkl")
    customer_card_validator = CustomerCardValidator()
    transaction_repository = GenericFileRepository("transactions.pkl")
    transaction_validator = TransactionValidator()
    car_service = CarService(car_repository,
                             car_validator,
                             transaction_repository)
    customer_card_service = CardService(customer_card_repository,
                                        customer_card_validator,
                                        transaction_repository)
    transaction_service = TransactionService(transaction_repository,
                                             transaction_validator,
                                             customer_card_repository,
                                             car_repository)

    ui = Console(car_service,
                 customer_card_service,
                 transaction_service)
    ui.run_console()


main()
