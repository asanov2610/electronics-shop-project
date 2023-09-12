from src.item import Item
from src.item import InstantiateCSVError
import pytest
import csv
"""Здесь надо написать тесты с использованием pytest для модуля item."""

def test_item():
    # Tests homework_1
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000

    assert item2.calculate_total_price() == 100000

    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000

    item2.apply_discount()
    assert item2.price == 16000.0

    # Tests homework_2

    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    assert len(Item.all) == 3
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    #Tests homework_3
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'

    item1 = Item("Планшет", 7000, 5)
    assert repr(item1) == "Item('Планшет', 7000, 5)"
    assert str(item1) == 'Планшет'


    #Tests homework_4
    assert item1 + 5 == None


    #Tests homework_6
# def test_instantiate_from_csv():
#     with pytest.raises(FileNotFoundError):
#         open("item.csv")
#     with pytest.raises(InstantiateCSVError):
#         with open('../src/items.csv') as csvfile:
#             reader = csv.DictReader(csvfile)
#             if not "quantity" in reader.fieldnames:
#                 raise InstantiateCSVError


def test_instantiate_from_csv():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('../src/item.csv')








