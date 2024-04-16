import unittest
from swords import SwordsSecond

class TestFigure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Виконається лише раз на початку тестів
        """
        pass

    def setUp(self) -> None:
        self.testObj = SwordsSecond.create_with_random_rarity("Kiborg")

    def tearDown(self) -> None:
        del self.testObj
        return super().tearDown()
    
    def test_buff_expire(self):
        Damage = self.testObj.damage
        Vitality = self.testObj.vitality
        result = self.testObj.expire_buff()
        assert(isinstance(result, str)), "Результат має бути рядком!!!"
        self.testObj.apply_random_buff()
        result2 = self.testObj.expire_buff()
        assert(isinstance(result, str)), "Результат має бути рядком!!!"
        assert(self.testObj.damage == Damage), "Неправильний результат: Початкове значення не дорівнює кінцевому!"
        assert(self.testObj.vitality == Vitality), "Неправильний результат: Початкове значення не дорівнює кінцевому!"

if __name__ == '__main__':
    unittest.main() 