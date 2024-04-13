class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

#a = Figure("трапеція", 12)
#b = Figure("квадрат", 0)
c = Figure("квадрат", 123)
d = Figure("трикутник", -92)