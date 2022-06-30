# 2. Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);
# ● значения атрибутов должны передаваться при создании экземпляра класса;
# ● атрибуты сделать защищёнными;
# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# ● проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.
class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.volume = 0.025
        self.depth = 0.05

    def asphalt_calculation(self):
        asphalt_calculation = self._length * self._width * self.volume * self.depth
        print(f'Для покрытия дорожного полотна длинной {self._length} и '
              f'шириной {self._width} неободимо {round(asphalt_calculation)} тонн асфальта')


r = Road(5000, 20)
r.asphalt_calculation()