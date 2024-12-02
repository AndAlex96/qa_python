from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_single_book_one_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        assert len(collector.get_books_genre()) == 1
        assert 'Гордость и предубеждение' in collector.get_books_genre()

    def test_add_new_book_add_two_books_two_books_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('1984')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_invalid_name_book_has_not_been_added(self):
        collector = BooksCollector()
        collector.add_new_book('')  # Пустое имя
        collector.add_new_book('К' * 41)  # Слишком длинное имя
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_setting_valid_genre_genre_is_set(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Детективы')
        assert collector.get_book_genre('Гордость и предубеждение') == 'Детективы'

    def test_set_book_genre_setting_invalid_genre_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Неизвестный жанр')
        assert collector.get_book_genre('1984') == ''

    def test_get_books_with_specific_genre_valid_genre_genre_get(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Убийство в Восточном экспрессе')
        collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
        books = collector.get_books_with_specific_genre('Фантастика')
        assert len(books) == 1
        assert 'Гарри Поттер' in books

    def test_get_books_for_children_add_books_in_genre_and_genre_age_rating_show_only_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        books = collector.get_books_for_children()
        assert len(books) == 1
        assert 'Гарри Поттер' in books

    def test_add_book_in_favorites_valid_genre_book_add_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        assert len(collector.get_list_of_favorites_books()) == 1
        assert '1984' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_added_book_book_is_del(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_add_book_in_favorites_get_list(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        assert collector.get_list_of_favorites_books() == ['1984']

    def test_get_book_genre_set_genre_book_genre_received(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Детективы')
        assert collector.get_book_genre('Гордость и предубеждение') == 'Детективы'

    def test_get_books_genre_set_books_genre_books_genre_received(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('1984')
        collector.set_book_genre('Гордость и предубеждение', 'Детективы')
        collector.set_book_genre('1984', 'Фантастика')
        assert len(collector.get_books_genre()) == 2
        assert 'Гордость и предубеждение' in collector.get_books_genre()
        assert '1984' in collector.get_books_genre()
