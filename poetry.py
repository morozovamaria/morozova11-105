class Author:
    def __init__(self, name, surname, nickname, country, birthday, deathday, works = None):
        self.name = name
        self.surname = surname
        self.nickname = nickname
        self.country = country
        self.birthday = birthday
        self.deathday = deathday

        if works == None:
            self.works = []
        elif isinstance(works, list):
            self.works = works
            for i in works:
                i.authors.append(self)
        else:
            self.works = [works]
            works.authors.append(self)


    def add_work(self, work):
        self.works.append(work)
        work.authors.append(self)

    def __str__(self):
        return f"{self.name} {self.surname} по псевдониму {self.nickname} из {self.country}"

class Work:
    def __init__(self, year, authors = None, publishers = None):
        self.year = year
        if authors == None:
            self.authors = []
        elif isinstance(authors, list):
            self.authors = authors
            for i in authors:
                i.works.append(self)
        else:
            self.authors = [authors]
            authors.works.append(self)

        if publishers == None:
            self.publishers = []

        elif isinstance(publishers, list):
            self.publishers = publishers
            for i in publishers:
                i.works.append(self)

        else:
            self.publishers = [publishers]
            publishers.works.append(self)

    def add_author(self, author):
        self.authors.append(author)
        author.works.append(self)

    def __str__(self):
        return f"Работа {self.year} года выпуска."

class Publisher:
    def __init__(self, name, works = None):
        self.name = name
        if works == None:
            self.works = []
        elif isinstance(works, list):
            self.works = works
            for i in works:
                i.publishers.append(self)
        else:
            self.works = [works]
            works.publishers.append(self)

    def __str__(self):
        return f"Издатель с именем {self.name}"


class Book(Work):
    def __init__(self, binding, cover, year, authors = None, publishers = None):
        super().__init__(year, authors, publishers)
        self.binding = binding
        self.cover = cover

    def __str__(self):
        return f"Книга {self.binding} переплета и {self.cover} обложки {self.year} года выпуска"

class Magazine(Work):
    def __init__(self, cover_type, year, authors = None, publishers = None):
        super().__init__(year, authors, publishers)
        self.cover_type = cover_type

    def __str__(self):
        return f"Журнал с обложкой типа {self.cover_type} {self.year} года выпуска"

class Publication(Work):
    def __init__(self, place, year, authors = None, publishers = None):
        super().__init__(year, authors, publishers)
        self.place = place

    def __str__(self):
        return f"Публикация с местом {self.place} {self.year} года выпуска"

Pushkin = Author('Александр', 'Пушкин', '', 'России', '06.06.1799', '10.02.1837')
Onegin = Book('твердого', 'бежевой', '1823', Pushkin)
print(Pushkin.works[0])
print(Onegin.authors[0])


