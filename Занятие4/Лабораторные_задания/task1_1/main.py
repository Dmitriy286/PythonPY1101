import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = r'####\s(?P<position>\d{1,2})\.\s\[(?P<book>.+?)\]\((?P<book_url>.+?)\)\sby\s(?P<author>.+?)\s\((?P<recommended>\d+\.\d+%)\s\w+\)\s*\!\[\]\((?P<cover_url>.+?)\)\n*\"(?P<description>.+?)\"'  # TODO записать ругулярное выражения для поиска книги


def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open(BOOKS_FILE, encoding="UTF-8") as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))


if __name__ == '__main__':
    task()




# (?P<position>\d{1,2})\.\s\[(?P<book>.+?)\]\((?P<book_url>https.+?)\)\sby\s(?P<author>\w+\s\w+)\s\((?P<recommended>.+?)\s!\[\]\((?P<cover_url>https.+)\)\n\n\"(?P<description>.+)\"