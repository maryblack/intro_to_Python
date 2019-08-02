import os
import requests
import shutil
import re
from typing import Optional
from pprint import pprint


class Book:
    def __init__(self, book_info):
        self._volume_info = book_info['volumeInfo']
        self.author = self._volume_info['authors'][0] if 'authors' in self._volume_info else 'Нет автора'
        self.title = self._volume_info['title']

    def __repr__(self):
        return f'Book: "{self.title}", pages:{self.pages}'

    @property
    def pages(self) -> Optional[int]:
        if 'pageCount' in self._volume_info:
            return self._volume_info['pageCount']
        return None

    @property
    def rate(self) -> Optional[float]:
        info = self._volume_info
        if 'averageRating' in info and 'ratingsCount' in info and info['ratingsCount']>=1:
            return float(info['averageRating'])
        return None

    def save_book_cover(self):
        image_name = re.sub(r"[!=@#$?/,[.\]\\]", '', self.title)
        pict_path = os.path.join(os.getcwd(), f'book_cover_{image_name}.png')
        if 'imageLinks' in self._volume_info:
            picture = self._volume_info['imageLinks']['thumbnail']
            r = requests.get(picture, stream=True)
            if r.status_code == 200:
                with open(pict_path, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
        else:
            print(f'Не существует обложки для книги {self.title}')





class GoogleBooks:

    def get_books(self, author) -> list:
        url = 'https://www.googleapis.com/books/v1/volumes?q=+inauthor:' + str(author)
        data = requests.get(url).json()
        if int(data['totalItems'])==0:
            print('Такого автора не существует:')
            return []
        books = []
        for item in data['items']:
            books.append(Book(item))
        return books


class AuthorBook:

    def __init__(self, author, info_provider=None):
        self.author = author.lower()
        self._book = info_provider or GoogleBooks()

    def library_info(self):
        return self._book.get_books(self.author)


def _main():
    while True:
        name = input('Введите имя или фамилию автора:')
        if name == '':
            break
        else:
            author = AuthorBook(name)
            book = author.library_info()
            pprint(book)


if __name__ == "__main__":
    _main()