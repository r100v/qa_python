from main import BooksCollector
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_twice(self): #Нельзя добавить одну и ту же книгу дважды.
        collector = BooksCollector()
        collector.add_new_book('Зеленая миля')
        collector.add_new_book('Зеленая миля')
        assert collector.get_books_rating() == {'Зеленая миля':1}
    def test_add_rating_to_a_book_that_is_not_in_the_list(self): #Нельзя выставить рейтинг книге, которой нет в списке.
        collector = BooksCollector()
        collector.add_new_book('Список Шиндлера')
        collector.set_book_rating('Побег из Шоушенка', 2)
        assert collector.books_rating == {'Список Шиндлера': 1}
    def test_cannot_set_rating_less_than_one(self): #Нельзя выставить рейтинг меньше 1.
        collector = BooksCollector()
        collector.add_new_book('Форрест Гамп')
        collector.set_book_rating('Форрест Гамп', 0)
        assert collector.books_rating == {'Форрест Гамп': 1}
    def test_cannot_set_rating_less_than_ten(self): #Нельзя выставить рейтинг больше 10.
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.set_book_rating('Властелин колец', 15)
        assert collector.books_rating == {'Властелин колец': 1}
    def test_to_check_the_book_that_has_not_been_added_there_is_no_rating(self): #У не добавленной книги нет рейтинга
        collector = BooksCollector()
        rating = collector.get_book_rating('Назад в будущее')
        assert rating is None
    def test_add_to_favorite(self): #Добавление книги в избранное.
        collector = BooksCollector()
        collector.add_new_book('Интерстеллар')
        collector.add_book_in_favorites('Интерстеллар')
        assert collector.favorites == ['Интерстеллар']
    def test_you_cannot_add_a_book_to_favorites_if_it_is_not_in_the_books_rating_dictionary(self):
        #Нельзя добавить книгу в избранное, если её нет в словаре books_rating
        collector = BooksCollector()
        collector.add_book_in_favorites('Криминальное чтиво')
        assert collector.books_rating == {}
    def test_delete_from_favorites(self):#Проверка удаления книги из избранного.
        collector = BooksCollector()
        collector.add_new_book('1+1')
        collector.add_book_in_favorites('1+1')
        collector.delete_book_from_favorites('1+1')
        assert collector.books_rating == {'1+1': 1}
#README