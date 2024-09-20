from time import sleep


class UrTube:

    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None

    def register(self, nickname, password, age: int):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users[nickname] = [password, age]
            self.log_in(nickname, password)

    def log_in(self, nickname, password):
        if nickname in self.users:
            if hash(password) == hash(self.users[nickname][0]):
                self.current_user = nickname

    def log_out(self, nickname):
        if nickname == self.current_user:
            self.current_user = None

    def add(self, *video):
        temp_list = [*video]
        for iter in range(len(temp_list)):
            self.videos[temp_list[iter][0]] = [temp_list[iter]
                                               [1], temp_list[iter][2], temp_list[iter][3]]

    def __len__(self):
        if len(self.users) <= 0:
            return False
        else:
            return len(self.users)

    def get_videos(self, phrase):
        search_result = []
        for title in self.videos:
            if title.lower().find(phrase.lower()):
                search_result.append(title)
        return search_result

    def watch_video(self, title: str):
        for name in self.videos:
            if title == name:
                if self.current_user in self.users:
                    if self.users[self.current_user][1] > 18 and self.videos[title][2] == True:
                        for sec in range(1, self.videos[title][0] + 1):
                            print(sec, end=' ', flush=True)
                            sleep(1)
                        print('Конец видео')
                    elif self.videos[title][2] == False:
                        for sec in range(1, self.videos[title][0] + 1):
                            print(sec, end=' ', flush=True)
                            sleep(1)
                        print('Конец видео')
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    print('Войдите в аккаунт, чтобы смотреть видео')


class User:

    def __init__(self, nickname, password, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __repr__(self) -> str:
        return f'User({self.nickname, self.password, self.age})'

    def __str__(self):
        return f'{self.nickname, self.password, self.age}'

    def __eq__(self, other):
        '''
        Сравнение объектов класса User по возрасту (age)
        '''
        if other is None or not isinstance(other, (User, int)):
            return False
        else:
            return self.age == other

    def __call__(self):
        return len(ur.users)


class Video:

    def __init__(self, title, duration, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        self.collection = [self.title, self.duration,
                           self.time_now, self.adult_mode]

    def __repr__(self):
        return f'{self.title}, {self.duration}, {self.time_now}, {self.adult_mode}'

    def __str__(self):
        return f'[{self.title}, {self.duration}, {self.time_now}, {self.adult_mode}]'

    def __eq__(self, other) -> bool:
        '''
        Сравнение объектов класса Video по их продолжительности (duration)
        '''
        if other is None or not isinstance(other, (Video, int)):
            return False
        else:
            return self.duration == other

    def __contains__(self, other):
        if other is None or isinstance(other, (Video, str, int)):
            return False
        else:
            self.title in UrTube.videos

    def __iter__(self):
        return self.__next__()

    def __next__(self):
        return Iterator(self.collection)

    def __len__(self):
        return len(self.collection)

    def __getitem__(self, index):
        if index < 0 or index > len(self.collection):
            return False
        elif index == 0:
            return self.title
        elif index == 1:
            return self.duration
        elif index == 2:
            return self.time_now
        elif index == 3:
            return self.adult_mode
        else:
            return None


class Iterator:

    def __init__(self, collection) -> None:
        self.index = -1
        self.collection = collection

    def __next__(self):
        if self.index + 1 >= len(self.collection):
            raise StopIteration()
        self.index += 1
        return self.collection[self.index]


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek!', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
