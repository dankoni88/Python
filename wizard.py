from enum import Enum
from typing import Set


class Magic(Enum):
    illusionism = 1
    mentalism = 2
    psychomentrism = 3
    pyromancery = 4
    gomancery = 5


class Wizard:
    def __init__(self, name: str, magic: Set = None):
        self.name = name
        self._knows_magic = magic

    @property
    def magic(self) -> Set:
        return self._knows_magic


class Apprentice:
    def __init__(self, name: str, magic: Set = None, mentor: Wizard = None):
        self.name = name
        self._magic_to_learn: Set = magic
        self._mentor = mentor

    @property
    def wanted_magic(self) -> Set:
        return self._magic_to_learn
#changed
    @property
    def mentor(self) -> Wizard:
        return self._mentor

    @mentor.setter
    def mentor(self, new_mentor: Wizard):
        self._mentor = new_mentor


class WizardDictionary:
    def __init__(self, starting_state=None):
        if starting_state is None:
            self._wizdic = {}
        else:
            self._wizdic = starting_state

    def __getitem__(self, wizard):
        return self._wizdic[wizard]

    def __setitem__(self, wizard, apprentice):
        if type(apprentice) != Apprentice:
            raise TypeError("You have entered the wrong type for apprentice. Please, try again.")

        if apprentice.mentor is not None:
            raise ValueError("Apprentice already has a mentor")

        if not wizard.magic & apprentice.wanted_magic:
            raise ValueError("Wizard does not know magic apprentice wants to learn")

        self._wizdic[wizard] = apprentice

    def __contains__(self, item):
        return item in self._wizdic

    def __len__(self):
        return len(self._wizdic)

    def __iter__(self):
        return iter(self._wizdic)

    def get_value(self, key):
        return self._wizdic[key]

    def get_keys(self):
        return self._wizdic.keys()
