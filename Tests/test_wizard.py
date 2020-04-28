from typing import Tuple, Set, Generator

import pytest
from wizard import WizardDictionary, Wizard, Apprentice, Magic


def test_contains():
    merlin = Wizard("Merlin")
    arthur = Apprentice("Arthur")
    wizards = WizardDictionary({merlin: arthur})
    assert merlin in wizards


def test_negative_contains():
    sherlock = Wizard("Sherlock")
    merlin = Wizard("Merlin")
    arthur = Apprentice("Arthur")
    wizards = WizardDictionary({merlin: arthur})
    assert sherlock not in wizards


def test_get_keys():
    merlin = Wizard("Merlin")
    arthur = Apprentice("Arthur")
    wizards = WizardDictionary({merlin: arthur})
    assert list(wizards.get_keys()) == [merlin]


def test_get_value():
    merlin = Wizard("Merlin")
    arthur = Apprentice("Arthur")
    wizards = WizardDictionary({merlin: arthur})
    assert wizards.get_value(merlin) == arthur


def test_non_existing_wizard():
    wizard = Wizard("Magicni")
    wizdict = WizardDictionary()
    with pytest.raises(KeyError):
        wizdict[wizard]


def test_empty():
    wizard_dict = WizardDictionary()
    assert len(wizard_dict) == 0


def test_one():
    merlin = Wizard("Merlin")
    arthur = Apprentice("Arthur")
    wizard_dict = WizardDictionary()
    wizard_dict._wizdic = {merlin: arthur}
    assert len(wizard_dict) == 1


def test_iter():
    merlin = Wizard("Merlin")
    arthur = Apprentice("Arthur")
    sherlock = Wizard("Sherlock")
    watson = Apprentice("Vatson")
    wizard_dict = WizardDictionary({merlin: arthur, sherlock: watson})
    i = iter(wizard_dict)
    assert next(i) == merlin
    assert next(i) == sherlock
    with pytest.raises(StopIteration):
        next(i)


def test_set_item():
    wizard_dict = WizardDictionary()
    artur = Apprentice("Arthur", {Magic.gomancery, Magic.pyromancery})
    merlin = Wizard("Merlin", {Magic.illusionism, Magic.mentalism, Magic.gomancery})
    wizard_dict[merlin] = artur
    assert wizard_dict[merlin] == artur


def test_set_wrong_value_type():
    wizard_dict = WizardDictionary()
    merlin = Wizard("Merlin", {Magic.illusionism, Magic.mentalism, Magic.gomancery})
    with pytest.raises(TypeError):
        wizard_dict[merlin] = "Artur"


def invalid_skill_combination() -> Generator[Tuple[Set, Set]]:
    for wizard_skill in Magic:
        for apprentice_skill in Magic:
            if wizard_skill != apprentice_skill:
                yield ({wizard_skill}, {apprentice_skill})


@pytest.mark.parametrize("wizard_skills, apprentice_skills", invalid_skill_combination())
def test_wizard_unsuitable(wizard_skills, apprentice_skills):
    wizard_dict = WizardDictionary()
    arthur = Apprentice("Arthur", apprentice_skills)
    merlin = Wizard("Merlin", wizard_skills)
    with pytest.raises(ValueError):
        wizard_dict[merlin] = arthur


def test_apprentice_has_mentor():
    wizard_dict = WizardDictionary()
    arthur = Apprentice("Arthur", {Magic.gomancery, Magic.pyromancery})
    merlin = Wizard("Merlin", {Magic.illusionism, Magic.mentalism, Magic.gomancery})
    gandalph = Wizard("Gandalph", {Magic.illusionism, Magic.mentalism, Magic.psychomentrism})
    wizard_dict[merlin] = arthur
    with pytest.raises(ValueError):
        wizard_dict[gandalph] = arthur
