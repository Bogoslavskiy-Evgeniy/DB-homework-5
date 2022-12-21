import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale
db_name = 'books'
password = '*****'
host = 'localhost:5432'
DSN = f'postgresql://postgres:{password}@{host}/{db_name}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

p_1 = Publisher(name="Reilly")
p_2 = Publisher(name="Pearson")
p_3 = Publisher(name="Microsoft Press")
p_4 = Publisher(name="No starch press")

session.add_all([p_1, p_2, p_3, p_4])
session.commit()

b_1 = Book(title="Programming Python, 4th Edition", id_publisher="1")
b_2 = Book(title="Learning Python, 4th Edition", id_publisher="1")
b_3 = Book(title="Natural Language Processing with Python", id_publisher="1")
b_4 = Book(title="Hacking: The Art of Exploitation", id_publisher="4")
b_5 = Book(title="Modern Operating Systems", id_publisher="2")
b_6 = Book(title="Code Complete: Second Edition", id_publisher="3")

session.add_all([b_1, b_2, b_3, b_4, b_5, b_6])
session.commit()

sh_1 = Shop(name="Labirint")
sh_2 = Shop(name="OZON")
sh_3 = Shop(name="Amazon")

session.add_all([sh_1, sh_2, sh_3])
session.commit()

st_1 = Stock(id_book=1, id_shop=1, count=34)
st_2 = Stock(id_book=2, id_shop=1, count=30)
st_3 = Stock(id_book=3, id_shop=1, count=0)
st_4 = Stock(id_book=5, id_shop=2, count=40)
st_5 = Stock(id_book=6, id_shop=2, count=50)
st_6 = Stock(id_book=4, id_shop=3, count=10)
st_7 = Stock(id_book=6, id_shop=3, count=10)
st_8 = Stock(id_book=1, id_shop=2, count=10)
st_9 = Stock(id_book=1, id_shop=3, count=10)

session.add_all([st_1, st_2, st_3, st_4, st_5, st_6, st_7, st_8, st_9])
session.commit()

s_1 = Sale(price=50.05, date_sale="2018-10-25T09:45:24.552Z", id_stock=1, count=16)
s_2 = Sale(price=50.05, date_sale="2018-10-25T09:51:04.113Z", id_stock=3, count=10)
s_3 = Sale(price=10.50, date_sale="2018-10-25T09:52:22.194Z", id_stock=6, count=9)
s_4 = Sale(price=16.00, date_sale="2018-10-25T10:59:56.230Z", id_stock=5, count=5)
s_5 = Sale(price=16.00, date_sale="2018-10-25T10:59:56.230Z", id_stock=9, count=5)
s_6 = Sale(price=50.05, date_sale="2018-10-25T10:59:56.230Z", id_stock=4, count=1)

session.add_all([s_1, s_2, s_3, s_4, s_5, s_6])
session.commit()

author = input("Введите название автора: ")

if author != '':
    q = session.query(
        Book.title,
        Shop.name,
        Sale.price,
        Sale.date_sale
        ).select_from(Publisher).join(Book).join(Stock).join(Shop).join(Sale).\
        filter(Publisher.name == author).all()
    for result in q:
        print(result)
else:
    author_id = input("Введите идентификатор автора: ")

    w = session.query(
        Book.title,
        Shop.name,
        Sale.price,
        Sale.date_sale
        ).select_from(Publisher).join(Book).join(Stock).join(Shop).join(Sale).\
        filter(Publisher.id_publisher == author_id).all()
    for res in w:
        print(res)

session.close