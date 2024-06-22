import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import Publisher, Book, Shop, Stock, Sale
import tabulate

DSN = 'postgresql://postgres:root@localhost:5432/ORM_db_test'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

charm_select = input('Какого издателя ищем?: ')

if charm_select.isdigit():
    subqwery_id = session.query(Publisher, Book, Stock, Shop, Sale).filter(Publisher.id == charm_select).join(Book, Publisher.id == Book.id_publisher).join(Stock, Stock.id_book == Book.id).join(Shop, Shop.id == Stock.id_shop).join(Sale, Sale.id_stock == Stock.id).all()

    data = [[book.title, shop.name, sale.price, sale.date_sale] for publisher, book, stock, shop, sale in subqwery_id]
    headers = ["Название книги", "Название магазина", "Стоимость покупки", "Дата покупки"]
    print(tabulate.tabulate(data, headers))
else:
    subqwery_word = session.query(Publisher, Book, Stock, Shop, Sale).filter(Publisher.name == charm_select).join(Book,
    Publisher.id == Book.id_publisher).join(
    Stock, Stock.id_book == Book.id).join(Shop, Shop.id == Stock.id_shop).join(Sale,
    Sale.id_stock == Stock.id).all()

    data = [[book.title, shop.name, sale.price, sale.date_sale] for publisher, book, stock, shop, sale in subqwery_word]
    headers = ["Название книги", "Название магазина", "Стоимость покупки", "Дата покупки"]
    print(tabulate.tabulate(data, headers))

session.close()