import os
import pprint
import requests
import shutil
import operator

class GoogleBooks:

    def get(self, author):
        def rate(book):
            try:
                rating = float(book['volumeInfo']['averageRating'])
            except KeyError:
                return 0.0
            else:
                if book['volumeInfo']['ratingsCount'] >= 10:
                    return rating
                else:
                    return 0.0

        url = 'https://www.googleapis.com/books/v1/volumes?q=+inauthor:' + str(author)
        data = requests.get(url).json()
        if int(data['totalItems'])==0:
            print('Такого автора не существует:')
        else:
            pass

        path_dir = os.path.join(os.getcwd(), 'tmp_pictures'+f'_{author}')
        try:
            # files = glob.glob(path_dir)
            # for f in files:
            #     os.remove(f)
            os.mkdir(path_dir)

        except OSError:
            print("Директория %s уже создана" % path_dir)
        else:
            print("Успешно создана директория %s " % path_dir)



        list_of_books = enumerate(data['items'])
        #averageRating
        #3
        book_rate = dict()
        for ind, item in list_of_books:
            book = item['volumeInfo']['title']
            try:
                pages = item['volumeInfo']['pageCount']
            except KeyError:
                pages = 0
            book_rate[book] = rate(item)
            pict_path = os.path.join(path_dir, 'book cover '+f'{book}'+'.png')
            check_image = item['volumeInfo']['readingModes']['image'] is True
            if check_image:
                picture = item['volumeInfo']['imageLinks']['thumbnail']
                r = requests.get(picture, stream=True)
                if r.status_code == 200:
                    with open(pict_path, 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
            else:
                print(f'Не существует обложки для книги {book}')
        rate_values = set(book_rate.values())
        if len(rate_values) == 1 and 0.0 in set(rate_values):
            print('Отсутствуют оценки произведений этого автора')
        else:
            sorted_by_rating = sorted(book_rate.items(), key = operator.itemgetter(1), reverse=True)
            print(f'Рекомендую к прочтению книгу {sorted_by_rating[0][0]} с рейтингом {sorted_by_rating[0][1]}')


class AuthorBook:

    def __init__(self, author, info_provider=None):
        self.author = author.lower()
        self._book = info_provider or GoogleBooks()

    def library_info(self):
        return self._book.get(self.author)


def _main():
    while True:
        name = input('Введите имя или фамилию автора:')
        if name == '':
            break
        else:
            author = AuthorBook(name)
            book = author.library_info()
            pprint.pprint(book)


if __name__ == "__main__":
    _main()