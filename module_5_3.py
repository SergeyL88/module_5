class House():
    def __init__(self, name, number_of_floors: int) -> None:
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for level in range(1, new_floor + 1):
                print(level)

    def __str__(self) -> str:
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self) -> int:
        return self.number_of_floors
    
    def __eq__(self, other) -> bool:
        return self.number_of_floors == other
     
    def __lt__(self, other: object) -> bool:
        return self.number_of_floors < other.number_of_floors
    
    def __le__(self, other: object) -> bool:
        return self.number_of_floors <= other.number_of_floors
        
    def __gt__(self, other: object) -> bool:
        return self.number_of_floors > other.number_of_floors
        
    def __ge__(self, other: object) -> bool:
        return self.number_of_floors >= other.number_of_floors
        
    def __ne__(self, other: object) -> bool:
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value) -> int:
        self.number_of_floors += value
        return self
    
    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        return self.__add__(other)
        


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__