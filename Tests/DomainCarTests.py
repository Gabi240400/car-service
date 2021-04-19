from Domain.Car import Car


def test_getter():
    car = Car(1, 'logan', 2010, 373772, True, True)
    assert car.get_model() == 'logan'
    assert car.get_year() == 2010
    assert car.get_km() == 373772
    assert car.get_guarantee() == True
    assert car.get_is_removed() == True


def test_eq():
    car1 = Car(1, 'logan', 2010, 373772, True, True)
    car2 = Car(1, 'logan', 2010, 373772, True, True)
    assert car1 == car2


def main():
    test_getter()
    test_eq()


main()
