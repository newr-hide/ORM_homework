import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale
import tabulate

DSN = 'postgresql://postgres:root@localhost:5432/ORM_db_test'
engine = sqlalchemy.create_engine(DSN)

# create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# publisher = Publisher(name='Толстой')
# session.add(publisher)
# session.commit()
charm_select = input()
subqwery_id = session.query(Publisher, Book, Stock, Shop, Sale).filter(Publisher.id == charm_select).join(Book, Publisher.id == Book.id_publisher).join(Stock, Stock.id_book == Book.id).join(Shop, Shop.id == Stock.id_shop).join(Sale, Sale.id_stock == Stock.id).all()

data = [[book.title, shop.name,sale.price, sale.date_sale] for publisher, book,stock, shop, sale in subqwery_id]
headers = ["Название книги", "Название магазина", "Стоимость покупки", "Дата покупки"]
print(tabulate.tabulate(data, headers))

# headers = ["Название книги", "Стоимость покупки", "Магазин", "Дата покупки"]
# data = [row for row in subqwery_id]
# print(tabulate.tabulate(data, headers))

# for c in session.query(Publisher).all():
#     print(c)
#
# for c in session.query(Book).all():
#     print(c)
#
# for c in session.query(Publisher.name, Publisher.id).all():
#     print(c)

session.close()