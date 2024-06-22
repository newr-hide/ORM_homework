import sqlalchemy as alh
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    id = alh.Column(alh.Integer, primary_key=True)
    name = alh.Column(alh.String(length=40), unique=True)

    def __str__(self):
        return f'{self.id}: {self.name}'

class Book(Base):
    __tablename__ = "book"

    id = alh.Column(alh.Integer, primary_key=True)
    title = alh.Column(alh.Text, nullable=False)
    id_publisher = alh.Column(alh.Integer, alh.ForeignKey("publisher.id"), nullable=False)
    publisher = relationship(Publisher, backref="book")

    def __str__(self):
        return f'{self.id}: {self.title} {self.id_publisher}'

class Shop(Base):
    __tablename__ = "shop"

    id = alh.Column(alh.Integer, primary_key=True)
    name = alh.Column(alh.Text, nullable=False)

    def __str__(self):
        return f'{self.id}: {self.name}'

class Stock(Base):
    __tablename__ = "stock"

    id = alh.Column(alh.Integer, primary_key=True)
    count = alh.Column(alh.Integer, nullable=False)
    id_book = alh.Column(alh.Integer, alh.ForeignKey("book.id"), nullable=False)
    publisher = relationship(Book, backref="stock.id")
    id_shop = alh.Column(alh.Integer, alh.ForeignKey("shop.id"), nullable=False)
    shop = relationship(Shop, backref="stock.id")

    def __str__(self):
        return f'{self.id}: {self.count} {self.id_book} {self.id_shop}'

class Sale(Base):
    __tablename__ = "sale"

    id = alh.Column(alh.Integer, primary_key=True)
    price = alh.Column(alh.Float, nullable=False)
    date_sale = alh.Column(alh.DateTime, nullable=False)
    count = alh.Column(alh.Integer, nullable=False)
    id_stock = alh.Column(alh.Integer, alh.ForeignKey("stock.id"), nullable=False)
    stock = relationship(Stock, backref="sale.id")

    def __str__(self):
        return f'{self.id}: {self.price} {self.date_sale} {self.count} {self.id_stock}'




def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

