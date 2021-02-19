from abc import ABC, abstractmethod

class Person(ABC):

    # def __init__(self, first_name, last_name, presonal_id, age):
        # self.personal_data = (first_name, last_name, presonal_id, age)

    @property
    def personal_data(self):
        return self._personal_data

    @personal_data.setter
    @abstractmethod
    def personal_data(self, val):
        pass