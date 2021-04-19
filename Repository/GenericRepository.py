import pickle

from Exceptions.InvalidID import InvalidIdException


class GenericFileRepository:

    def __init__(self, filename):
        self.__storage = {}
        self.__filename = filename

    def __load_from_file(self):
        try:
            with open(self.__filename, 'rb') as f_read:
                self.__storage = pickle.load(f_read)
        except FileNotFoundError:
            self.__storage.clear()

    def __save_to_file(self):

        with open(self.__filename, 'wb') as f_write:
            pickle.dump(self.__storage, f_write)

    def create(self, entity):
        """
        Adds a new entity.
        :param entity: the given entity
        :return: -
        :raises: InvalidIdException if the id already exists
        """
        self.__load_from_file()
        id_entity = entity.id_entity()
        if id_entity in self.__storage:
            raise InvalidIdException('The entity id already exists!')
        self.__storage[id_entity] = entity
        self.__save_to_file()

    def read(self, id_entity=None):
        """
        Gets a car by id or all the cars
        :param id_entity: optional, the entity id
        :return: the list of entities or the entity with the given id
        """
        self.__load_from_file()
        if id_entity is None:
            return self.__storage.values()

        if id_entity in self.__storage:
            return self.__storage[id_entity]
        return None

    def update(self, entity):
        """
        Updates an entity.
        :param entity: the entity to update
        :return: -
        :raises: InvalidIdException if the id does not exist
        """
        self.__load_from_file()
        id_entity = entity.id_entity()
        if id_entity not in self.__storage:
            raise InvalidIdException('There is no entity with that id!')
        self.__storage[id_entity] = entity
        self.__save_to_file()

    def delete(self, id_entity):
        """
        Deletes a entity.
        :param id_entity: the entity id to delete.
        :return: -
        :raises InvalidIdException: if no entity with id_entity
        """
        self.__load_from_file()
        if id_entity not in self.__storage:
            raise InvalidIdException('There is no entity with that id!')
        del self.__storage[id_entity]
        self.__save_to_file()

    # MORE OPERATIONS
    def clear(self):
        self.__load_from_file()
        self.__storage.clear()
        self.__save_to_file()

    def ensure_unique_cnp(self,
                          customer_card):
        for card_key in self.__storage:
            if self.__storage[card_key].get_customer_cnp() == customer_card.get_customer_cnp():
                raise InvalidIdException("CNP already exist!")

    def read_by_id(self, id_entity):
        """
        Function returns the object with the given id
        :param id_entity: int
        :return: object which has the given id
        """
        self.__load_from_file()
        if id_entity in self.__storage:
            return self.__storage[id_entity]
        return None
