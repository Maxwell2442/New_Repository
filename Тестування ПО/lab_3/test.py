import unittest 
from random import choice, randint 

class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.type # робимо помилку


class TestFigure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Виконається лише раз на початку тестів
        """
        pass
    
    def setUp(self) -> None:
        """Виконується кожного разу коли запускається тест
        """
        self.figure = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure, self.length)
        return super().setUp()

    def tearDown(self) -> None:
        del self.obj
        return super().tearDown()

    def test_figure_type(self):
        print(f"Тестуємо вивід, має бути: {self.figure} == {self.obj.get_figure_type}")
        self.assertEqual(self.figure, self.obj.get_figure_type, "Властивість get_figure_type повертає неправильну фігуру!")

    def test_figure_lengh(self):
        self.assertEqual(self.length, self.obj.get_figure_length, "Властивість get_figure_length повертає неправильну довжину!")
    
    def test_obj(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1) # Спробуємо створити обєкт з недозволеними параметрими, в нас має бути помилка AssertionError


if __name__ == '__main__':
    unittest.main() # unittest.main(verbosity=2) щоб був більш детальний вивід

