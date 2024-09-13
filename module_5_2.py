class House():
    def __init__(self, name, number_of_floors) -> None:
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for level in range(1, new_floor + 1):
                print(level)

    def __str__(self) -> str:
        return self.name

    def __len__(self) -> int:
        return self.number_of_floors
    


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))